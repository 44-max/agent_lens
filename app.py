from agent_core import get_llm_recommendations
from ollama_utils import get_local_models
import pandas as pd

def main():
    print("--- AgentLens: AI-Powered LLM Discovery Assistant --- [cite: 6]")
    query = input("\nDescribe your agentic workflow (e.g., 'marketing automation agent'): ") [cite: 52]
    
    print("\n🔍 Step 1: Searching the web for the latest LLM data...")
    recommendations = get_llm_recommendations(query)
    
    print("\n--- CLOUD MODEL RECOMMENDATIONS --- [cite: 18]")
    print(recommendations)
    
    print("\n--- LOCAL MODELS (OLLAMA) --- [cite: 65, 75]")
    local_data = get_local_models()
    if isinstance(local_data, list):
        # Presenting local models alongside cloud recommendations [cite: 64]
        df = pd.DataFrame(local_data)
        print(df)
        
        # Specifically highlighting Llama 3.2 suitability [cite: 76]
        if any("llama3.2" in m['Model Name'].lower() for m in local_data):
            print("\n💡 NOTE: Llama 3.2 is locally installed and suitable for edge agentic tasks.")
    else:
        print(local_data)

if __name__ == "__main__":
    main()