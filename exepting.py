import logging
import math
import lab_5_copy 
def logged(exception, logging_type):
    def outer(func):
        def inner(*args, **kwargs):
            if logging_type == "files" :
                logging.basicConfig(
                    filename="logs3.txt",
                    level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                    )
            else:
                logging.basicConfig(level=logging.DEBUG)
            try:
                func(*args, **kwargs)
            except exception:
                logging.exception(exception)
        return inner
    return outer
class TooStrong(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Your opponen has higher health on more than {self.value} points, the fight will be not fair "
    
class TooHealthy(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Your opponen has higher health on more than {self.value} points, the fight will be not fair "
    
class TooHugeTIMETOSLEEP(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"{self.value} sec is too slow, code will be going for too much time"
    
class HealthBeloveZero(Exception):
    def __str__(self):
        return f"{self.value} sec is too slow, code will be going for too much time"

    
class Fight(lab_5_copy.Fight):
    
    @logged(TooStrong, 'console')
    def is_fight_can_start(self, max_differance_in_attack, max_differance_in_health):
        if int(math.fabs(self.__fighter1.get_atack() - self.__fighter2.get_atack())) >= max_differance_in_attack:
            raise TooStrong(max_differance_in_attack)
        else:
            logging.info(f'attack {math.fabs(self.__fighter1.get_atack() - self.__fighter2.get_atack())} points is ok the fight will be')
        if int(math.fabs(self.__fighter1.get_atack() - self.__fighter2.get_atack())) >= max_differance_in_health:
            raise TooHealthy(max_differance_in_health)
        else:
            logging.info(f'health {math.fabs(self.__fighter1.get_health() - self.__fighter2.get_health())} points is ok the fight will be')
class Fighter(lab_5_copy.Fighter):
    def get_health(self):
        if self.__health < 0:
            raise HealthBeloveZero
       
        return self.__health
        
@logged(TooHugeTIMETOSLEEP, 'console')
def time_to_sleep_check(value):
    
    if lab_5_copy.TIME_TO_SLEEP >= value:
        raise TooHugeTIMETOSLEEP(value)
    else:
        logging.info('Code will be run comfotly')
        
if __name__ == '__main__':
    fighter4 = lab_5_copy.Fighter('Usyk', -10, 20)
    fighter5 = lab_5_copy.Fighter('Fury', 150, 30)
    fighter6 = lab_5_copy.Fighter('Joshua', 100, 65)
    saudi_arabia = Fight(fighter4, fighter5)
    time_to_sleep_check(3)
    
