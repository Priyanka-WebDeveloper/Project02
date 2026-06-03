# travel_data.py

# Expanded dataset
DESTINATIONS = [
    # 🌴 Beach Trips
    {
        "city": "Goa",
        "trip_type": "beach",
        "budget": "medium",
        "season": "winter",
        "avg_cost_per_day": 5000,
        "attractions": ["Beaches", "Water Sports", "Nightlife"]
    },
    {
        "city": "Kerala",
        "trip_type": "beach",
        "budget": "low",
        "season": "summer",
        "avg_cost_per_day": 3500,
        "attractions": ["Backwaters", "Beaches", "Houseboats"]
    },
    {
        "city": "Maldives",
        "trip_type": "beach",
        "budget": "high",
        "season": "summer",
        "avg_cost_per_day": 15000,
        "attractions": ["Beaches", "Resorts", "Scuba Diving"]
    },

    # 🏔️ Adventure Trips
    {
        "city": "Manali",
        "trip_type": "adventure",
        "budget": "low",
        "season": "summer",
        "avg_cost_per_day": 3000,
        "attractions": ["Mountains", "Trekking", "River Rafting"]
    },
    {
        "city": "Rishikesh",
        "trip_type": "adventure",
        "budget": "medium",
        "season": "spring",
        "avg_cost_per_day": 4000,
        "attractions": ["Rafting", "Camping", "Yoga Retreats"]
    },
    {
        "city": "Switzerland",
        "trip_type": "adventure",
        "budget": "high",
        "season": "winter",
        "avg_cost_per_day": 20000,
        "attractions": ["Skiing", "Alps", "Snowboarding"]
    },

    # 🏰 Cultural Trips
    {
        "city": "Jaipur",
        "trip_type": "cultural",
        "budget": "medium",
        "season": "winter",
        "avg_cost_per_day": 4000,
        "attractions": ["Forts", "Palaces", "Local Bazaars"]
    },
    {
        "city": "Varanasi",
        "trip_type": "cultural",
        "budget": "low",
        "season": "autumn",
        "avg_cost_per_day": 2500,
        "attractions": ["Ghats", "Temples", "Ganga Aarti"]
    },
    {
        "city": "Kyoto",
        "trip_type": "cultural",
        "budget": "high",
        "season": "spring",
        "avg_cost_per_day": 12000,
        "attractions": ["Shrines", "Cherry Blossoms", "Tea Houses"]
    },

    # 💞 Romantic Trips
    {
        "city": "Maldives",
        "trip_type": "romantic",
        "budget": "high",
        "season": "summer",
        "avg_cost_per_day": 15000,
        "attractions": ["Private Beaches", "Luxury Resorts", "Couple Activities"]
    },
    {
        "city": "Paris",
        "trip_type": "romantic",
        "budget": "high",
        "season": "spring",
        "avg_cost_per_day": 18000,
        "attractions": ["Eiffel Tower", "Seine River Cruise", "Museums"]
    },
    {
        "city": "Udaipur",
        "trip_type": "romantic",
        "budget": "medium",
        "season": "winter",
        "avg_cost_per_day": 6000,
        "attractions": ["Lakes", "Palaces", "Boat Rides"]
    },

    # 👨‍👩‍👧 Family Trips
    {
        "city": "Singapore",
        "trip_type": "family",
        "budget": "high",
        "season": "summer",
        "avg_cost_per_day": 14000,
        "attractions": ["Universal Studios", "Marina Bay Sands", "Gardens by the Bay"]
    },
    {
        "city": "Ooty",
        "trip_type": "family",
        "budget": "low",
        "season": "spring",
        "avg_cost_per_day": 3000,
        "attractions": ["Botanical Gardens", "Toy Train", "Tea Plantations"]
    },
    {
        "city": "Dubai",
        "trip_type": "family",
        "budget": "medium",
        "season": "winter",
        "avg_cost_per_day": 10000,
        "attractions": ["Burj Khalifa", "Desert Safari", "Theme Parks"]
    },
]


def find_destinations(trip_type, budget, season):
    # ✅ First try exact matches
    matches = [
        d for d in DESTINATIONS
        if d["trip_type"] == trip_type and d["budget"] == budget and d["season"] == season
    ]
    if matches:
        return matches

    # ✅ Fallback: match only trip_type
    matches = [d for d in DESTINATIONS if d["trip_type"] == trip_type]
    if matches:
        return matches

    # ✅ Last fallback: return all
    return DESTINATIONS
