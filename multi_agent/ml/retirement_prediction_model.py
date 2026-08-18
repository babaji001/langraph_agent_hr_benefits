"""
Retirement Prediction ML Model

Simple regression-based retirement forecast model.

Input:
- Current retirement balance
- Monthly contribution
- Years

Output:
- Future retirement value
"""


from sklearn.linear_model import LinearRegression
import numpy as np



class RetirementPredictionModel:


    def __init__(self):

        self.model = LinearRegression()

        self._train()



    def _train(self):

        # Sample training data
        #
        # Features:
        # current_balance,
        # monthly_contribution,
        # years


        X = np.array([

            [50000, 500, 10],
            [100000, 800, 15],
            [150000, 1000, 20],
            [200000, 1500, 25],
            [300000, 2000, 30]

        ])


        # Future retirement values

        y = np.array([

            180000,
            350000,
            600000,
            950000,
            1500000

        ])


        self.model.fit(
            X,
            y
        )



    def predict(
            self,
            current_balance: float,
            monthly_contribution: float,
            years: int
    ):


        prediction = self.model.predict(

            [[

                current_balance,

                monthly_contribution,

                years

            ]]

        )


        return {

            "current_balance":
                current_balance,

            "monthly_contribution":
                monthly_contribution,

            "years":
                years,

            "predicted_retirement_value":
                round(
                    prediction[0],
                    2
                )

        }



retirement_model = RetirementPredictionModel()
