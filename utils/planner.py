ACTIVITIES = {
    "adventure": [
        "Mountain hiking",
        "Ziplining",
        "Kayaking",
        "Scuba diving",
        "ATV tour"
    ],
    "luxury": [
        "Fine dining",
        "Spa experience",
        "Luxury shopping",
        "Private city tour",
        "Rooftop cocktail night"
    ],
    "budget": [
        "Free walking tour",
        "Street food exploration",
        "Public beach visit",
        "Local market visit",
        "Museum discount day"
    ],
    "cultural": [
        "Museum visit",
        "Historical landmark tour",
        "Local cooking class",
        "Art gallery visit",
        "Traditional music show"
    ]
}


def generate_daily_plan(days, style, real_attractions=None):
    style = style.lower()
    itinerary = []

    if real_attractions and len(real_attractions) > 0:
        activities = real_attractions
    else:
        if style not in ACTIVITIES:
            raise ValueError("Invalid travel style.")

        activities = ACTIVITIES[style]

    for i in range(days):
        activity = activities[i % len(activities)]
        itinerary.append(f"Day {i+1}: {activity}")

    return itinerary