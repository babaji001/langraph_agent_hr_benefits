
# guardrails.py

from typing import Dict, Any


class Guardrails:

    def __init__(self):

        self.blocked_patterns = [

            "password",

            "secret",

            "credit card",

            "cvv",

            "bank account"

        ]



    def validate_input(
        self,
        request: Dict[str, Any]
    ):


        message = str(

            request.get(

                "question",

                request.get(

                    "message",

                    ""

                )

            )

        ).lower()



        for pattern in self.blocked_patterns:


            if pattern in message:

                return {

                    "allowed": False,

                    "reason":
                        "Sensitive information request blocked"

                }



        return {

            "allowed": True

        }



    def validate_response(
        self,
        response: Dict[str, Any]
    ):


        if response is None:

            return {

                "allowed": False,

                "reason":
                    "Empty response"

            }



        return {

            "allowed": True,

            "response":
                self.sanitize_response(

                    response

                )

        }



    def sanitize_response(
        self,
        response: Dict[str, Any]
    ):


        return {

            key: value

            for key, value in response.items()

            if value is not None

        }



guardrails = Guardrails()
