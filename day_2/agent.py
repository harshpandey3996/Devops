from langchain_ollama import ChatOllama
from devops_tools import read_log_file, count_log_levels ,show_docker_containers
from langchain_core.tools import tool
from langchain.agents import create_agent

# LLM
llm = ChatOllama(
    model="qwen2.5:7b",
    base_url="http://localhost:11434",
    temperature=0
)

# Tools
@tool
def analyze_logs(path):
    """
    This tool counts the log levels INFO, WARNING, ERROR from a given file path.
    """
    return count_log_levels(read_log_file(path))

@tool
def get_docker_containers():
    """
    This tool internally runs docker command via subprocess and gets the running and exited containers information  
    """

    return show_docker_containers()


# LLM + Tools = AI Agent
TOOLS = [analyze_logs,get_docker_containers]

SYSTEM_PROMPT = """
You are a Log Analysis Agent for DevOps engineers.
Always use the analyze_logs tool and Analyze the Docker Containers runings locally using `get_docker_containers` to get exact counts, never guess.
State the INFO/WARNING/ERROR counts, then give a one or two line summary.
Suggest ideas only, never perform production actions.
"""

agent = create_agent(
    llm,
    tools=TOOLS,
    system_prompt=SYSTEM_PROMPT
)

question = input("Enter your question for DevOps Agent: ")

result = agent.invoke({
    "messages": [("user", question)]
})

print("\nThinking...\n")

# The last message is the agent's final answer
print(result["messages"][-1].content)