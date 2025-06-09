from google.adk.agents import BaseAgent, LlmAgent
from google.adk.events.event import Event
from typing_extensions import override
from google.adk.agents.invocation_context import InvocationContext
from typing import AsyncGenerator, List
from agents.models import FileContent, FileSummaryClassificationOutput

import logging
import json

logger = logging.getLogger(__name__)

class CustomProcessingAgent(BaseAgent):
    """A custom agent for processing documents of any size with specific logic.
    This agent is intelligent enough to handle document processing tasks based on content size.
    """
    fetching_agent: LlmAgent
    processing_agent: LlmAgent
    aggregating_agent: LlmAgent
    metadata_update_agent: LlmAgent

    model_config = {"arbitrary_types_allowed": True}

    def __init__(self, name: str, description: str, fetching_agent: LlmAgent, processing_agent: LlmAgent, aggregating_agent: LlmAgent, metadata_update_agent: LlmAgent):

        subagents = [fetching_agent, processing_agent, aggregating_agent, metadata_update_agent]

        super().__init__(name=name, description=description,
                         sub_agents=subagents,
                         fetching_agent=fetching_agent,
                         processing_agent=processing_agent,
                         aggregating_agent=aggregating_agent,
                         metadata_update_agent=metadata_update_agent
                     )



    @override
    async def _run_async_impl(self, ctx: InvocationContext ) -> AsyncGenerator[Event, None]:
        # Implement the custom logic for running the agent asynchronously
        logger.info(f"Running custom processing agent: {self.name}")
        file_summary: List[FileSummaryClassificationOutput] = []

        # fetch the file content using the fetching agent
        async for event in self.fetching_agent.run_async(ctx):
            yield event
        
        logger.info("File content fetched successfully.")   

        # get the file content from the context and update so as process in chunks
        data = ctx.session.state.get("file_content_key")
        if not data:
            logger.error("No file content found. Exiting the Agent.")
            return
        logger.info(f"File content found: {data}")
        if isinstance(data, str):   
            data = FileContent.model_validate_json(data)
        elif isinstance(data, FileContent):
            logger.info("Data is already a FileContent object.")
        else:
            logger.error("Invalid file content data type. Expected FileContent or JSON string.")

        file_id = data.file_id

        # process the file content using the processing agent
        counter = 0
        for content in data.file_content:
            counter += 1
            chunk = FileContent()
            chunk.file_id = file_id
            chunk.file_content = [content]  # process one chunk at a time
            logger.info(f"Processing chunk for file_id: {file_id}, item: {counter}")
            ctx.session.state["file_content_key"] = chunk.model_dump_json()


            # process the chunk of file content
            async for event in self.processing_agent.run_async(ctx):
                yield event
            logger.info(f"File chunk processed successfully.")
            output = ctx.session.state.get("file_summary_classification_output")
            logger.info(f"chunk summary output: {output}")
            if isinstance(output, str):   
                output = FileSummaryClassificationOutput.model_validate_json(output)
            elif isinstance(output, FileSummaryClassificationOutput):
                logger.info("Data is already a FileSummaryClassificationOutput object.")
            else:
                logger.error("Invalid file content data type. Expected FileSummaryClassificationOutput or JSON string.")
                
            file_summary.append(output)


        logger.info("Processed all the chunks successfully.")

        # aggregate the file summary using the aggregating agent
        summary_array = json.dumps([summary_output.model_dump() for summary_output in file_summary])
        ctx.session.state["file_summary_classification_output"] = summary_array
        async for event in self.aggregating_agent.run_async(ctx):
            yield event

        logger.info(f"Aggregated result is {ctx.session.state.get('aggregated_result')} successfully.")

        # update the metadata using the metadata update agent
        async for event in self.metadata_update_agent.run_async(ctx):
            yield event

        logger.info(f"updated the metadata {ctx.session.state.get('metadata_key')} successfully.")