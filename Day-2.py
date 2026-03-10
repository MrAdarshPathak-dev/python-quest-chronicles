# ladder for python basics
while True:
    command = input("I am TimerMan. Say Your Command:").lower()
    if command == "exist":
        print("powering down!!!".capitalize())
        break
    print(f"Executing Command: {command}")


#dictionary

modes = {"Recon": "Silent and Sleathy",
         "Combat": "High power and Sheilds",
         "Emergency": "Teleport to Safety"}
choice = input("Which mode should I describe? ").capitalize()
if choice in modes:
    print(f"{modes[choice]}")
else:
    print("Mode not found in system!")

#loops + dictionary
systems = {
    "Sensors" : 85,
    "Engines" : 12,
    "LifeSupport" : 95,
    "Cloak" : 18
}
for name, value in systems.items():
    verb = "are" if name == "Engines" or name == "Sensors" else "is"
    if 20 > value:
        print(f"CRITICAL: {name} {verb} falling at {value}% ")
    else:
        print(f"{name} {verb} stable. ")


#functions
def check_status(system_name,power_level):
    if power_level < 20:
        print(f"WARNING!!! {system_name} is critical...")
    else:
        print(f"{system_name} is operational.")
system_name = input("Enter the system name: ")
power_level = int(input("Enter the power level: "))
check_status(system_name,power_level)

def calculate_cost(years,unit = 50):
    calculation = years * unit
    return calculation
years = int(input("How many years back do you want to go?"))
final_cost = calculate_cost(years)
print(f"That jump will cost {final_cost} units of energy.")

def filter_anomalises(readings_list):
    dangerous_zones = []  # empty list for dangerous zone
    for reading in readings_list:
        if reading > 75:
            # instert the data into dangerous list
            dangerous_zones.append(reading)
    return dangerous_zones


scan_data = []
print("When you done the data insertion pass value 0")
while True:
    data = int(input("Enter the data to scan: "))
    if data == 0:
        break
    scan_data.append(data)
alerts = filter_anomalises(scan_data)
print("The alert list:",alerts)