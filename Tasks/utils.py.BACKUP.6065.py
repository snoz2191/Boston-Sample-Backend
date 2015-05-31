from .models import Status

# General
STATUS_OK = Status(code="OK",msg="OK")
STATUS_PARAMETERS_INVALID = Status(code="INVALID_PARAMETERS",msg="The format in the request is invalid")

# For user
STATUS_USER_INACTIVE = Status(code="INACTIVE", msg="User is inactive")
STATUS_USER_INVALID = Status(code="INVALID_USER", msg="User is not registered")

# For Task
STATUS_TASK_CREATOR_REQUIRED = Status(code="REQUIRED_PARAMETERS", msg="The creator field is required")
STATUS_TASK_NOT_FOUND = Status(code="TASK_NOT_FOUND", msg="There is no task for the given id")
STATUS_CREATOR_INVALID = Status(code="CREATOR_INVALID", msg="The creator is invalid or doesn't exists")

# For Execution 
STATUS_EXECUTION_NOT_EXISTS = Status(code="NOT_EXISTS", msg="The execution you are requesting doesn\'t exist")
