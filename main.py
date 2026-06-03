from flask import Flask, render_template, request
from travel_data import find_destinations
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    trip_type = budget = season = days = None
    days_int = 0  # ✅ Initialize here to avoid UnboundLocalError

    if request.method == "POST":
        trip_type = request.form.get("trip_type")
        budget = request.form.get("budget")
        season = request.form.get("season")
        days = request.form.get("days")

        # Ensure days_int is always an integer
        days_int = int(days) if days and days.isdigit() else 0

        matches = find_destinations(trip_type, budget, season)
        if matches:
            destination = random.choice(matches)
            avg_cost = destination.get("avg_cost_per_day", 5000)
            total_cost = avg_cost * days_int

            result = {
                "city": destination["city"],
                "attractions": destination.get("attractions", []),
                "total_cost": total_cost,
                "itinerary": f"Day-wise plan for {destination['city']}.",
                "tips": f"Recommended season: {destination.get('season', 'N/A').capitalize()}."
            }
        else:
            result = {"error": "No destinations found matching your preferences."}

    return render_template(
        "index.html",
        result=result,
        trip_type=trip_type,
        budget=budget,
        season=season,
        days=days_int  # ✅ Now always defined
    )


if __name__ == "__main__":
    app.run(debug=True)
