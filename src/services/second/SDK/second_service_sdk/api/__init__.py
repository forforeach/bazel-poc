from ..constants import SECOND_SERVICE_GREETING
from ..exceptions.SecondServiceException import SecondServiceException

def greet():
    print(SECOND_SERVICE_GREETING)

def make_trouble():
    raise SecondServiceException()