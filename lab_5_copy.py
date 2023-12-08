'''
this module is for K/O code and delays
'''
import random as rnd
import time as t
TIME_TO_SLEEP = 1
class Fighter:
    '''
    this cls is Fighters
    '''
    def __init__(self, name, health, damage_per_attack):
        '''
        initializating attibutes
        '''
        self.__name = name
        self.__health = health
        self.__damage_per_attack = damage_per_attack
    def get_name(self):
        '''
        getter from name
        '''
        return self.__name
    def get_health(self):
        '''
        getter from health and health check for < 0
        '''
        if self.__health > 0:
            return self.__health
        return 0
    def get_atack(self):
        '''
        getter from atack
        '''
        return self.__damage_per_attack
    def set_health(self, health_to_set):
        '''
        setters of health
        '''
        self.__health = health_to_set
        return self.__health
    def get_characteristics(self):
        '''
            this fnc gives you Characteristics of fighter
        '''
        print(f'Characteristics of Fighter: '
                f'Name: {self.__name}, '
                f'Health: {self.__health}, '
                f'damage per attack: {self.__damage_per_attack}')
        Fight.line()
        t.sleep(TIME_TO_SLEEP)
        return self.get_name(), self.get_health(), self.get_atack()
    def fighter_entering_ring(self):
        '''
            this fnc means entering of fighter on ring
        '''
        print(f'\nMeet {self.__name} today on ring ')
        
class Fight:
    '''
        This class is Fight of Fighters
    '''
    def __init__(self, fighter1, fighter2):
        self.__fighter1 = fighter1
        self.__fighter2 = fighter2
    def get_fighters(self):
        '''
        getter from instance
        '''
        return self.__fighter1, self.__fighter2
    def fighter_atack(self, fighter1, fighter2):
        '''
        Fnc that means atack of Fighter
        '''
        #віднімаю здоров'я і атаку
        fighter2_health = fighter2.get_health() - fighter1.get_atack()
        #k/o code
        random_number = rnd.randint(0, 100)
        if random_number == 1:
            fighter2.set_health(-10)
            print(f'\n Woooow {fighter1.get_name()} knocked out his opponent its ammazing')
        elif self.__fighter2.get_health() > 0:
            fighter2.set_health(fighter2_health)
            print(f'\n{fighter1.get_name()} made an atack with'
                  f' {fighter1.get_atack()} points of damage and left '
                  f'{fighter2.get_health()} '
                  f'to {fighter2.get_name()}')
        #delay
        t.sleep(TIME_TO_SLEEP)
        Fight.line()
        t.sleep(TIME_TO_SLEEP)
    @staticmethod
    def line():
        '''
        this fnc is going line
        '''
        i = 0
        while i < 60:
            print('_', end = '')
            t.sleep(0.01)
            i += 1
    def countdown(self):
        '''
            this fnc means start of the round
        '''
        self.__fighter1.fighter_entering_ring()
        self.__fighter1.get_characteristics()
        self.__fighter2.fighter_entering_ring()
        self.__fighter2.get_characteristics()
        print('\n                     Rooond starts after: ')
        i = 3
        while i > 0:
            print(f'                               {i}')
            i -= 1
            t.sleep(1)
        print('                             FIGHT')
        t.sleep(TIME_TO_SLEEP)
    def round(self):
        '''
            Round conduct
        '''
        self.countdown()
        while True:
            if self.__fighter1.get_health()  > 0:
                self.fighter_atack(self.__fighter1, self.__fighter2)
            elif self.__fighter1.get_health() <= 0:
                self.__fighter1.set_health(0)
                print(f'\n {self.__fighter1.get_name()} lost the Fight')
                break
            if self.__fighter2.get_health() > 0:
                self.fighter_atack(self.__fighter2, self.__fighter1)
            elif self.__fighter2.get_health() <= 0:
                self.__fighter2.set_health(0)
                print(f'\n {self.__fighter2.get_name()} lost the Fight')
                break

if __name__ == '__main__':
    fighter4 = Fighter('Usyk', 100, 20)
    fighter5 = Fighter('Fury', 100, 20)
    fighter6 = Fighter('Joshua', 100, 20)
    saudi_arabia = Fight(fighter4, fighter5)
    saudi_arabia.round()
