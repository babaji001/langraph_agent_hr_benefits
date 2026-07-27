import requests

from langchain_core.tools import tool

from rag import search_policy

BASE_URL = "http://127.0.0.1:8000"

###########################################################
# Employee Tool
###########################################################

@tool
def employee_tool(emp_id: int):
    """
       EMPLOYEE TOOL (employee_tool)

       Use this tool whenever the user asks about EMPLOYEE PROFILE information.

       Examples:

       - Employee information
       - Employee profile
       - My profile
       - My manager
       - Manager name
       - Department
       - Team
       - Work location
       - Office location
       - Email address
       - Hire date
       - Employment information
       - Job details

       IMPORTANT:

       This tool retrieves employee-specific information.

       Employee ID is REQUIRED.

       DO NOT use this tool for:

       - Leave Policy
       - Benefits Policy
       - Payroll
       - Claims
       - Company Policies
       """

    return requests.get(
        f"{BASE_URL}/employee/{emp_id}"
    ).json()


###########################################################
# Leave Balance
###########################################################

@tool
def leave_balance_tool(emp_id: int):
    """
        LEAVE BALANCE TOOL (leave_balance_tool)

        Use this tool whenever the user asks about THEIR PERSONAL leave balance.

        Examples:

        - My leave balance
        - PTO balance
        - Remaining PTO
        - Vacation balance
        - Sick leave balance
        - Floating holidays
        - Personal leave
        - Remaining vacation
        - Available leave
        - Leave credits

        IMPORTANT:

        This tool returns employee-specific leave balances.

        Employee ID is REQUIRED.

        DO NOT use this tool for:

        - Leave Policy
        - FMLA Policy
        - Manager Approval
        - Leave Rules
        - Carry Forward Policy
        """

    return requests.get(
        f"{BASE_URL}/leave/{emp_id}"
    ).json()


###########################################################
# Leave History
###########################################################

@tool
def leave_history_tool(emp_id: int):
    """
       LEAVE HISTORY TOOL (leave_history_tool)

       Use this tool whenever the user asks about previous leave requests.

       Examples:

       - Leave history
       - Vacation history
       - Sick leave history
       - Previous leave
       - Approved leave
       - Pending leave
       - Rejected leave
       - Leave requests
       - Past vacations

       IMPORTANT:

       Employee ID is REQUIRED.

       Do NOT use for company leave policy.
       """

    return requests.get(
        f"{BASE_URL}/leave/history/{emp_id}"
    ).json()


###########################################################
# Payroll
###########################################################

@tool
def payroll_tool(emp_id: int):
    """
     PAYROLL TOOL (payroll_tool)

     Use this tool whenever the user asks about payroll information.

     Examples:

     - Salary
     - Payroll
     - Net Pay
     - Gross Pay
     - Compensation
     - Bonus
     - Incentives
     - Taxes
     - Tax deductions
     - Pay Stub
     - Last paycheck
     - Payroll deductions

     IMPORTANT:

     Payroll information is employee-specific.

     Employee ID is REQUIRED.

     DO NOT use for Benefits or HR Policies.
     """

    return requests.get(
        f"{BASE_URL}/payroll/{emp_id}"
    ).json()


###########################################################
# Benefits
###########################################################

@tool
def benefits_tool(emp_id: int):
    """
       BENEFITS TOOL (benefits_tool)

       Use this tool whenever the user asks about THEIR enrolled benefits.

       Examples:

       - My benefits
       - My medical plan
       - Dental coverage
       - Vision coverage
       - Life insurance
       - STD coverage
       - LTD coverage
       - HSA
       - FSA
       - Retirement plan
       - 401K enrollment
       - Benefit enrollment

       IMPORTANT:

       This tool returns employee-specific enrolled benefits.

       Employee ID is REQUIRED.

       DO NOT use for:

       - Benefits Policy
       - Open Enrollment Policy
       - COBRA Policy
       - Medical Plan rules

       Use policy_tool for company benefit policies.
       """

    return requests.get(
        f"{BASE_URL}/benefits/{emp_id}"
    ).json()


###########################################################
# Claims
###########################################################

@tool
def claims_tool(emp_id: int):
    """
        CLAIMS TOOL (claims_tool)

        Use this tool whenever the user asks about insurance claims.

        Examples:

        - Medical claim
        - Dental claim
        - Vision claim
        - Claim status
        - Pending claims
        - Approved claims
        - Rejected claims
        - Claim amount
        - Claims history
        - Healthcare claims

        IMPORTANT:

        Employee ID is REQUIRED.

        This tool retrieves employee-specific claims.

        DO NOT use for benefits policy.
        """

    return requests.get(
        f"{BASE_URL}/claims/{emp_id}"
    ).json()


###########################################################
# Dependents
###########################################################

@tool
def dependents_tool(emp_id: int):
    """
       DEPENDENTS TOOL (dependents_tool)

       Use this tool whenever the user asks about covered family members.

       Examples:

       - My dependents
       - Covered spouse
       - Covered children
       - Family coverage
       - Dependents
       - Spouse coverage
       - Child coverage

       IMPORTANT:

       Employee ID is REQUIRED.

       Returns employee-specific dependent information.
       """

    return requests.get(
        f"{BASE_URL}/dependents/{emp_id}"
    ).json()


###########################################################
# HR Policy (RAG)
###########################################################

@tool
def policy_tool(question: str):
    """
    POLICY TOOL (policy_tool)

        Use this tool whenever the user asks about COMPANY POLICIES,
        BENEFITS POLICIES, HR RULES, or EMPLOYEE HANDBOOK information.

        Examples:

        LEAVE POLICIES

        - FMLA
        - Leave Policy
        - Vacation Policy
        - Sick Leave Policy
        - Maternity Leave
        - Paternity Leave
        - Adoption Leave
        - Bereavement Leave
        - Military Leave
        - Jury Duty
        - Leave Carry Forward
        - Leave Eligibility
        - Leave Approval Rules
        - Manager Approval
        - HR Approval
        - Approval Workflow

        BENEFITS POLICIES

        - Medical Plans
        - Dental Plans
        - Vision Plans
        - Life Insurance
        - Short Term Disability
        - Long Term Disability
        - HSA
        - FSA
        - 401K
        - Retirement Benefits
        - COBRA
        - Open Enrollment
        - Wellness Program
        - Employee Assistance Program
        - Tuition Reimbursement

        HR POLICIES

        - Employee Handbook
        - HR Policies
        - Company Policies
        - Code of Conduct
        - Ethics
        - Confidentiality
        - Security Policies
        - Travel Policy
        - Expense Policy

        IMPORTANT:

        Policy questions are COMPANY-WIDE.

        DO NOT ask for Employee ID.

        ALWAYS use policy_tool for policy questions.

        Never answer policy questions using your own knowledge.

        Always search the enterprise knowledge base first.
       """

    return search_policy(question)
