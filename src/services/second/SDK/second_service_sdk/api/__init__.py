from ..constants import SECOND_SERVICE_GREETING
from ..exceptions import SecondServiceException

def greet():
    print(SECOND_SERVICE_GREETING)

def make_trouble():
    raise SecondServiceException()