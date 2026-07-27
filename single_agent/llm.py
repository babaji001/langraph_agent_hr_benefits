from langchain_ollama import ChatOllama

from prompt import SYSTEM_PROMPT

from tools import *

llm = ChatOllama(

    model="qwen2.5:3b",

    temperature=0

)

llm_with_tools = llm.bind_tools(

[
employee_tool,
leave_balance_tool,
leave_history_tool,
payroll_tool,
benefits_tool,
claims_tool,
dependents_tool,
policy_tool
]

)

def invoke_llm(messages):

    messages = [SYSTEM_PROMPT] + messages

    return llm_with_tools.invoke(messages)
