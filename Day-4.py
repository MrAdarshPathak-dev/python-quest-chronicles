#Ship Management System
import random
#Default ship health
#Function to apply damage
ship_systems = {
    "Navigator" : 100,
    "Oxygen" : 100,
    "Engines" : 100
}
def apply_damage(systems_dict):
    #Select Random System from the dictionary
    rand_system = random.choice(list(systems_dict.keys()))
    #Get value of selected system 
    system_value = systems_dict[rand_system]
    #get damage value
    damage = random.randint(10,50)
    #calculate total damage and update 
    final_damage = system_value - damage
    systems_dict[rand_system] = final_damage
    return rand_system, systems_dict[rand_system]
#loop to scan damage
while True:
    #taking user input
    user_input = input("Scan system? (yes or exit)").lower()
    # exit command
    if user_input == "exit":
        print("EXITED!!!")
        break
    else: 
        #geting returned function value in variable
        name,new_value = apply_damage(ship_systems)
        if new_value <= 0:
            print(f"CRITICAL! {name} Destroyed. Ship damaged.... ")
            break
        else:
            print(f"Alert! {name} hit. New Status: {new_value}%")