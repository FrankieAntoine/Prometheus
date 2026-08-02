# Prometheus - Remade in Tkinter
# Frankie Antoine
# July 25th - Present

#Imports
import tkinter as tk

# Variables
backgroundFolder = "data\\resources\\backgrounds"
save1File = "data\\saves\\save1"
save2File = "data\\saves\\save2"
save3File = "data\\saves\\save3"

# The game object
root = tk.Tk()
root.geometry("960x540")
root.resizable(0, 0)
root.title("Prometheus")

# ----- Background images -----

# Zone 1 start background
bg_menu = tk.PhotoImage(file=backgroundFolder + "\\zone1\\image0.png")

# Zone 1 area backgrounds
bg_z1a1 = tk.PhotoImage(file=backgroundFolder + "\\zone1\\image1.png")
bg_z1a2 = tk.PhotoImage(file=backgroundFolder + "\\zone1\\image2.png")
bg_z1a3 = tk.PhotoImage(file=backgroundFolder + "\\zone1\\image3.png")
bg_z1a4 = tk.PhotoImage(file=backgroundFolder + "\\zone1\\image4.png")
bg_z1a5 = tk.PhotoImage(file=backgroundFolder + "\\zone1\\image5.png")
bg_z1a6 = tk.PhotoImage(file=backgroundFolder + "\\zone1\\image6.png")
bg_z1a7 = tk.PhotoImage(file=backgroundFolder + "\\zone1\\image7.png")
bg_z1a8 = tk.PhotoImage(file=backgroundFolder + "\\zone1\\image8.png")
bg_z1a9 = tk.PhotoImage(file=backgroundFolder + "\\zone1\\image9.png")
bg_z1a10 = tk.PhotoImage(file=backgroundFolder + "\\zone1\\image10.png")
z1Backgrounds = [bg_z1a1, bg_z1a2, bg_z1a3, bg_z1a4, bg_z1a5, bg_z1a6, bg_z1a7, bg_z1a8, bg_z1a9, bg_z1a10]

# Zone 1 boss background
bg_z1b1 = tk.PhotoImage(file=backgroundFolder + "\\zone1\\image11.png")

# page setup
page_start = tk.Frame(root)
page_saves = tk.Frame(root)
page_main = tk.Frame(root)

pages = [page_start, page_saves, page_main]
for frame in pages:
    frame.grid(row=0, column=0, sticky="nsew")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Change page funtion
def changePage(page):
    page.lift()

# ---------- START MENU ----------

# Background creation
background_start = tk.Canvas(page_start, highlightthickness=0)
background_start.pack(fill="both", expand=True)
background_start.create_image(0, 0, image=bg_menu, anchor="nw")

# ----- Buttons -----

# --- Start ---

# Command
def command_start():
    createSaves()
    loadSaves()
    changePage(page_saves)

# Creation
btn_start = tk.Button(page_start, text="START", font=("Consolas", 20, "bold"), bg="white", fg="red", command=command_start)
btn_start.place(x=480, y=520, width=125, height=100, anchor="s")

# ---------- SAVES MENU ----------

# Background creation
background_saves = tk.Canvas(page_saves, highlightthickness=0)
background_saves.pack(fill="both", expand=True)
background_saves.create_image(0, 0, image=bg_menu, anchor="nw")

# ----- Variables -----
playerKeys = ["name", "time", "zone", "area"] # list to store the player keys for the dictionary
save1Data = [] # List to store the data from file 1
save2Data = [] # List to store the data from file 2
save3Data = [] # List to store the data from file 3
player = {} # Dictionary to store the main player stats. Originally obtained by the save file

# Save file componient definitions
text_save1_title: tk.Label = None; text_save1_keys: tk.Message = None; text_save1_data: tk.Message = None; btn_save1: tk.Button = None
text_save2_title: tk.Label = None; text_save2_keys: tk.Message = None; text_save2_data: tk.Message = None; btn_save2: tk.Button = None
text_save3_title: tk.Label = None; text_save3_keys: tk.Message = None; text_save3_data: tk.Message = None; btn_save3: tk.Button = None

# ----- Functions -----

# Function to open a file and load the data given into a list
def readFile(fileName, list):
    file = open(fileName)
    while True:
        data = file.readline().rstrip("\n")
        if data == "":
            break
        list.append(data)
    file.close()

# A function that turns all the string data into floats and ints if needed
def configData(list):
    list[0] = str(list[0])
    for i in range(1, len(list)):
        list[i] = int(list[i])
    return list

# A function to turn the save data lists into a string for the save files to show
def getListStr(list):
    dataStr = ""
    for i in range(len(list)):
        dataStr+= str(list[i]) + "\n"
    return dataStr

# Function that loads all the files into their data lists and updates the saves on the save page
def loadSaves():
    readFile(save1File, save1Data)
    text_save1_data.config(text=getListStr(save1Data))
    readFile(save2File, save2Data)
    text_save2_data.config(text=getListStr(save2Data))
    readFile(save3File, save3Data)
    text_save3_data.config(text=getListStr(save3Data))

def getDict(keys, data):
    return dict(zip(keys, data))

# Function that loads the save data into the player data
def loadPlayer(saveData):
    global player
    saveData = configData(saveData)
    player = getDict(playerKeys, saveData)
    player["currentArea"] = player["area"]
    
# Function that creates all of the visual saves using a for loop
def createSaves():

    # Stating the global functions being modified
    global text_save1_title, text_save1_keys, text_save1_data, btn_save1
    global text_save2_title, text_save2_keys, text_save2_data, btn_save2
    global text_save3_title, text_save3_keys, text_save3_data, btn_save3

    # Command list
    commandList = [command_loadSave1, command_loadSave2, command_loadSave3]

    # x variable storing the x value difference between each save file
    x = 240

    # For loop to create each componient dynamically
    for i in range(0, 3):

        # Background
        background_saves.create_rectangle(150 + (i*x), 90, 330 + (i*x), 450, fill="white", outline="black", width=2)

        # Title
        save_lbl = tk.Label(page_saves, text="SAVE " + str(i+1), font=("Consolas", 15, "bold"), bg="grey")
        save_lbl.place(x=240 + (i*x), y=120, width=180, height=50, anchor="n")

        # Keys
        save_keys = tk.Message(page_saves, text="Name:\nTime:\nZone:\nArea:", font=("Consolas", 13, "bold"), bg="white", anchor="nw", justify="left")
        save_keys.place(x=150 + (i*x), y=170, width=90, height=230)

        # Data
        save_data = tk.Message(page_saves, font=("Consolas", 13, "bold"), bg="white", anchor="ne", justify="right")
        save_data.place(x=240 + (i*x), y=170, width=90, height=230)

        # Button
        save_button = tk.Button(page_saves, text="LOAD", font=("Consolas", 10, "bold"), bg="white", command=commandList[i])
        save_button.place(x=240 + (i*x), y=400, width=180, height=50, anchor="n")

        # transfer the dynamically created componients back into their repective save file names
        if i == 0: text_save1_title, text_save1_keys, text_save1_data, btn_save1 = save_lbl, save_keys, save_data, save_button
        elif i == 1: text_save2_title, text_save2_keys, text_save2_data, btn_save2 = save_lbl, save_keys, save_data, save_button
        elif i == 2: text_save3_title, text_save3_keys, text_save3_data, btn_save3 = save_lbl, save_keys, save_data, save_button

# ----- Button commands -----

# Save 1 command
def command_loadSave1():
    loadPlayer(save1Data)
    print("Save 1 Loaded!")
    print(player)
    changePage(page_main)
    background_main.itemconfig(areaImage, image=z1Backgrounds[player["currentArea"] - 1])
    configAreaButtons()

# Save 2 command
def command_loadSave2():
    loadPlayer(save2Data)
    print("Save 2 Loaded!")
    print(player)
    changePage(page_main)
    background_main.itemconfig(areaImage, image=z1Backgrounds[player["currentArea"] - 1])
    configAreaButtons()


# Save 3 command
def command_loadSave3():
    loadPlayer(save3Data)
    print("Save 3 Loaded!")
    print(player)
    changePage(page_main)
    background_main.itemconfig(areaImage, image=z1Backgrounds[player["currentArea"] - 1])
    configAreaButtons()

# ---------- Main Page ----------
background_main = tk.Canvas(page_main, highlightthickness=0)
background_main.pack(fill="both", expand=True)
areaImage = background_main.create_image(0, 0, image=bg_z1a1, anchor="nw")

# ----- Variables -----

# ----- Functions -----

# A function that goes to the next area if possible
def command_nextArea():
    global player
    player["currentArea"] = player["currentArea"] + 1
    background_main.itemconfig(areaImage, image=z1Backgrounds[player["currentArea"] - 1])
    btn_nextArea.place_forget()
    configAreaButtons()

# A function that goes to the previous area if possible
def command_prevArea():
    global player
    player["currentArea"] = player["currentArea"] - 1
    background_main.itemconfig(areaImage, image=z1Backgrounds[player["currentArea"] - 1])
    btn_prevArea.place_forget()
    configAreaButtons()

# A function that finds out if the area button should be placed or not based on the current area and max area the player can go
def configAreaButtons():
    btn_nextArea.place(x=960, y=540, width=180, height=50, anchor="se")
    btn_prevArea.place(x=0, y=540, width=180, height=50, anchor="sw")
    if player["currentArea"] == 1:
        btn_prevArea.place_forget()
    if (player["currentArea"] == player["area"]) or (player["currentArea"] == 10):
        btn_nextArea.place_forget()

# ----- buttons -----

btn_nextArea = tk.Button(page_main, text="Next Area", font=("Consolas", 10, "bold"), bg="white", anchor="center", command=command_nextArea)
btn_prevArea = tk.Button(page_main, text="Prev Area", font=("Consolas", 10, "bold"), bg="white", anchor="center", command=command_prevArea)


# ----- Main Loop -----
changePage(page_start)
root.mainloop()