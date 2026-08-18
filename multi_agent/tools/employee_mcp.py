from mcp.server.fastmcp import FastMCP

from services.employee_service import EmployeeService


mcp = FastMCP(

    "Employee MCP"

)

service = EmployeeService()

##########################################################
# Employee Profile
##########################################################

@mcp.tool()

def employee_profile(

    employee_id: int

):

    """
    Returns the employee profile including
    employee id, name, title, department,
    email, location and manager.
    """

    return service.employee_profile(

        employee_id

    )

##########################################################
# Manager
##########################################################

@mcp.tool()

def manager(

    employee_id: int

):

    """
    Returns the employee's reporting manager.
    """

    return service.manager(

        employee_id

    )

##########################################################
# Department
##########################################################

@mcp.tool()

def department(

    employee_id: int

):

    """
    Returns employee department.
    """

    return service.department(

        employee_id

    )

##########################################################
# Job Title
##########################################################

@mcp.tool()

def job_title(

    employee_id: int

):

    """
    Returns employee job title.
    """

    return service.job_title(

        employee_id

    )

##########################################################
# Location
##########################################################

@mcp.tool()

def location(

    employee_id: int

):

    """
    Returns employee work location.
    """

    return service.location(

        employee_id

    )

##########################################################
# Organization
##########################################################

@mcp.tool()

def organization(

    employee_id: int

):

    """
    Returns employee organization hierarchy.
    """

    return service.organization(

        employee_id

    )

##########################################################

if __name__ == "__main__":

    mcp.run()
