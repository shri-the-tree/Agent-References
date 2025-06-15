from agents.base_agent import BaseAgent
import json
import re

class IntentParserAgent(BaseAgent):
    def run(self, user_input):
        prompt = f"""
You are an intent understanding agent for a car consultant in India.
Given the user's input, extract the following as JSON:
- budget_in_inr: estimated budget in rupees
- primary_use_case: e.g., city drive, highway, family, off-road, etc.
- user_location: city or state if mentioned
- passenger_count: optional
- fuel_preference: optional
- extra_notes: anything else relevant

Input: \"{user_input}\"

Respond with only the JSON. Do not explain.
"""
        response = self.call_llm(prompt)

        # Remove any markdown code block formatting
        clean_response = re.sub(r"^```(?:json)?|```$", "", response.strip(), flags=re.MULTILINE)

        try:
            return json.loads(clean_response)
        except Exception as e:
            print("❗ Failed to parse response into JSON. Raw output:")
            print(response)
            print("\nError:", str(e))
            return {}