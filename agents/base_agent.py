# agents/base_agent.py

import requests
from config import GROQ_API_KEY, GROQ_API_BASE

class BaseAgent:
    def __init__(self, model):
        self.model = model

    def call_llm(self, prompt):
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        response = requests.post(GROQ_API_BASE, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            raise Exception(f"LLM call failed: {response.status_code} - {response.text}")
