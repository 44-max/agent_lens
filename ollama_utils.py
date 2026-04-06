import ollama

def get_local_models():
    try:
        response = ollama.list()
        local_list = []
        for model in response['models']:
            local_list.append({
                "Model Name": model['name'],
                "Parameters": model['details'].get('parameter_size', 'Unknown'),
                "Quantization": model['details'].get('quantization_level', 'Unknown')
            })
        return local_list
    except Exception as e:
        return f"Error: {e}"

# --- EXECUTION BLOCK ---
if __name__ == "__main__":
    print("🔍 Checking for Llama 3.2 in Ollama...")
    models = get_local_models()
    if isinstance(models, list):
        for m in models:
            if "llama3.2" in m['Model Name'].lower():
                print(f"✅ Found Model: {m['Model Name']} | Size: {m['Parameters']}")
    else:
        print(models)