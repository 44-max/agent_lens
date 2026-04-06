import agent_core
import ollama_utils
import pandas as pd

def main():
    print("="*50)
    print("      AGENTLENS: LOCAL AI DISCOVERY ASSISTANT")
    print("="*50)

    query = input("\nDescribe your agentic workflow: ")

    # This now uses Llama 3.2 instead of OpenAI
    print("\n[1/2] Processing Recommendations...")
    recommendations = agent_core.get_recommendations(query)
    print("\n--- LLM RECOMMENDATIONS ---")
    print(recommendations)

    # Shows all your local models in a table
    print("\n[2/2] Local Ollama Library:")
    local_models = ollama_utils.get_local_models()
    if isinstance(local_models, list):
        print(pd.DataFrame(local_models))
    
    print("\n" + "="*50)
    print("Project: AgentLens | Status: Local-Mode Active")
    print("="*50)

if __name__ == "__main__":
    main()