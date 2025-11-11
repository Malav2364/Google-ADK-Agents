from google.adk.agents.llm_agent import Agent

#Mock Tool Implementation
def get_current_time(city : str) -> dict:
    """Returns the current time in a specified city."""
    return{
        "status": "success",
        "city" : city,
        "time" : "10:30 AM"
    }
def get_current_weather(city : str) -> dict:
    """Returns the current weather in a specified city."""
    return{
        "status": "success",
        "city" : city,
        "weather" : "Sunny, 25°C"
    }

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Tells the current time in a specified city.',
    instruction='You are a helpful assistant that tells the current time  or weather in cities. Use the \'get_current_time\' and \'get_current_weather\' tools for this purpose.',
    tools=[get_current_time, get_current_weather],
)
