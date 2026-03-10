#File Handling
mission_name = "Operation Time-Rift"
#w --> create then write function to write in that file
with open("mission.txt", "w") as file:
    file.write(f"Mission Report: {mission_name}")
#a --> append new data to the file
with open("mission.txt", "a") as file:
    file.write("\nPhase 2: Scanning for anomalies")
#r --> To Read file, read function(read())
with open("mission.txt", "r") as file:
    content = file.read()
    print(content)