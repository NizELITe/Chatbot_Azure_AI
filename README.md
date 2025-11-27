

---

# 🚀 Azure Chatbot – Python Examples Using Azure OpenAI & Azure AI Foundry

This repository contains **three different Python scripts**, each demonstrating a different way to interact with Azure OpenAI and Azure AI Foundry.
These examples cover:

* Basic chat completions
* Creating agents
* Working with threads, messages, and runs
* Using Azure AI Foundry project endpoints

---

# 📁 Project Structure

```
📦 Chatbot_Azure_AI
 ├── Chatfile.py
 ├── AgenticAI.py
 ├── AgenticAI2.py
 └── README.md
```

Each Python file represents a **different method** of interacting with Azure AI.

---

# 1️⃣ Basic Azure OpenAI Chat Completion (Chatfile.py)

This script shows the **simplest API call** to Azure OpenAI using the `AzureOpenAI` client.

### 🔹 What it does

* Connects to your Azure OpenAI model (gpt-4.1-mini)
* Sends a chat message (“I am going to Paris, what should I see?”)
* Prints the assistant’s reply

### 🔹 Example usage

```python
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=subscription_key,
    azure_endpoint=endpoint,
    api_version="2024-12-01-preview",
)

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "I am going to Paris, what should I see?"}
    ]
)

print(response.choices[0].message.content)
```

This file is best for learning **how to send a direct prompt** without agents.

---

# 2️⃣ Azure AI Foundry – Agent Creation + Thread + Run (AgenticAI.py)

This script shows how to use the **AIProjectClient** to:

* Create an agent
* Create a thread
* Send messages
* Process the run
* Retrieve responses
* Delete the agent when done

### 🔹 What it does

* Creates a model-driven agent with instructions
* Sends a message asking how to plot a line
* Processes the conversation
* Prints all assistant responses

### 🔹 Key features

* Uses environment variables
* Uses `DefaultAzureCredential()` for authentication
* Fully managed agent workflow

---

# 3️⃣ Azure AI Foundry – Simple Agent Example (AgenticAI2.py)

This is a **lighter**, simpler version of demo #2.

### 🔹 What it does

* Creates an agent
* Starts a conversation thread
* Sends a user message (“Write a poem about AI and nature.”)
* Retrieves the assistant’s generated poem
* Deletes the agent afterward

### 🔹 Highlights

```python
agent = project.agents.create_agent(
    model="gpt-4.1-mini",
    name="my-agent",
    instructions="You are a helpful AI assistant."
)
```

This file is good if you want a **minimal clean example**.

---

# 🧩 When to Use Which File?

| File                | Purpose                                       | Difficulty       |
| ------------------- | --------------------------------------------- | ---------------- |
| **Chatfile.py**     | Basic chat API call                           | ⭐ Easy           |
| *AgenticAI.py** | Full agent workflow (threads, runs, messages) | ⭐⭐⭐ Intermediate |
| **AgenticAI2.py** | Simple agent example                          | ⭐⭐ Medium        |

---

# 🔐 Environment Variables (Important)

Make sure you set the following in your system or `.env` file (do NOT push `.env` to GitHub):

```
PROJECT_ENDPOINT=
MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
AZURE_CLIENT_ID=
AZURE_TENANT_ID=
AZURE_CLIENT_SECRET=
```

---

# 📌 Requirements

Install dependencies:

```bash
pip install openai azure-ai-projects azure-identity
```

You must also be logged into Azure:

```bash
az login
```



Just tell me, Ahmed bro — I’ll hook you up.
