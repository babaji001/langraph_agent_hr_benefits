
# router.py

import json

from config import llm
from prompts import ROUTER_PROMPT


VALID_AGENTS = {

    "employee",
    "leave",
    "benefits",
    "payroll",
    "claims",
    "retirement",
    "policy",
    "hr"

}


class Router:

    def __init__(self):

        pass


    def route(
        self,
        question
    ):


        prompt = f"""
{ROUTER_PROMPT}

Employee Question:
{question}

Return ONLY valid JSON.
"""


        response = llm.invoke(
            prompt
        ).content


        try:

            route = json.loads(
                response
            )


        except Exception:

            route = {

                "intent": "unknown",

                "agents": [

                    "hr"

                ],

                "ml": False,

                "hr": True

            }


        route["agents"] = [

            agent

            for agent in route.get(
                "agents",
                []
            )

            if agent in VALID_AGENTS

        ]


        if not route["agents"]:

            route["agents"] = [

                "hr"

            ]


        return route



router = Router()
