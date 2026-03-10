# OOPS
# class create name Hero
import random


class Hero:
    # init is constructor here automatically called at the time of object creation
    def __init__(self, name, energy):
        # self works as this pointer i.e., object --> get a name that point to that particular objects name
        self.name = name
        self.energy = energy
# function to check the self details i.e., objects details

    def check_self(self):
        print(f"My name is {self.name} and My Energy is {self.energy}%")
# being attacked by the villen

    def attack(self):
        damage = random.randint(40, 100)
        self.energy -= damage
        print(f"Thanos arrived!\nFight begin...\n{self.name} is getting damage")
        if self.energy < 0: #if the hero's energy left 0
            self.energy = 0
            print(f"💥OOUCH!!,damaged very hard.\nNeed to heal \nRemaining Energy:{self.energy}%\n{self.name} defeated!☠️")
        else:
            print(f"Remaining Energy:{self.energy}%")        
#Game start from here
print("\nGame start!!!")
# Input name for hero
name_input = input("Enter the name for your hero.🦸‍♀️: ")
# input energy until a valid energy level
energy_input = int(
    input("Enter the Energy level for the Hero between 0 to 100: "))
while True:
    if 0 <= energy_input <= 100:
        break
    else:
        energy_input = int(input("Invalid! Please enter between 0 to 100: "))
player1 = Hero(name_input, energy_input)
player1.check_self()
player1.attack()
