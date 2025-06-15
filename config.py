# config.py

GROQ_API_KEY = ""
SERPAPI_KEY = ""


# Mapping each agent to a Groq-hosted model
AGENT_MODELS = {
    "intent_parser": "llama-3.1-8b-instant",
    "market_researcher": "qwen/qwen3-32b",
    "recommender": "mixtral-8x7b-32768",
    "advisor": "llama3-8b-8192",
    "editorial_writer": "mixtral-8x7b-32768"
}

GROQ_API_BASE = "https://api.groq.com/openai/v1/chat/completions"
