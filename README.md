# 🤖 Smart Code Reviewer (LangGraph + Streamlit)

This project is a Streamlit-based Agentic AI application that performs intelligent code review on uploaded Java projects using the [LangGraph](https://github.com/langchain-ai/langgraph) framework and [DeepSeek](https://deepseek.com) LLM via LiteLLM.

---

## 🚀 Features

- Upload a ZIP of your Java codebase.
- Multi-agent review:
  - ✅ Naming convention analysis
  - 🧠 Code smell detection
  - 🔐 Security flaw detection
- Agent collaboration using LangGraph.
- Real-time feedback through a Streamlit UI.
- Supports `DeepSeek` LLM via `LiteLLM`.

---

## 🛠️ Tech Stack

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LiteLLM](https://docs.litellm.ai)
- [DeepSeek LLM](https://platform.deepseek.com)
- [Streamlit](https://streamlit.io)
- Python 3.10+

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/smart-code-reviewer-langgraph.git
cd smart-code-reviewer-langgraph
python -m venv my_env
source my_env/bin/activate  # Windows: my_env\Scripts\activate
pip install -r requirements.txt
