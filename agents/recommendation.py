# agents/recommendation.py

from agents.base_agent import BaseAgent
import json

class RecommendationAgent(BaseAgent):
    def run(self, user_profile, raw_car_list):
        print("\n🤖 Personalizing your recommendations...")

        prompt = f"""
You are a smart automotive consultant.

You will receive a user profile and a list of potential car options.
Your job is to re-rank the cars in the most personalized way for the user based on their use case, budget, and any preferences.
Respond with ONLY a JSON list in the format shown.

User Profile:
{json.dumps(user_profile, indent=2)}

Car List:
{json.dumps(raw_car_list, indent=2)}

Expected Output Format:
[
  {{
    "model": "Brand Model Name",
    "price_estimate": "₹X Lakh",
    "why": "Why this car fits THIS user"
  }},
  ...
]

Do not explain. Only return the JSON list.
"""
        response = self.call_llm(prompt)

        try:
            return json.loads(response)
        except:
            print("⚠️ Could not parse response. Raw output:")
            print(response)
            return []
