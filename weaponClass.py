import random

"""
Create a Weapon Class definition according to the following specs:

Attributes:

name - user supplied
bullets - random number between 10 and 100000
speed - user supplied
range - user supplied
status - 'Active' (this attribute should be changed to 'Inactive' if bullets 
                    run out.)

Methods:

Create accessor methods for each attribute.

Create a method named 'fire_bullet' that will simulate
firing a bullet. This is accomplished by decreasing the number of bullets by 1 
every time the method is called. When the bullet count reaches zero, it should change
the attribute 'status' to 'Inactive'

"""
import random


class Weapon:
    def __init__(self, name, speed, gunrange):
        self.__gunname = name
        self.__numbullets = 0
        self.__speedofbull = speed
        self.__gunrange = gunrange
        self.__status = "Active"

    def set_gunname(self, name):
        self.__gunname = name

    def set_numbullets(self):
        # set this equal to the random numbers, and eliminate
        # the bullets variable since you initialized it to 0
        self.__numbullets = random.randint(10, 100000)

    def set_speedbull(self, speed):
        self.__speedofbull = speed

    def set_range(self, gunrange):
        self.__gunrange = gunrange

    def set_status(self):
        if self.__numbullets == 0:
            self.__status = "Inactive"
        else:
            self.__status = "Active"

    def get_gunname(self):
        return self.__gunname

    def get_numbullets(self):
        return self.__numbullets

    def get_speedofbull(self):
        return self.__speedofbull

    def get_gunrange(self):
        return self.__gunrange

    def get_status(self):
        return self.__status

    def fire_bullet(self):
        self.__numbullets = self.__numbullets - 1
        return self.__numbullets
