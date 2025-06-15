# agents/editorial.py

from tools.html_renderer import render_html

class EditorialAgent:
    def __init__(self):
        pass  # No LLM needed here, just formatting

    def run(self, user_profile, cars):
        # Ensure there's at least placeholder images if not provided
        for car in cars:
            if not car.get("image_url"):
                car["image_url"] = "https://via.placeholder.com/500x300?text=Car+Image"
        render_html(user_profile, cars)
