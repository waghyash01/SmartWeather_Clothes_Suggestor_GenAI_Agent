from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

from models import basic_model
from tools import get_weather,get_user_location
from rag_pipeline import retriever_tool
from middleware.dynamic_model import dynamic_model_selection
from middleware.dynamic_prompt import role_based_prompt
from schema import UserContext, AgentResponse

checkpointer = InMemorySaver()

agent = create_agent(
    model=basic_model,
    tools=[get_weather, get_user_location, retriever_tool],
    
    middleware=[
        dynamic_model_selection,
        role_based_prompt
    ],
    system_prompt= '''
        You are a Smart Climate Assistant.

If image is provided:
1. Analyze clothing or environment.
2. Call weather tool for current city.
3. Retrieve safety guidelines from RAG.
4. Combine all data.
5. Give personalized advice.

Always use weather tool first.
Always use kb_search tool after weather.
                   ''',
    context_schema=UserContext,
    response_format=AgentResponse,
    checkpointer=checkpointer
)