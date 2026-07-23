from google.adk.agents import Agent
from greeting_agent.agent import root_agent as greeting_agent
from incident_analysis_agent.agent import root_agent as incident_analysis_agent

from google.adk.models.lite_llm import LiteLlm



root_agent = Agent(
    name = "multiagent",
    description = "Routes user requests to the appropriate specialist agent.",
    model=LiteLlm(
            model="groq/llama-3.3-70b-versatile"
        ),
    sub_agents=[greeting_agent,incident_analysis_agent],
    instruction="""
                You are a coordinator agent.
                you are a multiagent system which perform various task on the basis of 
                given first use greeting_agent to greet the user and then ask how can you help? 
                when user provide their problem then use incident_analysis_agent to analyze the incident and produce a structured report.
                """)