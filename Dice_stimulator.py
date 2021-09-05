from tkinter import *
import random

root=Tk()
root.title("Dice Stimulator")
root.geometry("600x500")

label=Label(root,font=("Helvitica", 400 ,'bold'),text="",fg='Blue')

def rolldice():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack()

button=Button(root,font=("Helvitica,30,'bold"),text="Dice Roll",command=rolldice,bg='lightblue',fg='red')
button.pack()

root.mainloop()