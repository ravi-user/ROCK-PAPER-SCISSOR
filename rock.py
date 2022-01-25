from ast import Str
from tkinter import * 
from random import * 

screen = Tk() 

screen.geometry("500x500")
screen.config(bg="#F57F17")
screen.title("ROCK PAPER SCISSOR GAME")

# begin  -------------- GAME LOGIC ----------------

game_list = ["ROCK","PAPER","SCISSOR"]

user_choice_var = StringVar()
computer_choice_var = StringVar()
result_var = StringVar()

user_score_var = IntVar()
comp_score_var = IntVar()

u_score = 0 
c_score = 0
def mygame(userchoice):
    global u_score,c_score
    
    computer_chocie = choice(game_list)
    

    user_choice_var.set(userchoice)
    computer_choice_var.set(computer_chocie)


    if userchoice == "ROCK" and computer_chocie == "PAPER":
        result_var.set(" COMPUTER WON ")
        c_score += 1
    elif userchoice == "ROCK" and computer_chocie == "SCISSOR":
        result_var.set(" USER WON ")
        u_score += 1
    elif userchoice == "PAPER" and computer_chocie == "ROCK":
        result_var.set(" USER WON ")
        u_score += 1
    elif userchoice == "PAPER" and computer_chocie == "SCISSOR":
        result_var.set(" COMPUTER WON ")
        c_score += 1
    elif userchoice == "SCISSOR" and computer_chocie == "ROCK":
        result_var.set(" COMPUTER WON ")
        c_score += 1
    elif userchoice == "SCISSOR" and computer_chocie == "PAPER":
        result_var.set(" USER WON ")
        u_score += 1
    else:
        result_var.set(" TIE ")

    user_score_var.set(u_score)
    comp_score_var.set(c_score)

# End  -------------- GAME LOGIC ----------------

lbl = Label(screen,text="Welcome to rock paper scissor",font=('arial',18,'bold'),bg="#F57F17",fg="black")
lbl.pack()

btn_rock = Button(screen,text="ROCK",font=('arial',18,'bold'),bg="black",fg="yellow",command=lambda:mygame("ROCK"))
btn_rock.place(x = 50,y = 100)


btn_rock = Button(screen,text="PAPER",font=('arial',18,'bold'),bg="black",fg="yellow",command=lambda:mygame("PAPER"))
btn_rock.place(x = 200,y = 100)


btn_rock = Button(screen,text="SCISSOR",font=('arial',18,'bold'),bg="black",fg="yellow",command=lambda:mygame("SCISSOR"))
btn_rock.place(x = 350,y = 100)

# ------ user display ----
lbl_user = Label(screen,text="USER",font=('arial',16,'bold'),bg="#F57F17",fg="black")
lbl_user.place(x=50, y=200)

lbl_user_selection = Label(screen,textvariable=user_choice_var,font=('arial',16,'bold'),bg="#F57F17",fg="black")
lbl_user_selection.place(x=200, y=200)

lbl_user_score = Label(screen,textvariable=user_score_var,font=('arial',16,'bold'),bg="#F57F17",fg="black")
lbl_user_score.place(x=350, y=200)
# ------ user display ----


# ------ computer display ----
lbl_computer = Label(screen,text="COMPUTER",font=('arial',16,'bold'),bg="#F57F17",fg="black")
lbl_computer.place(x=50, y=250)

lbl_computer_selection = Label(screen,textvariable=computer_choice_var,font=('arial',16,'bold'),bg="#F57F17",fg="black")
lbl_computer_selection.place(x=200, y=250)

lbl_computer_score = Label(screen,textvariable=comp_score_var,font=('arial',16,'bold'),bg="#F57F17",fg="black")
lbl_computer_score.place(x=350, y=250)
# ------ computer display ----


# ------ result display ----- 

btn_result = Button(screen,textvariable=result_var,font=('arial',18,'bold'),bg="black",fg="yellow",height=3,width=25)
btn_result.place(x = 70,y = 350)

# ------ result display ----- 



screen.mainloop()

