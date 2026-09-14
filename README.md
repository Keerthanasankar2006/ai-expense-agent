# 💰 AI Expense Agent

An AI-powered expense management assistant built using Python, Groq LLM, Function Calling, FastAPI, SQLite, and HTML/CSS/JavaScript.

The agent can understand expense-related requests, select the appropriate tool, validate expense data, store expenses in SQLite, and return a useful response to the user.

---

## 🚀 Features

- 🤖 Groq LLM integration
- 🔧 AI Function Calling
- 🔄 Agent Tool-Calling Loop
- 💾 SQLite database
- ✅ Expense validation
- 🛡️ Tool error handling
- 🔁 Retry and timeout concepts
- ⚡ FastAPI backend
- 🌐 HTML/CSS/JavaScript frontend
- 📊 Expense listing and total calculation
- 🔐 Environment variable support for API keys

---

## 🏗️ Architecture

```text
                    User
                      │
                      ▼
                 Frontend
              HTML/CSS/JavaScript
                      │
                      ▼
                  FastAPI
                      │
                      ▼
                 AI Agent
                      │
                      ▼
                  Groq LLM
                      │
                Function Calling
                      │
                      ▼
                   Tools
                 /       \
                /         \
       Validation       Database
           │               │
           ▼               ▼
       Valid Data        SQLite
