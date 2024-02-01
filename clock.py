# -*- coding: utf-8 -*-
import tkinter as tk 
import time

def update_clock():
    current_time = time.strftime("%H : %M : %S")
    ceas.config(text=current_time)
    ceas.after(1000,update_clock)
    
app = tk.Tk()
app.title("Ceas Python")
    
ceas = tk.Label(app, text="", font=("Helvetica", 48), fg="yellow", bg="green")
ceas.pack()
 
update_clock()
app.mainloop()
    