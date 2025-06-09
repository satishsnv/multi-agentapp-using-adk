from google.adk.agents import Agent
from agents.tools.database import fetch_db_constraints_and_metadata
from constants import GEMINI_FLASH_MODEL

db_agent = Agent(
    name="database_agent",
    description="Specialist agent for generating the queries",
    instruction="""
            You are an expert agent in generating the queries provided the contraints and metadata of database. 
            You should call the tool to fetch the constraints and metadata of the database using the unique identifier.
            ask the user for resource_id if not provided.
            Call the tool using the resource_id provided by the user.
            Generate the valid query with the help of metadata provided by the tool.
            you should return the valid sql query only.
            """,
    tools=[fetch_db_constraints_and_metadata],
    model=GEMINI_FLASH_MODEL
)
