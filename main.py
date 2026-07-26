import tkinter as tk

backgroundFolder = "data\\resources\\backgrounds"

# The game object
root = tk.Tk(className="Prometheus")

# Size of window
root.geometry("960x540")
root.resizable(0, 0)

bg_menu = tk.PhotoImage(file=backgroundFolder + "\\zone1\\image0.png")

background = tk.Canvas(root, highlightthickness=0)
background.pack(fill="both", expand=True)

background.create_image(0, 0, image=bg_menu, anchor="nw")

# Main Loop
root.mainloop()