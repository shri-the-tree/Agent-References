# tools/car_database.py

import json
import os


# You can replace this with a real API or scraper later.
def load_car_data():
    path = os.path.join(os.path.dirname(__file__), 'car_data.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def find_cars(user_profile, limit=5):
    budget = user_profile.get("budget_in_inr")
    preferred_brand = user_profile.get("extra_notes", "").lower()

    cars = load_car_data()
    filtered = []

    for car in cars:
        # Budget filter only if budget is specified
        if budget is not None and car['price_inr'] > budget:
            continue
        if preferred_brand and preferred_brand not in car['brand'].lower():
            continue
        filtered.append(car)

    return filtered[:limit]
