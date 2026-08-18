
# supervisor.py

from agents.employee_agent import EmployeeAgent
from agents.leave_agent import LeaveAgent
from agents.benefits_agent import BenefitsAgent
from agents.payroll_agent import PayrollAgent
from agents.claims_agent import ClaimsAgent
from agents.retirement_agent import RetirementAgent
from agents.policy_agent import PolicyAgent
from agents.hr_agent import HRAgent

from response_builder import ResponseBuilder


class Supervisor:

    def __init__(self):

        self.agent_map = {

            "employee": EmployeeAgent(),

            "leave": LeaveAgent(),

            "benefits": BenefitsAgent(),

            "payroll": PayrollAgent(),

            "claims": ClaimsAgent(),

            "retirement": RetirementAgent(),

            "policy": PolicyAgent(),

            "hr": HRAgent()

        }


        self.response_builder = ResponseBuilder()



    def invoke_agent(
        self,
        agent_name,
        question,
        employee_id
    ):


        agent = self.agent_map.get(
            agent_name
        )


        if not agent:

            return None


        return agent.process(

            question,

            employee_id

        )



    def process(
        self,
        state
    ):


        responses = []


        question = state.get(
            "question"
        )


        employee_id = state.get(
            "employee_id"
        )


        route = state.get(
            "route",
            {}
        )


        for agent_name in route.get(
            "agents",
            []
        ):


            response = self.invoke_agent(

                agent_name,

                question,

                employee_id

            )


            if response:

                responses.append(
                    response
                )


        return self.response_builder.build(

            responses

        )



supervisor = Supervisor()
