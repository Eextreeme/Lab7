import logging
import math
import lab_5_copy 
def logged(exception, logging_type):
    def outer(func):
        def inner(*args, **kwargs):
            if logging_type == "file" :
                logging.basicConfig(
                    filename="/Users/prabwa/Politech/lab_7/Lab7/logs.txt",
                    level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                    )
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
    @logged(TooStrong, 'file')
    def fighter_attack(self, max_differanace_in_attack):
        if int(math.fabs(self.__fighter1.get_atack() - self.__fighter2.get_atack())) > max_differanace_in_attack:
            raise TooStrong(max_differanace_in_attack)
       

if __name__ == '__main__':
    fighter4 = lab_5_copy.Fighter('Usyk', 100, 20)
    fighter5 = lab_5_copy.Fighter('Fury', 100, 65)
    fighter6 = lab_5_copy.Fighter('Joshua', 100, 65)
    saudi_arabia = Fight(fighter4, fighter5)
    saudi_arabia.fighter_attack(30)
