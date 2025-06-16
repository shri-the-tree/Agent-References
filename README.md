# AutoDriveGPT 🚗

**Premium Multi-Agent Car Consulting System for India**

AutoDriveGPT is an intelligent automotive consultant that uses multiple specialized AI agents to provide personalized car recommendations with magazine-style output.

## Architecture

The system employs a **multi-agent pipeline** where each agent has a specific role:

1. **Intent Parser Agent** - Extracts structured requirements from natural language
2. **Market Research Agent** - Searches live car data and creates recommendations  
3. **Recommendation Agent** - Re-ranks and personalizes suggestions
4. **Editorial Agent** - Generates premium magazine-style HTML output

## Features

- **Live Web Search** - Real-time car data from Indian automotive websites
- **Multi-Model LLM** - Different specialized models for each agent task
- **Premium Output** - Magazine-quality HTML reports with styling
- **Indian Market Focus** - Tailored for Indian car buying (₹ pricing, local brands)

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Keys
Create `.env` file:
```env
GROQ_API_KEY=your_groq_api_key
SERPAPI_KEY=your_serpapi_key
```

Get keys from:
- [Groq API](https://console.groq.com/keys) (free tier available)
- [SerpAPI](https://serpapi.com/dashboard) (100 free searches/month)

### 3. Run Setup Check
```bash
python setup.py
```

### 4. Launch Application
```bash
python main.py
```

## Example Usage

```
What are your requirements? 
> 7 seater SUV under 20 lakhs with off-road capability

🧠 Intent Profile:
  budget_in_inr: 2000000
  primary_use_case: off-road
  passenger_count: 7
  
🔍 Searching live car listings...
🚘 Search-Based Car Options:
- Mahindra Thar (₹11.50-17.62 Lakh)
- Maruti Jimny (₹10-15 Lakh)

🤖 Personalizing your recommendations...
🏁 Final Personalized Car Picks:
- Mahindra Thar → Perfect off-road capability with 7-seater variants

📰 Magazine generated: output/user_magazine.html
```

## Agent Models

Each agent uses optimized models from Groq:

- **Intent Parser**: `llama-3.1-8b-instant`
- **Market Research**: `llama-3.1-70b-versatile` 
- **Recommendation**: `mixtral-8x7b-32768`
- **Editorial**: `mixtral-8x7b-32768`

## Project Structure

```
AgenticAI/
├── agents/
│   ├── intent_parser.py    # Natural language → structured data
│   ├── market_research.py  # Web search → car recommendations
│   ├── recommendation.py   # Personalization & ranking
│   └── editorial.py        # HTML magazine generation
├── tools/
│   ├── web_search.py       # SerpAPI integration
│   ├── html_renderer.py    # Jinja2 template rendering
│   └── car_data.json       # Static car database
├── templates/
│   └── magazine_template.html
├── output/
│   └── user_magazine.html
├── config.py               # API keys & model configuration
└── main.py                # Main application pipeline
```

## Research Focus

This project explores:

- **Multi-agent coordination** - How specialized agents collaborate
- **Tool integration** - Combining web search, LLMs, and rendering
- **Real-time data processing** - Live market research capabilities
- **Personalization at scale** - Tailored recommendations from generic data

## Extending the System

### Adding New Agents
1. Create agent class inheriting from `BaseAgent`
2. Implement `run()` method with specific logic
3. Add model mapping in `config.py`
4. Integrate into main pipeline

### Adding New Tools
1. Create tool module in `tools/` directory
2. Import and use in relevant agents
3. Update requirements if external dependencies needed

### Customizing Output
- Modify `templates/magazine_template.html` for different styling
- Update `editorial.py` for new output formats
- Add image fetching, pricing APIs, or other enhancements

## License

Research and educational use only.
