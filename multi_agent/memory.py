
# memory.py

from typing import Dict, Any, List


class Memory:

    def __init__(self):

        self.memory_store = {}



    def save_context(
        self,
        employee_id: str,
        session_id: str,
        message: Dict[str, Any]
    ):


        if employee_id not in self.memory_store:

            self.memory_store[employee_id] = {}



        if session_id not in self.memory_store[employee_id]:

            self.memory_store[employee_id][session_id] = []



        self.memory_store[employee_id][session_id].append(

            message

        )



    def get_context(
        self,
        employee_id: str,
        session_id: str,
        limit: int = 10
    ) -> List[Dict[str, Any]]:


        history = (

            self.memory_store

            .get(employee_id, {})

            .get(session_id, [])

        )


        return history[-limit:]



    def clear_memory(
        self,
        employee_id: str,
        session_id: str
    ):


        if employee_id in self.memory_store:

            if session_id in self.memory_store[employee_id]:

                del self.memory_store[employee_id][session_id]



    def get_last_message(
        self,
        employee_id: str,
        session_id: str
    ):


        history = self.get_context(

            employee_id,

            session_id

        )


        if history:

            return history[-1]


        return None



memory = Memory()
