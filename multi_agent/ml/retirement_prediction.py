
# ml/retirement_prediction.py

import joblib


class RetirementPrediction:

    def __init__(self):

        self.model_path = (
            "ml/models/retirement_prediction_model.py"
        )

        self.model = None

        self.load_model()



    def load_model(self):

        self.model = joblib.load(

            self.model_path

        )



    def predict(
        self,
        features
    ):

        prediction = self.model.predict(

            [features]

        )


        return {

            "model":

                "retirement_prediction",

            "prediction":

                prediction[0]

        }
