from mcp.server.fastmcp import FastMCP

from services.benefits_service import BenefitsService


mcp = FastMCP(

    "Benefits MCP"

)

service = BenefitsService()

##########################################################
# Benefit Summary
##########################################################

@mcp.tool()

def benefit_summary(

    employee_id: int

):

    """
    Returns employee benefit summary.
    """

    return service.benefit_summary(

        employee_id

    )

##########################################################
# Medical Plan
##########################################################

@mcp.tool()

def medical_plan(

    employee_id: int

):

    """
    Returns employee medical plan.
    """

    return service.medical_plan(

        employee_id

    )

##########################################################
# Dental Plan
##########################################################

@mcp.tool()

def dental_plan(

    employee_id: int

):

    """
    Returns employee dental plan.
    """

    return service.dental_plan(

        employee_id

    )

##########################################################
# Vision Plan
##########################################################

@mcp.tool()

def vision_plan(

    employee_id: int

):

    """
    Returns employee vision plan.
    """

    return service.vision_plan(

        employee_id

    )

##########################################################
# Dependents
##########################################################

@mcp.tool()

def dependents(

    employee_id: int

):

    """
    Returns employee dependents.
    """

    return service.dependents(

        employee_id

    )

##########################################################
# Life Insurance
##########################################################

@mcp.tool()

def life_insurance(

    employee_id: int

):

    """
    Returns employee life insurance details.
    """

    return service.life_insurance(

        employee_id

    )

##########################################################

if __name__ == "__main__":

    mcp.run()
