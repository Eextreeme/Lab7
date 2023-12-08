import logging
import math
import lab_5_copy 
def logged(exception, logging_type):
    def outer(func):
        def inner(*args, **kwargs):
            if logging_type == "file" :
                logging.basicConfig(
                    filename="logs.txt",
                    level=logging.DEBUG,)
            else:
                logging.basicConfig(level=logging.DEBUG)
            try:
                func(*args, **kwargs)
            except exception:
                logging.exception(exception)
            except Exception:
                logging.error("Unexpected Exceptions was made")
        return inner
    return outer
class TooStrong(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Your opponen has higher attack on {self.value} points"

class Fight(lab_5_copy.Fight):
    @logged(TooStrong, 'console')
    def fighter_atack(self):
        if math.fabs(self.__fighter1.get_atack() - self.__fighter2.get_atack()) > 40:
            raise print(TooStrong)
        
    