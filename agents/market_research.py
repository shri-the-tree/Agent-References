# agents/market_research.py

from agents.base_agent import BaseAgent
from tools.web_search import search_google

class MarketResearchAgent(BaseAgent):
    def run(self, user_profile):
        print("\n🔍 Searching live car listings...")

        # Construct a user-tailored search query
        budget = user_profile.get("budget_in_inr", 1500000)
        use_case = user_profile.get("primary_use_case", "")
        extra = user_profile.get("extra_notes", "")

        search_query = f"best {use_case} cars under ₹{budget:,} in India 2025 {extra} site:cardekho.com"

        results = search_google(search_query, num_results=6)

        if not results:
            return "Sorry, no relevant search results found."

        context = "\n\n".join(
            f"{r['title']}\n{r['snippet']}\n{r['link']}" for r in results
        )

        prompt = f"""
You are a car advisor. Based on the following user profile and live search results, recommend 3 car models that best fit.

User Profile:
{user_profile}

Web Results:
{context}

Please return a JSON list of car recommendations in the following format:
[
  {{
    "model": "Brand Model Name",
    "price_estimate": "₹X Lakh",
    "why": "Short justification tailored to the user"
  }},
  ...
]
Only return the JSON. No explanation.
"""
        response = self.call_llm(prompt)

        return response
