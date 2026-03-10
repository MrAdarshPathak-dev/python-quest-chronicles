#data convertion
import json
status = {
    "energy": 65,
    "location": "mars"}
with open("status.json","w") as file:
    json.dump(status,file)
with open("status.json","r") as file:
    current_status = json.load(file)
print(current_status["location"])
# =======================================================================================================================
#Error Handling
import json
status = {
    "energy": 65,
    "location": "mars"}
try:
    with open("status.json", "r") as f:
        print(json.load(f))
except FileNotFoundError:
    print("No save file found. Starting Fresh!!!")
else:
    print("Data loaded successfully!✅")
