
# notification_service.py

from datetime import datetime


class NotificationService:

    def __init__(self):

        self.notifications = []



    def send(
        self,
        employee_id,
        message,
        notification_type="INFO"
    ):


        notification = {

            "employee_id":
                employee_id,

            "type":
                notification_type,

            "message":
                message,

            "timestamp":
                datetime.utcnow().isoformat()

        }


        self.notifications.append(

            notification

        )


        return {

            "status":
                "SENT",

            "notification":
                notification

        }



    def get_notifications(
        self,
        employee_id
    ):


        return [

            notification

            for notification in self.notifications

            if notification["employee_id"] == employee_id

        ]



notification_service = NotificationService()
