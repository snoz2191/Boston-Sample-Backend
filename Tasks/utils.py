from .models import Status

# General
STATUS_OK = Status(code="OK",msg="OK")
STATUS_PARAMETERS_INVALID = Status(code="INVALID_PARAMETERS",msg="The format in the request is invalid")

# For user
STATUS_USER_INACTIVE = Status(code="INACTIVE", msg="User is inactive")
STATUS_USER_INVALID = Status(code="INVALID_USER", msg="User is not registered")