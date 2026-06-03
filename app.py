from flask import Flask, render_template, request
from travel_data import find_destinations
from ai_module import generate_itinerary, travel_tips

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = {}
    if request.method == "POST":
        trip_type = request.form.get("trip_type")
        budget = request.form.get("budget")
        season = request.form.get("season")
        days = request.form.get("days")

        # Validate days input
        if not days or int(days) < 1:
            result = {"error": "Please enter a valid number of days."}
            return render_template("index.html", result=result)

        # Find matching destinations
        destinations = find_destinations(trip_type, budget, season)
        if destinations:
            selected = destinations[0]  # pick first match
            total_cost = selected['avg_cost_per_day'] * int(days)

            itinerary = generate_itinerary(selected['city'], days)
            tips = travel_tips(selected['city'])

            result = {
                "city": selected['city'],
                "attractions": selected['attractions'],
                "total_cost": total_cost,
                "itinerary": itinerary,
                "tips": tips
            }
        else:
            result = {"error": "No destinations match your preferences."}

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
