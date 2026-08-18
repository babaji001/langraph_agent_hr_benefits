
# metrics.py

from datetime import datetime
from collections import defaultdict


class Metrics:

    def __init__(self):

        self.request_count = 0

        self.agent_usage = defaultdict(int)

        self.error_count = 0

        self.response_times = []



    def record_request(
        self
    ):

        self.request_count += 1



    def record_agent_usage(
        self,
        agent_name
    ):

        self.agent_usage[agent_name] += 1



    def record_error(
        self
    ):

        self.error_count += 1



    def record_response_time(
        self,
        duration
    ):

        self.response_times.append(
            duration
        )



    def get_metrics(
        self
    ):


        average_response_time = 0


        if self.response_times:

            average_response_time = (

                sum(self.response_times)

                /

                len(self.response_times)

            )


        return {

            "timestamp":
                datetime.utcnow().isoformat(),

            "total_requests":
                self.request_count,

            "agent_usage":
                dict(self.agent_usage),

            "errors":
                self.error_count,

            "average_response_time":
                average_response_time

        }



metrics = Metrics()
