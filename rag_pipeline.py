from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.tools import create_retriever_tool
import os
from dotenv import load_dotenv

load_dotenv()


embeddings=GoogleGenerativeAIEmbeddings(model='gemini-embedding-001')

documents = [
    """Climate: Extreme Heat (Above 35°C)
    Clothing: Wear light cotton clothes, hat, sunglasses.
    Safety: Drink water frequently, avoid 12-4 PM sun, use SPF 30+ sunscreen.
    Risk: Heat exhaustion and dehydration.""",

    """Climate: Warm Weather (25-35°C)
    Clothing: Light breathable clothes.
    Safety: Stay hydrated, avoid long sun exposure.""",

    """Climate: Rainy Conditions
    Clothing: Raincoat, waterproof footwear.
    Safety: Avoid flooded areas, slippery roads, carry umbrella.""",

    """Climate: Cold Weather (Below 15°C)
    Clothing: Layered clothing, wool sweaters, gloves.
    Safety: Keep body warm, drink warm fluids.""",

    """Climate: Extreme Cold (Below 5°C)
    Clothing: Heavy insulated jackets, thermal layers.
    Safety: Limit outdoor exposure, watch for hypothermia.""",

    """Climate: Thunderstorm
    Clothing: Waterproof outerwear.
    Safety: Stay indoors, avoid trees, unplug appliances.""",

    """Climate: High Humidity
    Clothing: Lightweight breathable fabrics.
    Safety: Stay ventilated, drink electrolyte fluids."""
]

vector_store = FAISS.from_texts(documents, embedding=embeddings)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})

retriever_tool = create_retriever_tool(
    retriever,
    name="kb_search",
    description="""Mandatory tool.
    Use this tool to retrieve climate-based clothing and safety advice.
    Always use before answering."""
)