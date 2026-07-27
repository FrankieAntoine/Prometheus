# Prometheus - Remade in Tkinter
# Frankie Antoine
# July 25th - Present

#Imports
import tkinter as tk

# Variables
backgroundFolder = "data\\resources\\backgrounds"

# The game object
root = tk.Tk()
root.geometry("960x540")
root.resizable(0, 0)
root.title("Prometheus")

# ----- Background images -----
bg_menu = tk.PhotoImage(file=backgroundFolder + "\\zone1\\image0.png")

# page setup
page_start = tk.Frame(root)
page_saves = tk.Frame(root)

pages = [page_start, page_saves]
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
    changePage(page_saves)

# Creation
btn_start = tk.Button(page_start, text="START", font=("Arial", 20, "bold"), bg="white", fg="red", command=command_start)
btn_start.place(x=480, y=520, width=125, height=100, anchor="s")

# ---------- SAVES MENU ----------

# Background creation
background_saves = tk.Canvas(page_saves, highlightthickness=0)
background_saves.pack(fill="both", expand=True)
background_saves.create_image(0, 0, image=bg_menu, anchor="nw")

# ----- Buttons -----

# --- Save 1 ---

# Command
def command_loadSave1():
    print("Save 1 Loaded!")

# Creation
btn_save1 = tk.Button(page_saves, text="SAVE 1", font=("Arial", 10, "bold"), bg="white", fg="green", command=command_loadSave1)
btn_save1.place(x=100, y=50, width=50, height=50, anchor="nw")

# --- Save 2 ---

# Command
def command_loadSave2():
    print("Save 2 Loaded!")

# Creation
btn_save2 = tk.Button(page_saves, text="SAVE 2", font=("Arial", 10, "bold"), bg="white", fg="green", command=command_loadSave2)
btn_save2.place(x=150, y=50, width=50, height=50, anchor="nw")

# --- Save 3 ---

# Command
def command_loadSave3():
    print("Save 3 Loaded!")

# Creation
btn_save3 = tk.Button(page_saves, text="SAVE 3", font=("Arial", 10, "bold"), bg="white", fg="green", command=command_loadSave3)
btn_save3.place(x=200, y=50, width=50, height=50, anchor="nw")


# Main Loop
changePage(page_start)
root.mainloop()