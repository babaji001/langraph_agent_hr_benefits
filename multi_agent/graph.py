# graph.py

from typing import TypedDict, Any, Dict, List

from langgraph.graph import StateGraph, END

from guardrails import guardrails
from memory import memory
from router import router
from supervisor import supervisor

from audit_logger import audit_logger
from metrics import metrics


###############################################################
# LangGraph State
###############################################################

class HRState(TypedDict, total=False):

    employee_id: str

    session_id: str

    question: str

    route: Dict[str, Any]

    response: Dict[str, Any]

    history: List[Dict[str, Any]]

    stop: bool



###############################################################
# Guardrails Node
###############################################################

def guardrail_node(
    state: HRState
):

    validation = guardrails.validate_input(

        state

    )


    if not validation["allowed"]:

        state["response"] = {

            "error":

                validation["reason"]

        }

        state["stop"] = True


    return state



###############################################################
# Memory Node
###############################################################

def memory_node(
    state: HRState
):

    employee_id = state.get(

        "employee_id"

    )


    session_id = state.get(

        "session_id",

        "default"

    )


    memory.save_context(

        employee_id,

        session_id,

        {

            "role":

                "user",

            "content":

                state.get(

                    "question",

                    ""

                )

        }

    )


    state["history"] = memory.get_context(

        employee_id,

        session_id

    )


    return state



###############################################################
# Router Node
###############################################################

def router_node(
    state: HRState
):

    route = router.route(

        state.get(

            "question",

            ""

        )

    )


    state["route"] = route


    audit_logger.log_request(

        state.get(

            "employee_id"

        ),

        state.get(

            "question"

        ),

        route

    )


    return state



###############################################################
# Supervisor Node
###############################################################

def supervisor_node(
    state: HRState
):

    response = supervisor.process(

        state

    )


    state["response"] = response


    return state



###############################################################
# Response Node
###############################################################

def response_node(
    state: HRState
):

    validation = guardrails.validate_response(

        state.get(

            "response"

        )

    )


    state["response"] = validation


    memory.save_context(

        state.get(

            "employee_id"

        ),

        state.get(

            "session_id",

            "default"

        ),

        {

            "role":

                "assistant",

            "content":

                validation

        }

    )


    audit_logger.log_response(

        state.get(

            "employee_id"

        ),

        validation

    )


    metrics.record_request()


    return state



###############################################################
# Build Graph
###############################################################

workflow = StateGraph(

    HRState

)



workflow.add_node(

    "guardrails",

    guardrail_node

)


workflow.add_node(

    "memory",

    memory_node

)


workflow.add_node(

    "router",

    router_node

)


workflow.add_node(

    "supervisor",

    supervisor_node

)


workflow.add_node(

    "response",

    response_node

)



workflow.set_entry_point(

    "guardrails"

)


workflow.add_edge(

    "guardrails",

    "memory"

)


workflow.add_edge(

    "memory",

    "router"

)


workflow.add_edge(

    "router",

    "supervisor"

)


workflow.add_edge(

    "supervisor",

    "response"

)


workflow.add_edge(

    "response",

    END

)



graph = workflow.compile()
