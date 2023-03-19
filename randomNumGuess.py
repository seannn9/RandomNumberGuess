from tkinter import *
import random
import os

window = Tk()
window.geometry("300x300")
window.title("RNG ")
window.resizable(False, False)

score = 0
f = open("C:\\Users\\naesk\\Downloads\\history.txt", "a")

def reset_button():
    score = 0
    l3.config(text=f"Tries: {score}", fg="dark red")
    l1.config(text="")
    b1.config(text="Submit",command=game_start, bg="grey", fg="black")

def scoring_system():
    global score
    score += 1
    l3.config(text=f"Tries: {score}", fg="dark red")

def game_start():
    scoring_system()
    num = int(e1.get())
    for i in range(1, 100):
        if num < to_guess:
            e1.delete(0, END)
            l1.config(text=f"{num}: Higher", fg="red")
        elif num > to_guess:
            e1.delete(0, END)
            l1.config(text=f"{num}: Lower", fg="blue")              
        elif num == to_guess:
            e1.delete(0,END)
            l1.config(text=f"{num}: Correct!", fg="green")
            b1.config(text="Reset", fg="red", bg="black", command=reset_button)
            break

def show_history():
    f.write(f"{e1.get()}")

game_title_font = ("Comic Sans MS",  15 , "bold")
game_title = Label(window, text="Random Number Guessing", font=game_title_font, fg="dark orange")
game_title.pack()

l1 = Label(window, text="", font=game_title_font, bg="white", width=15, borderwidth=2, relief="solid")
l1.pack(padx=10, pady=20)

l2 = Label(window, text="Enter a number between 1 and 1,000:", font="Roboto 12")
l2.pack(pady=10)

e1 = Entry(window)
e1.pack()

to_guess = random.randint(1, 1000)
b1 = Button(window, text="Submit", bg="grey", command=game_start)
b1.pack(pady=10)

l3 = Label(window, text="Tries:", font=game_title_font, fg="dark red")
l3.pack(pady=10)

b2 = Button(window, text="Show guesses", bg="grey", command=show_history)
b2.pack(pady=0.5)


window.mainloop()