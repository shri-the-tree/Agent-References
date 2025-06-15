# config.py

GROQ_API_KEY = "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"
SERPAPI_KEY = "8585258d1a1c2a76ef264754d2638e86eb4d0705cf80de79923b792789bdc921"


# Mapping each agent to a Groq-hosted model
AGENT_MODELS = {
    "intent_parser": "llama-3.1-8b-instant",
    "market_researcher": "qwen/qwen3-32b",
    "recommender": "mixtral-8x7b-32768",
    "advisor": "llama3-8b-8192",
    "editorial_writer": "mixtral-8x7b-32768"
}

GROQ_API_BASE = "https://api.groq.com/openai/v1/chat/completions"
