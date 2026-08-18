
# audit_logger.py

import logging
import json
from datetime import datetime


class AuditLogger:

    def __init__(self):

        logging.basicConfig(

            filename="audit.log",

            level=logging.INFO,

            format="%(asctime)s %(levelname)s %(message)s"

        )

        self.logger = logging.getLogger(
            "HR_AI_AUDIT"
        )



    def log_request(
        self,
        employee_id,
        question,
        route
    ):

        event = {

            "timestamp":
                datetime.utcnow().isoformat(),

            "employee_id":
                employee_id,

            "question":
                question,

            "route":
                route

        }


        self.logger.info(

            json.dumps(event)

        )



    def log_response(
        self,
        employee_id,
        response
    ):

        event = {

            "timestamp":
                datetime.utcnow().isoformat(),

            "employee_id":
                employee_id,

            "response":
                response

        }


        self.logger.info(

            json.dumps(event)

        )



    def log_error(
        self,
        employee_id,
        error
    ):

        event = {

            "timestamp":
                datetime.utcnow().isoformat(),

            "employee_id":
                employee_id,

            "error":
                str(error)

        }


        self.logger.error(

            json.dumps(event)

        )



audit_logger = AuditLogger()
