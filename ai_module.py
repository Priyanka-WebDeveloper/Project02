# ai_module.py

def generate_itinerary(city: str, days: int) -> str:
    """
    Generates a simple travel itinerary for a given city and number of days.
    """
    return (
        f"Here’s a {days}-day itinerary for {city}:\n"
        "- Explore main attractions\n"
        "- Try local food\n"
        "- Enjoy cultural experiences"
    )

def travel_tips(city: str) -> str:
    """
    Provides general travel tips for a given city.
    """
    return (
        f"Tips for {city}:\n"
        "- Carry essentials\n"
        "- Respect local culture\n"
        "- Keep some cash handy"
    )
