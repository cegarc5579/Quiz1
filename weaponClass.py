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
    def __init__(self, bullets, speed, range, status):
        self.__numbullets = bullets
        self.__speedofbull = speed
        self.__gunrange = range
        self.__status = status

    def get__numbullets(self):
        return self.__numbullets

    def get_speedofbull(self):
        return self.__speedofbull

    def get_gunrange(self):
        return self.__gunrange

    def get_status(self):
        return self.__status

    def fire_bullet(self, bullets):
        self.__numbullets -= 1
        return self.__numbullets


"""
    def bullet_count(self):
        if self.__numbullets = 0:
            self.__status = "Inactive"
        else:
            return self.__numbullets


"""
