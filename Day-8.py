#OOPS INHERITENCE
import random
class Hero:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
    def check_self(self):
        print(f"My name is {self.name} and My Energy is {self.energy}%")
    def attack(self):
        damage = random.randint(40, 100)
        self.energy -= damage
        print(f"Thanos arrived!\nFight begin...\n{self.name} is getting damage")
        if self.energy < 0: 
            self.energy = 0
            print(f"💥OOUCH!!,damaged very hard.\nNeed to heal \nRemaining Energy:{self.energy}%\n{self.name} defeated!☠️")
        else:
            print(f"Remaining Energy:{self.energy}%")        
print("\nGame start!!!")
class TimeMaster(Hero):
    def rewind_time(self):
        self.energy =100
        print("Time Rewinded! Energy Restored")
player2 = TimeMaster("TimerMan_Pro",50)
player2.attack()
player2.rewind_time()
