from langchain.tools import tool,ToolRuntime
from schema import UserContext
import requests

# Resume analyzer tool
@tool
def get_weather(city: str) -> str:
    """Get real-time weather information for a city."""

    print("WEATHER API CALLED")

    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url)

    if response.status_code == 200:
        return response.text

    return "Weather information not available."

# User profile location using runtime context
@tool
def get_user_location(runtime: ToolRuntime[UserContext]) -> str:
    """
    Get user's city based on user_id.
    """

    user_id = runtime.context.user_id

    user_city_map = {
        "USER001": "Pune",
        "USER002": "Mumbai",
        "USER003": "Jalgaon",
        "USER004": "Tirupati"
    }

    city = user_city_map.get(user_id)

    return f"User is located in {city}, India."