from ..constants import FIRST_SERVICE_GREETING
from ..exceptions import FirstServiceException

def greet():
    print(FIRST_SERVICE_GREETING)

def make_trouble():
    raise FirstServiceException()