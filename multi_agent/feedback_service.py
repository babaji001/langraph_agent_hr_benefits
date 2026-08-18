
# feedback_service.py

from datetime import datetime


class FeedbackService:

    def __init__(self):

        self.feedback_store = []



    def capture_feedback(
        self,
        employee_id,
        response_id,
        rating,
        comments=None
    ):


        feedback = {

            "employee_id":
                employee_id,

            "response_id":
                response_id,

            "rating":
                rating,

            "comments":
                comments,

            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.feedback_store.append(

            feedback

        )


        return {

            "status":
                "RECORDED",

            "feedback":
                feedback

        }



    def get_feedback(
        self,
        employee_id=None
    ):


        if employee_id:

            return [

                item

                for item in self.feedback_store

                if item["employee_id"] == employee_id

            ]


        return self.feedback_store



feedback_service = FeedbackService()
