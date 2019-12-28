from ..constants import FIRST_SERVICE_GREETING
from ..exceptions.FirstServiceException import FirstServiceException

def greet():
    print(FIRST_SERVICE_GREETING)

def make_trouble():
    raise FirstServiceException()