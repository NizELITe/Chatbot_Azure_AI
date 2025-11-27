from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import ListSortOrder

# Initialize project client using your Azure AI Foundry project endpoint
project = AIProjectClient(
    endpoint="",
    credential=DefaultAzureCredential(),
)

# --- Create Agent ---
agent = project.agents.create_agent(
    model="gpt-4.1-mini",
    name="my-agent",
    instructions="You are a helpful AI assistant."
)

# --- Create a conversation thread ---
thread = project.agents.threads.create()

# --- Add a user message ---
project.agents.messages.create(
    thread_id=thread.id,
    role="user",
    content="Write a short poem about AI and nature."
)

# --- Process the conversation ---
run = project.agents.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)

if run.status == "failed":
    print(f"Run failed: {run.last_error}")

# --- Retrieve and print responses ---
messages = project.agents.messages.list(thread_id=thread.id, order=ListSortOrder.ASCENDING)
for message in messages:
    if message.role == "assistant" and message.text_messages:
        print("Assistant:", message.text_messages[-1].text.value)

# --- Cleanup: delete the agent ---
project.agents.delete_agent(agent.id)
print("Agent deleted successfully.")
