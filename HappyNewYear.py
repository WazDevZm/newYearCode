import random
import tkinter as tk
import time
from tkinter import ttk


#main window
root = tk.Tk()
root.title("Happy New Year")
root.geometry("800x600")
root.configure(bg="black")


def text(text, label):
    for i in range (len(text) + 1):
        label.config(text=text[:i])
        label.update()
        time.sleep(0.1)
        
def create_confetti(canvas):
    colors = ["red", "yellow", "green", "blue", "purple", "orange"]
    for _ in range(100):
        x = random.randint (0,800)
        y = random.randint (0,600)
        color =  random.choice(colors)
        canvas.create_oval(x,y,x+5,y+5, fill=color,  outline = color)
        
heading = tk.Label(
       root, text = "", font=("Helvetica", 36,"bold"), fg="gold", bg="black"
    )
heading.pack(pady=20)
 


subheading = tk.Label(
   root, text = "", font=("Helvetica", 24,"italic"), fg="white", bg="black"
    )
subheading.pack(pady=10)


canvas = tk.Canvas(root, width=800, height=400, bg="black",
                   highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

root.after(1000, lambda: text("🥳🍾Happy New Year 2025🎇🥂", heading))
root.after(5000, lambda: text("Wazingwa is wishing you joy and success", subheading))
root.after(7000, lambda: create_confetti(canvas))

root.mainloop()