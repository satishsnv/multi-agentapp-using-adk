from google.adk.agents import Agent, SequentialAgent
from constants import *
from google.adk.models.lite_llm import LiteLlm
from agents.models import FileSummaryClassificationOutput, FileContent
from agents.tools.content import fetch_file_content

content_processing_agent = Agent(
    name="processing_agent",
    description="Specialist agent for processing the file content",
    instruction="""
        You are expert in document processing. you will be provided with file content and its corresponding file_id.
        
        ```content to process
        
        {file_content}

        ```
        
        Use the content to generate the summary, classification and sentiment in FileSummaryClassificationOutput format. 
        You should return the FileSummaryClassificationOutput object only nothing else.    
        The summary should be concise and informative with maximum of 10 bullet points.
        The classification should be a list of top 5 classifications.
        The sentiment should be a sentiment object with label and score.
        The label should be one of the following: positive, negative, neutral. score should be a float between -1 and 1.
        include the file_id in the output.
        you should return the FileSummaryClassificationOutput object only nothing else.
    """,
    output_schema=FileSummaryClassificationOutput, 
    model=LiteLlm(model=GPT_4O_MINI_MODEL)
)


content_fetching_agent = Agent(
    name="content_fetching_agent",
    description="Specialist agent for fetching the file content",
    instruction="""
        You should utilize the tool for fetching file content. 
        You can ask for file_id or resourceids in the input, if not provided, you can ask the user to provide it.
        Tool will return the content in FileContent format .
        Return the FileContent returned by the tool as it is.
    """,
    tools=[fetch_file_content],
    model=GEMINI_FLASH_MODEL,
    output_key="file_content",  # This is the key that will be used to access the output of the tool
)


data_aggregating_agent = Agent(
    name="aggregating_agent",
    description="Specialist agent in aggregating given objects",
    instruction="""
        You are expert in aggregating the data objects.
        you will be provided with a list of FileSummaryClassificationOutput objects, they all have same file_id.
        You should generate the aggregated summary, classification and sentiment based on the provided objects.
        You should return the aggregated FileSummaryClassificationOutput object only nothing else.
        Aggregated summary should be summary of all summaries.
        Aggregated classification should be maximum repeated classifications, consider only top 5 classifications.
        Aggregated sentiment should be the weighted average sentiment score.     
        The label should be one of the following: positive, negative, neutral. score should be a float between -1 and 1.
        include the file_id in the output.
    """,
    model=LiteLlm(model=GPT_4O_MINI_MODEL)
)

content_management_agent = SequentialAgent(
    name="content_management_agent",
    description="Agent for managing the entire content processing tasks",
    sub_agents=[content_fetching_agent, content_processing_agent]
)
