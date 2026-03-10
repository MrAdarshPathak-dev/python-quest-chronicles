#Libraries and modules
import random
rift_multipliers = [0.5, 1.2, 2.0, 3.5]
effect = random.choice(rift_multipliers)
current_energy = int(input("Enter your current energy: "))
new_energy = effect * current_energy
print(
    f"The rift affected you by a factor of {effect}!!!\nNew Energy: {new_energy}")

#Timerman catchphrase 
import random
import cowsay
catchphrases = ["Vikki", "Tick Tock!", "No Chance!"]
fav_phrase = random.choice(catchphrases)
cowsay.cow(fav_phrase)
