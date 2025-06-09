# multi-agentapp-using-adk
Multi agent application using google adk

This is multiagent application using custom agent

custom agent is capable of processing the document using chunks based on the document size to avoid token limitation issues.
chunks are processed in sequence to avoid token per miniute issues

db agent is capable of generating sql queries from text

front desk agent/root agent is the one that handles the user queries. It is an autonomous agent and decides what to do based on user query.

db agent and custom agent uses tools for fetching the relevant data. 
Tools will mimic a fetch call and provide fake data, they can be replaced with proper logic to fetch real data 


# Running the application locally

clone the repo
go to the root directory
create .env file and copy the entities from .env_template
you should provide the OPENAI_API_KEY and GEMINI_API_KEY which are mandatory for inferencing the llms
install uv if not available in the system
run  
    uv venv
    uv sync
    adk web

happy browsing
