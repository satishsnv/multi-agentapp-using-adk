from google.adk.agents import Agent
from agents.tools.metadata import update_metadata 
from constants import GEMINI_FLASH_MODEL
from agents.models import FileSummaryClassificationOutput

metadata_update_agent = Agent(
    name="metadata_update_agent",
    description="Specialist agent for updating the metadata",
    instruction="""
            You are an expert agent in updating the metadata. you should be using the tool to update the metadata
            you will be provided with the metadata in the session state with key 'aggregated_result'.
            you should pass the object FileSummaryClassificationOutput to the tool in order to update the metadata.
            return the output of the tool as it is, do not modify it.
            """,
    tools=[update_metadata],
    model=GEMINI_FLASH_MODEL,
    output_key="metadata_key"
)