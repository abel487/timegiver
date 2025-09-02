print("Time theif")
print("abel")


import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Time Thief")           # Title bar
root.geometry("400x300")           # Window size (Width x Height)
root.configure(bg="#1e1e1e")       # Dark background color

# Heading Label
title_label = tk.Label(
    root,
    text="Time Thief",
    font=("Helvetica", 24, "bold"),
    fg="#00ff00",                  # Green text
    bg="#1e1e1e",                  # Same as background
    pady=20
)
title_label.pack()

# Placeholder content
content = tk.Label(
    root,
    text="Welcome to your time-tracking base app.",
    font=("Helvetica", 12),
    fg="#cccccc",
    bg="#1e1e1e"
)
content.pack()

# Start the Tkinter event loop
root.mainloop()
