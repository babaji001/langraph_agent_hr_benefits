
# response_builder.py

from typing import List, Dict, Any


class ResponseBuilder:


    def __init__(self):

        pass



    def build(
        self,
        responses: List[Dict[str, Any]]
    ):


        if not responses:

            return {

                "message":
                    "No response generated",

                "status":
                    "EMPTY"

            }



        final_response = {


            "status":
                "SUCCESS",


            "agents":
                [],


            "results":
                []

        }



        for response in responses:


            final_response["agents"].append(

                response.get(
                    "agent"
                )

            )


            final_response["results"].append(

                {

                    "intent":
                        response.get(
                            "intent"
                        ),

                    "data":
                        response.get(
                            "data"
                        )

                }

            )



        return final_response



response_builder = ResponseBuilder()
