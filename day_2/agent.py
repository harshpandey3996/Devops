from langchain_ollama import ChatOllama
from devops_tools import read_log_file, count_log_levels
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


# LLM + Tools = AI Agent
TOOLS = [analyze_logs]

SYSTEM_PROMPT = """
You are a Log Analysis Agent for DevOps engineers.
Always use the analyze_logs tool to get exact counts, never guess.
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