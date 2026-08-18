from enum import Enum


############################################################
# Roles
############################################################

class Role(Enum):

    EMPLOYEE = "EMPLOYEE"

    MANAGER = "MANAGER"

    HR = "HR"

    PAYROLL = "PAYROLL"

    BENEFITS = "BENEFITS"

    ADMIN = "ADMIN"


############################################################
# Access Matrix
############################################################

PERMISSIONS = {

    Role.EMPLOYEE: [

        "EmployeeAgent",

        "LeaveAgent",

        "BenefitsAgent",

        "ClaimsAgent",

        "RetirementAgent",

        "PolicyAgent"

    ],

    Role.MANAGER: [

        "EmployeeAgent",

        "LeaveAgent",

        "BenefitsAgent",

        "ClaimsAgent",

        "RetirementAgent",

        "PolicyAgent",

        "ManagerApproval"

    ],

    Role.HR: [

        "EmployeeAgent",

        "LeaveAgent",

        "BenefitsAgent",

        "ClaimsAgent",

        "RetirementAgent",

        "PolicyAgent",

        "HRAgent"

    ],

    Role.PAYROLL: [

        "PayrollAgent"

    ],

    Role.BENEFITS: [

        "BenefitsAgent",

        "ClaimsAgent"

    ],

    Role.ADMIN: [

        "*"

    ]

}


############################################################

class AccessControl:

    def has_access(

        self,

        role,

        resource

    ):

        permissions = PERMISSIONS.get(role, [])

        if "*" in permissions:

            return True

        return resource in permissions


############################################################

access_control = AccessControl()
