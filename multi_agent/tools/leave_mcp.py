from mcp.server.fastmcp import FastMCP

from services.leave_service import LeaveService


mcp = FastMCP(

    "Leave MCP"

)

service = LeaveService()

##########################################################
# Leave Balance
##########################################################

@mcp.tool()

def leave_balance(

    employee_id: int

):

    """
    Returns employee leave balance.
    """

    return service.leave_balance(

        employee_id

    )

##########################################################
# Leave History
##########################################################

@mcp.tool()

def leave_history(

    employee_id: int

):

    """
    Returns employee leave history.
    """

    return service.leave_history(

        employee_id

    )

##########################################################
# Leave Status
##########################################################

@mcp.tool()

def leave_status(

    employee_id: int,

    request_id: int

):

    """
    Returns leave request status.
    """

    return service.leave_status(

        employee_id,

        request_id

    )

##########################################################
# Apply Leave
##########################################################

@mcp.tool()

def apply_leave(

    employee_id: int,

    leave_type: str,

    start_date: str,

    end_date: str,

    reason: str

):

    """
    Creates a leave request.
    """

    return service.apply_leave(

        employee_id,

        leave_type,

        start_date,

        end_date,

        reason

    )

##########################################################
# Cancel Leave
##########################################################

@mcp.tool()

def cancel_leave(

    employee_id: int,

    request_id: int

):

    """
    Cancels a leave request.
    """

    return service.cancel_leave(

        employee_id,

        request_id

    )

##########################################################

if __name__ == "__main__":

    mcp.run()
