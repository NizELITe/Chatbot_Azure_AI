import os
from pathlib import Path
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

# ✅ Set environment variables for your Azure AI Foundry project
os.environ["PROJECT_ENDPOINT"] = ""
os.environ["MODEL_DEPLOYMENT_NAME"] = "gpt-4.1"  # we'll test this first without tools

# ✅ Get the endpoint from environment variable
project_endpoint = os.environ["PROJECT_ENDPOINT"]

# ✅ Create AIProjectClient instance
project_client = AIProjectClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential(),
)

with project_client:
    # ✅ Create an agent (no Code Interpreter for now)
    agent = project_client.agents.create_agent(
        model=os.environ["MODEL_DEPLOYMENT_NAME"],
        name="nizam_agent",
        instructions="You politely help with math and data visualization explanations.",
    )
    print(f"✅ Created agent with ID: {agent.id}")

    # ✅ Create a communication thread
    thread = project_client.agents.threads.create()
    print(f"✅ Created thread with ID: {thread.id}")

    # ✅ Send user message
    message = project_client.agents.messages.create(
        thread_id=thread.id,
        role="user",
        content="Hey agent! Can you explain how to plot a line with slope 4 and intercept 9?",
    )
    print(f"✅ Created message with ID: {message.id}")

    # ✅ Process the run
    run = project_client.agents.runs.create_and_process(
        thread_id=thread.id,
        agent_id=agent.id,
        additional_instructions="Address the user as Nizam.",
    )
    print(f"✅ Run finished with status: {run.status}")

    # If run failed, show error
    if run.status == "failed":
        print(f"❌ Run failed: {run.last_error}")

    # ✅ Retrieve and print messages
    messages = project_client.agents.messages.list(thread_id=thread.id)
    print("\n📩 Agent Responses:")
    for msg in messages:
        print(f"{msg.role}: {msg.content}")

    # ✅ Delete the agent after run
    project_client.agents.delete_agent(agent.id)
    print("🗑️ Agent deleted successfully.")
