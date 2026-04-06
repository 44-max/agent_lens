import ollama
from search_utils import perform_web_search # Ensure this matches your file name

def get_recommendations(user_query):
    # 1. Get real-time web data (This part is free!)
    print(f"🔍 Searching the web for: {user_query}...")
    web_context = perform_web_search(user_query)
    
    # 2. Use Llama 3.2 to process the recommendation
    print(f"🤖 Llama 3.2 is analyzing data for your workflow...")
    
    prompt = f"""
    You are an AI Discovery Assistant. Based on this web data:
    {web_context}
    
    Recommend the best LLMs for this workflow: '{user_query}'
    Provide: Model Name, Description, Parameters, and Tool Calling Support.
    Mention that Llama 3.2 (which you are currently using) is a great local choice.
    """
    
    try:
        response = ollama.chat(model='llama3.2', messages=[
            {'role': 'user', 'content': prompt},
        ])
        return response['message']['content']
    except Exception as e:
        return f"Local Model Error: {e}. Make sure 'ollama serve' is running."