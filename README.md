# LangGraph Agentic AI Chatbot

This project implements a versatile Agentic AI Chatbot using LangGraph, featuring a user-friendly Streamlit interface. It's designed to be easily configurable and extensible, supporting multiple Large Language Models (LLMs) and various use cases.

## Features

*   **Multi-LLM Support:** Seamlessly switch between different LLM providers, including:
    *   **Groq:** (llama3-8b-8192, llama3-70b-8192, gemma2-9b-it)
    *   **OpenAI:** (gpt-4o, gpt-3.5-turbo)
    *   **Gemini:** (gemini-1.5-pro-latest, gemini-1.0-pro)
    *   **DeepSeek:** (deepseek-chat, deepseek-coder)
*   **Dynamic UI:** The Streamlit interface dynamically adjusts model selection and API key inputs based on the chosen LLM.
*   **Configurable Use Cases:** Supports various agentic use cases, such as:
    *   Basic Chatbot
    *   Chatbot with Tool
    *   AI News
    *   Blog Generator
*   **Modular Design:** The codebase is structured to allow easy addition of new LLMs, tools, and use cases.
*   **API Key Management:** Securely handles API keys via Streamlit's text input (for local development).

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd "ETE project chatbot" # Or the name of your cloned directory
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

Install all required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

The application requires API keys for the LLM providers you intend to use. You will enter these directly in the Streamlit UI when you run the application.

### 5. Run the Application

Start the Streamlit application from the project's root directory:

```bash
streamlit run app.py
```

Your browser should automatically open to the Streamlit application. If not, navigate to `http://localhost:8501`.

## Project Structure

```
.
├── app.py                      # Main Streamlit application entry point
├── README.md                   # This file
├── requirements.txt            # Python dependencies
└── src/
    ├── langgraphagenticai/
    │   ├── LLMs/               # LLM integration classes (Groq, OpenAI, Gemini, DeepSeek)
    │   ├── graph/              # LangGraph graph building logic
    │   ├── nodes/              # LangGraph nodes for different agent steps
    │   ├── state/              # LangGraph state definition
    │   ├── tools/              # Custom tools for agents
    │   └── ui/                 # Streamlit UI components
    │       ├── streamlitui/    # Specific Streamlit UI elements (loadui, display_result)
    │       └── uiconfigfile.ini# Configuration file for UI options and models
    │       └── uiconfigfile.py # Python class to read uiconfigfile.ini
    └── __init__.py
```

## Configuration

The `src/langgraphagenticai/ui/uiconfigfile.ini` file contains configurable options for the UI and available models. You can modify this file to:

*   Change the `PAGE_TITLE`.
*   Adjust `LLM_OPTIONS` to enable/disable specific LLMs.
*   Modify `USECASE_OPTIONS` to define available use cases.
*   Update model lists for each LLM (e.g., `GROQ_MODEL_OPTIONS`).

## Contributing

Feel free to fork the repository, open issues, or submit pull requests.

---