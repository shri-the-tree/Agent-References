# main.py
from agents.editorial import EditorialAgent
from agents.intent_parser import IntentParserAgent
from agents.market_research import MarketResearchAgent
from agents.recommendation import RecommendationAgent
from config import AGENT_MODELS

def main():
    print("🚗 Welcome to AutoDriveGPT — Your Indian Car Buying Consultant\n")
    user_input = input("What are your requirements? (e.g., budget, usage, location): ")

    # STEP 1: Understand the user
    intent_agent = IntentParserAgent(model=AGENT_MODELS["intent_parser"])
    profile = intent_agent.run(user_input)

    if not profile:
        print("❌ Could not extract intent. Try again.")
        return

    print("\n🧠 Intent Profile:")
    for k, v in profile.items():
        print(f"  {k}: {v}")

    # STEP 2: Search cars
    market_agent = MarketResearchAgent(model=AGENT_MODELS["market_researcher"])
    car_list = market_agent.run(profile)

    print("\n🚘 Search-Based Car Options:")
    if isinstance(car_list, str):
        print(car_list)
        return

    for car in car_list:
        print(f"- {car['model']} ({car['price_estimate']})")

    # STEP 3: Re-rank & personalize
    recommendation_agent = RecommendationAgent(model=AGENT_MODELS["recommender"])
    final_recommendations = recommendation_agent.run(profile, car_list)

    print("\n🏁 Final Personalized Car Picks:")
    for car in final_recommendations:
        print(f"- {car['model']} ({car['price_estimate']}) → {car['why']}")

    # PREP for step 4
    print("\n✨ Want a magazine-style version of your recommendations? Say the word...")

    generate_magazine = input("\nWould you like to generate a magazine-style summary? (yes/no): ").strip().lower()
    if generate_magazine in ['yes', 'y']:
        editorial_agent = EditorialAgent()
        editorial_agent.run(profile, final_recommendations)

if __name__ == "__main__":
    main()
