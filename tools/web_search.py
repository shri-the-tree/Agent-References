# tools/web_search.py

from serpapi import GoogleSearch  # this comes from the `google-search-results` package
from config import SERPAPI_KEY

def search_google(query, num_results=5):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": num_results
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return [
        {
            "title": r.get("title"),
            "link": r.get("link"),
            "snippet": r.get("snippet", "")
        }
        for r in results.get("organic_results", [])
    ]
