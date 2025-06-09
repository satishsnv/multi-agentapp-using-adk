from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from constants import GPT_4O_MINI_MODEL
from agents.subagents.content import custom_processing_agent
from agents.subagents.database import db_agent
from dotenv import load_dotenv

load_dotenv()

root_agent = Agent(
    name="front_desk_agent",
    model=LiteLlm(model=GPT_4O_MINI_MODEL),
    description="Delegates the task to the specialized agents based input.",
    instruction="""
                You are an experienced front desk agent helping the users on their queries.
                You are provisioned with couple of specialized agents to help you with the tasks.
                You should analyze the user question and decide which specialized agent to invoke.
                Try to handle the queries on your own if the query can't be handled by the specialized agents.                
                """,
    sub_agents=[custom_processing_agent, db_agent],
)