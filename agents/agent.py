from google.adk.agents import Agent
from constants import GEMINI_FLASH_MODEL
from agents.subagents.content import content_management_agent
from agents.subagents.database import db_agent
from dotenv import load_dotenv

load_dotenv()

root_agent = Agent(
    name="front_desk_agent",
    model=GEMINI_FLASH_MODEL,
    description="Delegates the task to the specialized agents based input.",
    instruction="""
                You are an experienced front desk agent helping the users on their queries.
                You are provisioned with multiple specialized agents to help you with the tasks.
                You should delegate the tasks based on user question invoke the correct agent.
                If you are not sure about the task, you can ask the user for more information.
                You should return the response from the specialized agent as it is.
                If there is no specialized agent available for the task, you can decide how to proceed.
                """,
    sub_agents=[content_management_agent, db_agent],
)