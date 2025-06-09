from google.adk.agents import Agent
from constants import *
from google.adk.models.lite_llm import LiteLlm
from agents.models import FileSummaryClassificationOutput
from agents.tools.content import fetch_file_content
from agents.subagents.custom_agent import CustomProcessingAgent
from agents.subagents.metadata import metadata_update_agent


processing_agent = Agent(
    name="processing_agent",
    description="Specialist agent for processing the file content",
    instruction="""
        You are expert in document processing. 
        Analyze the provided FileContent object in the session state with key 'file_content_key' and
        Use the file_content attribute to generate the summary, classification and sentiment of the content in FileSummaryClassificationOutput format. 
        You should return the FileSummaryClassificationOutput object only nothing else.    
        The summary should be concise and informative with maximum of 10 points.
        The classification should be a list of top 2-3 classifications.
        The sentiment should be a sentiment object with label and score.
        The label should be one of the following: positive, negative. score should be a float between -1 and 1.
        include the file_id in the output.
        you should return the FileSummaryClassificationOutput as a valid json string.
    """, 
    model=LiteLlm(model=GPT_4O_MINI_MODEL),
    output_key="file_summary_classification_output",  # This is the key that will be used to access the output of the tool
)

fetching_agent = Agent(
    name="fetching_agent",
    description="Specialist agent for fetching the file content",
    instruction="""
        You are expert in fetching the file content. check for the unique identifier and use it to fetch the file content.
        If the file_id is not provided, ask the user for it.
        You should return the FileContent object only nothing else.
        The FileContent object should contain the file_content attribute which is a list of strings and the file_id attribute.
        Return the FileContent object provided by the tool as it is, do not modify it.
    """,
    tools=[fetch_file_content],
    model=LiteLlm(model=GPT_4O_MINI_MODEL),
    output_key="file_content_key",  # This is the key that will be used to access the output of the tool
)


aggregating_agent = Agent(
    name="aggregating_agent",
    description="Specialist agent in aggregating given objects",
    instruction="""
        You are expert in aggregating the data objects.
        Analyze the provided list of FileSummaryClassificationOutput objects in session state with key 'file_summary_classification_output' and
        aggregate them in to a single FileSummaryClassificationOutput object.
        Aggregated summary should be summary of all summaries.
        Aggregated classification should be maximum repeated classifications, consider only top 2-3 classifications.
        Aggregated sentiment should be the weighted average sentiment score.     
    """,
    output_schema=FileSummaryClassificationOutput,
    model=LiteLlm(model=GPT_4O_MINI_MODEL),
    output_key="aggregated_result"
)

custom_processing_agent = CustomProcessingAgent(
    name="custom_processing_agent",
    description="A custom agent for processing documents of any size with specific logic.",
    fetching_agent=fetching_agent,
    processing_agent=processing_agent,
    aggregating_agent=aggregating_agent,
    metadata_update_agent=metadata_update_agent
)
