# AgentLens: AI-Powered LLM Discovery Assistant

**AgentLens** is a local-first AI assistant designed to discover, analyze, and compare Large Language Models (LLMs) for agentic workflows. It uses a **Hybrid RAG (Retrieval-Augmented Generation)** approach, combining real-time web search with local LLM inference to provide up-to-date recommendations.

---

## 🚀 Features
* **Natural Language Discovery:** Describe a workflow, and the agent finds the best models for the task.
* **Real-time Web Integration:** Uses DuckDuckGo to bypass LLM knowledge cutoffs and find the latest frontier models.
* **Local-First Architecture:** Powered by **Ollama** and **Llama 3.2** for private, offline reasoning.
* **Local Inventory Check:** Automatically detects and displays metadata for models installed on your local machine.
* **Comparison Engine:** Provides structured tables comparing parameters, tool-calling support, and best use cases.

---

## 🛠️ Tech Stack
* **Language:** Python 3.11+
* **Package Manager:** `uv`
* **LLM Engine:** Ollama (Llama 3.2)
* **Libraries:** `pandas`, `python-dotenv`, `ddgs` (DuckDuckGo Search), `ollama-python`

---

## 📦 Installation & Setup

### 1. Prerequisites
Ensure you have [Ollama](https://ollama.com/) installed and the Llama 3.2 model pulled:
```bash
ollama pull llama3.2