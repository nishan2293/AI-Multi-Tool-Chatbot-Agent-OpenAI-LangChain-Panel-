# 🤖 AI Multi-Tool Chatbot

This is an AI-powered multi-tool chatbot that utilizes **OpenAI Function Calling** and **LangChain Agents** to dynamically select and invoke tools based on natural language queries. It includes:

- 🌦 Real-time weather fetching using Open-Meteo API
- 📚 Wikipedia search and summarization
- 🔁 Text reversal utility

### 🔧 Technologies Used

- LangChain
- OpenAI API (Function Calling)
- Panel (for interactive UI)
- Python (requests, wikipedia, dotenv, etc.)

### 🚀 Running the Project

1. Install requirements:
    ```
    pip install -r requirements.txt
    ```

2. Add your OpenAI key in a `.env` file:
    ```
    OPENAI_API_KEY=your_key_here
    ```

3. Run the Panel app:
    ```
    panel serve app.py --autoreload --show
    ```

### 📁 Structure

```
ai-multitool-chatbot/
├── app.py
├── tools/
│   ├── weather_tool.py
│   ├── wikipedia_tool.py
│   └── reverse_tool.py
├── utils/
│   └── agent_initializer.py
├── requirements.txt
├── .env
├── README.md
```

Enjoy building your own conversational agent!