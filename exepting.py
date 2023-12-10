'''
logging
'''
#pylint: disable=W1203
import logging
import math
import lab_5_copy
def logged(exception, logging_type):
    def logger(func):
        def inner(*args, **kwargs):
            if logging_type == 'file':
                logging.basicConfig(
                    filename = 'log2.txt',
                    filemode = 'w',
                    level = logging.DEBUG,
                )
            else:
                logging.basicConfig(level = logging.DEBUG)

            try:
                func(*args, **kwargs)
            except exception:
                logging.exception(exception)
            except Exception:
                logging.exception(Exception)
        return inner
    return logger
class TooStrong(Exception):
    '''
    class exeption means too strong
    '''
    def __init__(self, value):
        '''
        init
        '''
        self.value = value
    def __str__(self):
        '''
        str
        '''
        return f"Your opponen has higher attack on more than {self.value}\
                    points, the fight will be not fair "

class TooHealthy(Exception):
    '''
    class exeption means that fight is not fair
    '''
    def __init__(self, value):
        '''
        init
        '''
        self.value = value
    def __str__(self):
        '''
        str
        '''
        return f"Your opponen has higher health on more than {self.value}\
                    points, the fight will be not fair "

class TooHugeTIMETOSLEEP(Exception):
    '''
    too huge time and code is uncomfortable
    '''
    def __init__(self, value):
        '''
        init
        '''
        self.value = value
    def __str__(self):
        '''
        str
        '''
        return f"{lab_5_copy.TIME_TO_SLEEP} sec is too slow, code will be going for too much time, try {self.value}"

class HealthBeloveZero(Exception):
    '''
    class health below zero
    '''
    def __str__(self):
        return "Health returned belove zero"


class Fight(lab_5_copy.Fight):
    '''
    fight
    '''
    @logged(TooStrong, 'file')
    def is_attack_good(self, max_differance_in_attack):
        '''
        check if fight can start 
        '''
        differance_in_attack = (self.__fighter1.get_atack() - self.__fighter2.get_atack())
        if int(math.fabs(differance_in_attack)) >= max_differance_in_attack:
            raise TooStrong(max_differance_in_attack)
        logging.info(f'attack diffarance {math.fabs(differance_in_attack)} points is ok the fight will be')
    @logged(TooHealthy, 'file')
    def is_health_good(self, max_differance_in_health):
        differance_in_health = (self.__fighter1.get_health()) - self.__fighter2.get_health()
        if int(math.fabs(differance_in_health)) >= max_differance_in_health:
            raise TooHealthy(max_differance_in_health)
        logging.info(f'health diffarance {math.fabs(differance_in_health)} points is ok the fight will be')

class Fighter(lab_5_copy.Fighter):
    '''
    fighter
    '''
    @logged(HealthBeloveZero, 'files')
    def get_health_check(self):
        '''
        health check is it below zero
        '''
        if self.__health < 0:
            raise HealthBeloveZero
        return self.__health

@logged(TooHugeTIMETOSLEEP, 'files')
def time_to_sleep_check(value):
    '''
    max time to sleep
    '''
    if lab_5_copy.TIME_TO_SLEEP >= value:
        raise TooHugeTIMETOSLEEP(value)
    logging.info('Code will be run comfotly')


fighter4 = Fighter('Usyk', -20, 20)
fighter5 = Fighter('Fury', 50, 40)
fighter6 = Fighter('Joshua', 100, 65)
saudi_arabia = Fight(fighter4, fighter5)
saudi_arabia.is_health_good(100)
saudi_arabia.is_attack_good(10)
fighter4.get_health_check()
time_to_sleep_check(4)