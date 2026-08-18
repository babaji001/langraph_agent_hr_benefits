
# ml/ml_router.py

from ml.leave_prediction import LeavePrediction
from ml.retirement_prediction import RetirementPrediction
from ml.fraud_detection import FraudDetection


class MLRouter:

    def __init__(self):

        self.leave_model = LeavePrediction()

        self.retirement_model = RetirementPrediction()

        self.fraud_model = FraudDetection()



    def predict(
        self,
        intent,
        request
    ):


        if intent == "leave_prediction":

            return self.leave_model.predict(

                request

            )



        elif intent == "retirement_prediction":

            return self.retirement_model.predict(

                request

            )



        elif intent == "fraud_detection":

            return self.fraud_model.predict(

                request

            )



        return {

            "message":

                "No ML model required"

        }



ml_router = MLRouter()
