```python id="8m3kq1"
# ml/fraud_detection.py


class FraudDetection:

    def __init__(self):

        self.model_name = "fraud_detection"

        self.model = None



    def load_model(
        self,
        model_path
    ):

        self.model = model_path



    def predict(
        self,
        features
    ):

        if self.model is None:

            raise NotImplementedError(
                "Fraud detection model is not implemented"
            )


        prediction = self.model.predict(

            [features]

        )


        return {

            "model":

                self.model_name,

            "prediction":

                prediction[0]

        }
```
