from os import name
from turtle import speed
import weaponClass as w
import csv


"""
- Craete a program that will read the contents of the file 'weapons.txt'. Each record in the file represents the specs to a weapon.
- Create an instance of the weapon object for each record. 
- Create a dictionary that will contain the name of the weapon as the key and the number of bullets as the value. 
- Print out details of each weapon using the object's methods only (as per comments below). 
- Fire all bullets of the weapon and print a countdown of bullets remaining (run exe file to visualize, HINT: use end='\r' in your print statement).
- Print out the name of the weapon and the number of bullets from the dictionary.

HINT: Follow the comments for each line to help with the logic of the problem.
"""


# create a file object to open the file in read mode

weapons = open("weapons.csv", "r")

# create a csv object from the file object

weapons_file = csv.reader(weapons, delimiter=",")

# skip the header row

next(weapons_file)


# create an empty dictionary named 'weapons_dict'

weapons_dict = {}


# use a for loop to iterate through every row of the csv file
for i in weapons_file:
    # would this way work as well?
    # print(
    # "Weapon Name:",
    # i[0] + "\n" + "Weapon Speed:",
    # i[1] + "\n" + "Weapon Range:",
    # i[2],
    # )

    # input()

    # use variables for name,speed and range (optional)
    name = i[0]
    speed = i[1]
    gunrange = i[2]

    # create an instance of the weapon object using the
    # specs from the csv file (name,speed and range)
    my_weapon = w.Weapon(name, speed, gunrange)

    # append the name and bullet count to 'weapons_dict'
    my_weapon.set_numbullets()
    weapons_dict[name] = my_weapon.get_numbullets()
    # print out the name of the weapon using the appropriate method of the object
    print("Name of the weapon is:", my_weapon.get_gunname())
    # print out the speed of the weapon using the appropriate method of the object
    print("Speed of the weapon is:", my_weapon.get_speedofbull())
    # print out the range of the weapon using the appropriate method of the object
    print("Range of the weapon is:", my_weapon.get_gunrange())
    # print out the number of bullets of the weapon using the appropriate method of the object
    print("The number of bullets in the weapon:", my_weapon.get_numbullets())
    # use an input statement to halt the program and wait for the user -
    input("Press any key to fire the weapon")

    for b in range(my_weapon.get_numbullets()):
        my_weapon.set_status()
        # use an appropriate loop to keep firing the weapon until all bullets run out
        if my_weapon.get_status() == "Active":
            # call the appropriate method to fire a bullet
            my_weapon.fire_bullet()
            # print out the bullet count every time the weapon is fired
            print("Bullets remaining:", my_weapon.get_numbullets())
        else:
            print("There are no more bullets in the weapon")

# using a loop print out the name and number of bullets from the dictionary
for key, value in weapons_dict.items():
    print("Gun name:", key)
    print("Number of bullets left:", value)
