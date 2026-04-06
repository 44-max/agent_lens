from ddgs import DDGS

def perform_web_search(query):
    """Searches the web for latest LLM data[cite: 18, 48]."""
    with DDGS() as ddgs:
        results = [r['body'] for r in ddgs.text(f"best LLMs for {query} agentic workflow", max_results=3)]
    return "\n".join(results)