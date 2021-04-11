from tkinter import *
import random

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock-Paper-Scissors Game')
root.config(bg ='#a3d2ca')

user_take = StringVar()
Label(root, text = 'Choose any one: rock, paper, scissors' , font='arial 15 bold', bg = '#a3d2ca').place(x = 20,y=70)
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'antiquewhite2').place(x=90 , y = 130)

comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'

Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('TIE')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('You lost, as computer selected paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('You win, as computer selected scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('You lost, as computer selected scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('You win, as computer selected rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('You loose, as computer selected rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('You win , as computer selected paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')

def Reset():
    Result.set("")
    user_take.set("")

def Exit():
    root.destroy()

Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 15 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 15 bold', text = 'RESTART'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310)

Button(root, font = 'arial 15 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)


root.mainloop()
