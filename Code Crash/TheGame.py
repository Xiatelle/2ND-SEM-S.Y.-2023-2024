import tkinter
from tkinter import *
import random
from tkinter import messagebox
import pygame

tree_grow = Tk()
tree_grow.geometry('1500x850+200+100')
tree_grow.title("TGrow")
tree_grow.maxsize(1500, 850)
tree_grow.minsize(1500, 850)

background_img = PhotoImage(file='bg_img.png')
tree_grow_bg = Label(image=background_img)
tree_grow_bg.pack()

play_btn_img = PhotoImage(file='play_btn_img.png')
exit_btn_img = PhotoImage(file='exit_btn_img.png')
higher_btn_img = PhotoImage(file='higher_btn_img.png')
lower_btn_img = PhotoImage(file='lower_btn_img.png')
equal_btn_img = PhotoImage(file='equal_btn_img.png')
next_btn_img = PhotoImage(file='next_btn_img.png')
reveal_btn_img = PhotoImage(file='reveal_btn_img.png')
score_bg_img = PhotoImage(file='score_img.png')
correct_img = PhotoImage(file='correct_img.png')
wrong_img = PhotoImage(file='wrong_img.png')
plant_trees_img = PhotoImage(file='plant_trees_btn_img.png')
rounds_lbl_img = PhotoImage(file="rounds_img.png")
card1_img = PhotoImage(file='reveal_1_img.png')
card2_img = PhotoImage(file='reveal_2_img.png')
trees1 = PhotoImage(file='plant_5_img.png')
trees2 = PhotoImage(file='plant_10_img.png')
trees3 = PhotoImage(file='plant_15_img.png')
trees4 = PhotoImage(file='plant_23_img.png')

global frame_1, frame_0, number_1, user_tree_lbl, number_2, num2_lbl, reveal_btn, higher_btn, lower_btn, equal_btn, play_btn, wrong_lbl, correct_lbl, next_btn, win, trees_planted

pygame.mixer.init()
pygame.mixer.music.load("Red Dead Redemption 2 Free Roam Music 10 (Cumberland Forest).mp3")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(loops=6)

user_tree = 10
rounds = 1


def game_start():
    global frame_0, play_btn
    play_btn = Button(tree_grow, text="Start", command=play_game, image=play_btn_img)
    play_btn.place(relx=0.5, rely=0.5, anchor=CENTER)
    exit_btn = Button(tree_grow, text="Exit", command=exit_game, image=exit_btn_img)
    exit_btn.place(x=30, y=300)


def play_game():
    global number_1, user_tree, user_tree_lbl, reveal_btn, higher_btn, lower_btn, equal_btn, tree_grow, win, rounds_lbl, correct_lbl, wrong_lbl, next_btn, play_btn_img, status

    play_btn.destroy()
    win = 0


    if rounds < 10 and user_tree > 0:
        card_1 = Label(tree_grow, image=card1_img)
        card_1.place(x=300, y=200)
        card_2 = Label(tree_grow, image=card2_img)
        card_2.place(x=900, y=200)
        score_img_lbl = Label(tree_grow, image=score_bg_img, font=("Rye", 25))
        score_img_lbl.place(x=1000, y=45)

        user_tree_lbl = Label(tree_grow, text="Trees: " + str(user_tree), font=("Rye", 30), bg="#e2a757", fg="white")
        user_tree_lbl.place(x=1020, y=45)

        rounds_img = Label(tree_grow, image=rounds_lbl_img)
        rounds_img.place(x=600, y=38)

        rounds_lbl = Label(tree_grow, text="Rounds: " + str(rounds), font=("Rye", 30), bg="#e2a757", fg="white")
        rounds_lbl.place(x=650, y=40)

        number_1 = random.randint(1, 13)

        num1_lbl = Label(tree_grow, text=number_1, font=("Rye", 150), bg="#e2a757", fg="white")
        num1_lbl.place(x=400, y=210)

        higher_btn = Button(tree_grow, text='Higher', font=('Rye', 15), bg='white', fg='black', command=higher,
                            image=higher_btn_img)
        higher_btn.place(x=50, y=530)

        lower_btn = Button(tree_grow, text='Lower', font=('Arial', 15), bg='white', fg='black', command=lower,
                           image=lower_btn_img)
        lower_btn.place(x=1015, y=530)

        equal_btn = Button(tree_grow, text='Equal', font=('Arial', 15), bg='white', fg='black', command=equal,
                           image=equal_btn_img)
        equal_btn.place(x=530, y=530)

        reveal_btn = Button(tree_grow, text='Reveal', font=('Arial', 15), bg='white', fg='black', command=reveal,
                            image=reveal_btn_img)
        reveal_btn.place(x=530, y=730)

        reveal_btn['state'] = "disable"

    elif rounds >= 10 and user_tree > 0:

        card_1 = Label(tree_grow, image=card1_img)
        card_1.place(x=300, y=200)
        card_2 = Label(tree_grow, image=card2_img)
        card_2.place(x=900, y=200)
        score_img_lbl = Label(tree_grow, image=score_bg_img, font=("Rye", 25))
        score_img_lbl.place(x=1000, y=45)

        user_tree_lbl = Label(tree_grow, text="Trees: " + str(user_tree), font=("Rye", 30), bg="#e2a757", fg="white")
        user_tree_lbl.place(x=1020, y=45)

        rounds_img = Label(tree_grow, image=rounds_lbl_img)
        rounds_img.place(x=600, y=38)

        rounds_lbl = Label(tree_grow, text="Rounds: " + str(rounds), font=("Rye", 30), bg="#e2a757", fg="white")
        rounds_lbl.place(x=650, y=40)

        number_1 = random.randint(1, 13)

        num1_lbl = Label(tree_grow, text=number_1, font=("Rye", 150), bg="#e2a757", fg="white")
        num1_lbl.place(x=400, y=210)

        higher_btn = Button(tree_grow, text='Higher', font=('Rye', 15), bg='white', fg='black', command=higher,
                            image=higher_btn_img)
        higher_btn.place(x=50, y=530)

        lower_btn = Button(tree_grow, text='Lower', font=('Arial', 15), bg='white', fg='black', command=lower,
                           image=lower_btn_img)
        lower_btn.place(x=1015, y=530)

        equal_btn = Button(tree_grow, text='Equal', font=('Arial', 15), bg='white', fg='black', command=equal,
                           image=equal_btn_img)
        equal_btn.place(x=530, y=530)

        reveal_btn = Button(tree_grow, text='Reveal', font=('Arial', 15), bg='white', fg='black', command=reveal,
                            image=reveal_btn_img)
        reveal_btn.place(x=530, y=730)

        reveal_btn['state'] = "disable"

        plant_tree_btn = Button(tree_grow, font=('Arial', 15), bg='white', fg='black',
                                image=plant_trees_img, command=plant_trees)
        plant_tree_btn.place(x=1200, y=800)

    else:
        messagebox.showerror("NEGATIVE TREES", "INSUFFICIENT TREES. PLEASE QUIT!")
        tree_grow.destroy()


def higher():
    global number_2, number_1, user_tree, user_tree_lbl, higher_btn, rounds_lbl, reveal_btn, lower_btn, equal_btn, wrong_lbl, correct_lbl, win, status

    number_2 = random.randint(1, 13)
    reveal_btn['state'] = "active"
    higher_btn['state'] = "disable"
    lower_btn['state'] = "active"
    equal_btn['state'] = "active"

    if number_1 == number_2:
        print("TIE -1 TREE")
        user_tree -= 1
        wrong_lbl = Label(tree_grow, image=wrong_img)

    elif number_1 < number_2:
        print("CORRECT +1 TREE")
        pygame.mixer.music.load('MONEY SOUND EFFECT !!.mp3')
        pygame.mixer.music.play(loops=0)
        user_tree += 1
        win = 1
        status = Label(tree_grow, image=correct_img)

    else:
        print("LOWER -1 TREE")
        user_tree -= 1
        status = Label(tree_grow, image=wrong_img)


def lower():
    global number_1, number_2, user_tree, user_tree_lbl, wrong_lbl, correct_lbl, win, status

    number_2 = random.randint(1, 13)
    reveal_btn['state'] = "active"
    higher_btn['state'] = "active"
    lower_btn['state'] = "disable"
    equal_btn['state'] = "active"

    if number_1 == number_2:
        print("TIE -1 TREE")
        user_tree -= 1

        status = Label(tree_grow, image=wrong_img)

    elif number_1 < number_2:
        print("HIGHER -1 TREE")
        user_tree -= 1

        status = Label(tree_grow, image=wrong_img)

    else:
        print("CORRECT +1 TREE")
        pygame.mixer.music.load('MONEY SOUND EFFECT !!.mp3')
        pygame.mixer.music.play(loops=0)
        user_tree += 1
        win = 1

        status = Label(tree_grow, image=correct_img)


def equal():
    global number_1, number_2, user_tree, user_tree_lbl, wrong_lbl, correct_lbl, win, status

    number_2 = random.randint(1, 13)
    reveal_btn['state'] = "active"
    higher_btn['state'] = "active"
    lower_btn['state'] = "active"
    equal_btn['state'] = "disable"

    if number_1 == number_2:
        print("CORRECT +3 TREES")
        user_tree += 3
        pygame.mixer.music.load('MONEY SOUND EFFECT !!.mp3')
        pygame.mixer.music.play(loops=0)

        status = Label(tree_grow, image=correct_img)

        win = 1

    elif number_1 < number_2:
        print("HIGHER -3 TREES")
        user_tree -= 3

        status = Label(tree_grow, image=wrong_img)

    else:
        print("LOWER -3 TREES")
        user_tree -= 3

        status = Label(tree_grow, image=wrong_img)


def reveal():
    global number_1, number_2, num2_lbl, user_tree_lbl, rounds, rounds_lbl, wrong_lbl, correct_lbl, next_btn, win, status

    num2_lbl = Label(tree_grow, text=number_2, bg="#e2a757", font=("Rye", 150), fg="white")
    num2_lbl.place(x=1000, y=210)

    rounds += 1
    rounds_lbl['text'] = "Rounds:" + str(rounds)
    user_tree_lbl['text'] = "Trees: " + str(user_tree)


    next_btn = Button(tree_grow, text="Next", font=('Arial', 15), bg='white', fg='black', command=next_round,
                      image=next_btn_img)
    next_btn.place(x=1200, y=750)

    status.place(x=700, y=325)


def next_round():
    global rounds, user_tree, user_tree_lbl, number_2, lower_btn, next_btn, win
    num2_lbl.place_forget()
    next_btn.place_forget()
    play_game()
    higher_btn['state'] = "active"
    lower_btn['state'] = "active"
    equal_btn['state'] = "active"
    status.place_forget()


def plant_trees():
    global user_tree, frame_0, trees_planted

    frame_0 = LabelFrame(tree_grow)
    frame_0.place(x=0, y=0)



    if 0 <= user_tree <= 5:
        trees_planted = Label(tree_grow, image=trees1)
        trees_planted.place(x=0, y=0)
        print(5)
    elif 5 <= user_tree <= 10:
        trees_planted = Label(tree_grow, image=trees2)
        trees_planted.place(x=0, y=0)
        print(10)
    elif 10 <= user_tree <= 15:
        trees_planted = Label(tree_grow, image=trees3)
        trees_planted.place(x=0, y=0)
        print(15)
    elif 15 <= user_tree <= 20:
        trees_planted = Label(tree_grow, image=trees4)
        trees_planted.place(x=0, y=0)
        print(20)

    message = Label(tree_grow, font=('Rye', 80), fg="#e2a757", text="You planted: " + str(user_tree))
    message.place(x=100, y=100)
def exit_game():
    tree_grow.destroy()


game_start()

tree_grow.mainloop()
