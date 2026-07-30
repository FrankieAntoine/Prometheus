# save1Data = {"Name": "Boy1", "Time": 0}
# save2Data = {"Name": "Boy2", "Time": 60}
# save3Data = {"Name": "Boy3", "Time": 180}
# player = {}

# player = save1Data
# print(player["Name"] + " " + str(player["Time"]))
# player = save2Data
# print(player["Name"] + " " + str(player["Time"]))
# player = save3Data
# print(player["Name"] + " " + str(player["Time"]))

# player["Name"] = "Girl1"
# print(player["Name"])
# print(save3Data["Name"])

# # These tests concluded that when file writing and reading you only need to set the players stats the the selected file and when saving only need to write the save data back onto the file

# playerKeys = ["name", "time"]
# save1Data = {"name": "Boy1", "time": 0}
# save2Data = {"name": "Boy2", "time": 60}
# save3Data = {"name": "Boy3", "time": 180}

# player = {}

# # use zip to make the dict

save3File = "data\\saves\\save1"

playerKeys = ["name", "time"]
save1Data = []
save2Data = []
save3Data = []
player = {}

# Function to open a file and load the data given into a list
def readFile(fileName, list):
    file = open(fileName)
    while True:
        data = file.readline().rstrip("\n")
        if data == "":
            break
        list.append(data)
    file.close()

readFile(save3File, save3Data)
print(save3Data)