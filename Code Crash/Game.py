from tkinter import *
import random as rand

game = Tk()
game.title('Python Game')
game.geometry('1500x850+200+100')
game.maxsize(1500, 850)
game.minsize(1500, 850)
game.background()
game.resizable(False, False)

global frame_1, frame_0, button_1


def frame_one():
    global frame_1
    frame_0.place_forget()
    frame_1 = LabelFrame(game, text='Frame One', font=('Arial', 15), width=1200, height=750)
    frame_1.place(relx=0.5, rely=0.5, anchor=CENTER)
    button_2 = Button(frame_1, text='1', command=frame_zero, font=('Arial', 15))
    button_2.place(relx=0.5, rely=0.5, anchor=CENTER)


def frame_zero():
    global frame_0, button_1, frame_1
    frame_0 = LabelFrame(game, text='Frame Zero', width=1300, height=750)
    frame_0.place(relx=0.5, rely=0.5, anchor=CENTER)

    button1 = Button(frame_0, text='Click Me!', command=frame_one)
    button1.place(relx=0.5, rely=0.5, anchor=CENTER)


frame_zero()

game.mainloop()
