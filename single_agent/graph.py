from typing import TypedDict, Annotated

from langgraph.graph import StateGraph, END

from langgraph.graph.message import add_messages

from langchain_core.messages import ToolMessage

from llm import invoke_llm

from tools import (
    employee_tool,
    leave_balance_tool,
    leave_history_tool,
    payroll_tool,
    benefits_tool,
    claims_tool,
    dependents_tool,
    policy_tool,
)

#########################################################
# State
#########################################################

class AgentState(TypedDict):

    messages: Annotated[list, add_messages]
# LLM Node
def llm_node(state):

    response = invoke_llm(state["messages"])

    return {

        "messages":[response]

    }
# Tool Node
tool_map = {

    "employee_tool": employee_tool,

    "leave_balance_tool": leave_balance_tool,

    "leave_history_tool": leave_history_tool,

    "payroll_tool": payroll_tool,

    "benefits_tool": benefits_tool,

    "claims_tool": claims_tool,

    "dependents_tool": dependents_tool,

    "policy_tool": policy_tool

}

def tool_node(state):

    last_message = state["messages"][-1]

    tool_messages = []

    for tool_call in last_message.tool_calls:

        tool = tool_map[tool_call["name"]]

        result = tool.invoke(tool_call["args"])

        tool_messages.append(

            ToolMessage(

                content=str(result),

                tool_call_id=tool_call["id"]

            )

        )

    return {

        "messages": tool_messages

    }
#router
def should_continue(state):

    last_message = state["messages"][-1]

    if hasattr(last_message, "tool_calls"):

        if len(last_message.tool_calls) > 0:

            return "tools"

    return END
#graph

builder = StateGraph(AgentState)

builder.add_node("llm", llm_node)

builder.add_node("tools", tool_node)

builder.set_entry_point("llm")

builder.add_conditional_edges(

    "llm",

    should_continue,

    {

        "tools":"tools",

        END:END

    }

)

builder.add_edge("tools","llm")

graph = builder.compile()
