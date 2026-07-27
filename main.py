import tkinter as tk

# Variables
backgroundFolder = "data\\resources\\backgrounds"

# The game object
root = tk.Tk(className="Prometheus")

# Size of window
root.geometry("960x540")
root.resizable(0, 0)

# Background image
bg_menu = tk.PhotoImage(file=backgroundFolder + "\\zone1\\image0.png")

# Background creation
window = tk.Canvas(root, highlightthickness=0)
window.pack(fill="both", expand=True)

# Background placement
window.create_image(0, 0, image=bg_menu, anchor="nw")

# Button creation
btn_start = tk.Button(root, text="START", font=("Arial", 20, "bold"), bg="white", fg="red")
btn_start.place(x=480, y=520, width=125, height=100, anchor="s")

# Main Loop
root.mainloop()