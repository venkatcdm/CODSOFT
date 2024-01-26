from tkinter import *
from PIL import Image, ImageTk



def click1():
    global lab
    lab = Label(dbox,text="You\nchose",fg="blue",font=("times",14))
    lab.grid(row=4,column=1)
    b2['state'] = DISABLED
    b3['state'] = DISABLED
    proceed['state'] = NORMAL
    global user
    user = b1.cget("text")

def click2():
    global lab
    lab = Label(dbox,text="You\nchose",fg="blue",font=("times",14))
    lab.grid(row=4,column=2)
    b1['state'] = DISABLED
    b3['state'] = DISABLED
    proceed['state'] = NORMAL
    global user
    user = b2.cget("text")

def click3():
    global lab
    lab = Label(dbox,text="You\nchose",fg="blue",font=("times",14))
    lab.grid(row=4,column=3)
    b2['state'] = DISABLED
    b1['state'] = DISABLED
    proceed['state'] = NORMAL
    global user
    user = b3.cget("text")

def reset1():
    global lab1
    global lb1
    lb1.destroy()
    global tb
    tb.config(text="Choose any one")
    global reset
    reset.destroy()
    global proceed
    proceed =  Button(dbox,text="Proceed",width=7,borderwidth=0,bg="green",fg="white",font=("times",16,"bold"),activebackground="#008631",command=proceed1,state=DISABLED)
    proceed.grid(row=5,column=2,pady=60)
    b1['state'] = NORMAL
    b2['state'] = NORMAL
    b3['state'] = NORMAL
    global answer
    answer.destroy()
    global lab
    lab.destroy()
    lab1.destroy()
    
    
    
    
    

def proceed1():
    global tb
    tb.config(text="")
    global lb1
    lb1 = Label(dbox,text="COMPUTER'S\n TURN",bg="white",font=("times",15,"bold"),padx=30)
    lb1.grid(row=0,column=2)
    proceed.destroy()
    global user
    game()

global lab1
def game():
    import random
    global user
    global lab
    global lab1
    lab1 = Label(dbox,text="Computer\nchose",fg="blue",font=("times",14))
    options = ['ROCK','PAPER','SCISSOR']
    computerchoice = random.choice(options)
    if user==computerchoice:
        lab.config(text="Both chose")
    elif computerchoice==options[0]:
        lab1.grid(row=4,column=1)
    elif computerchoice==options[1]:
        lab1.grid(row=4,column=2)
    elif computerchoice==options[2]:
        lab1.grid(row=4,column=3)
    global answer
    answer = Label(dbox,text="",font=("Helvetica",18,"bold"),fg="#8B4000",bg="white")
    answer.grid(row=5,column=2,pady=50)
    
    
    if user=="ROCK":
        if computerchoice=="ROCK":
            answer.config(text="TIE")
        elif computerchoice=="PAPER":
            answer.config(text="YOU LOSE")
            answer.config(fg="red")
        else:
            answer.config(text="YOU WIN")
            answer.config(fg="green")
            
    elif user=="PAPER":
        if computerchoice=="ROCK":
            answer.config(text="YOU WIN")
            answer.config(fg="green")
        elif computerchoice=="PAPER":
            answer.config(text="TIE")
        else:
            answer.config(text="YOU LOSE")
            answer.config(fg="red")
            
    elif user=="SCISSOR":
        if computerchoice=="ROCK":
            answer.config(text="YOU LOSE")
            answer.config(fg="red")
        elif computerchoice=="PAPER":
            answer.config(text="YOU WIN")
            answer.config(fg="green")
        else:
            answer.config(text="TIE")        
            
    global reset
    reset = Button(dbox,text="PLAY AGAIN",bg="#b70eff",fg="white",width=13,command=reset1,font=("times",10,"bold"))
    reset.grid(row=6,column=2)








dbox = Tk()
width = 430
height = 400
screenwidth = dbox.winfo_screenwidth()
screenheight = dbox.winfo_screenheight()
reqwidth = (screenwidth/2)-(width/2)
reqheight = (screenheight/2)-(height/2)
dbox.geometry("%dx%d+%d+%d" %(width,height,reqwidth,reqheight))
dbox.title("ROCK , PAPER , SCISSOR !")
dbox.iconbitmap("images/icon.ico")
dbox.config(bg="white")
dbox.resizable("False","False")


global lb
lb = Label(dbox,text="YOUR TURN",fg="black",bg="white",font=("times",15,"bold"),padx=30,pady=10)
lb.grid(row=0,column=2)

global tb
tb = Label(dbox,text="Choose any one",fg="black",bg="white",font=("times",15,"bold"),padx=30)
tb.grid(row=2,column=2)

i1= Image.open("images/rock.jpg")
resizedimage1 = i1.resize((110, 100))
r1 = ImageTk.PhotoImage(resizedimage1)


b1 = Button(dbox,text="ROCK",image=r1,width=110,pady=30,borderwidth=0,command=click1)
b1.grid(row=4,column=1,pady=20,padx=3)

i2= Image.open("images/paper.jpg")
resizedimage2 = i2.resize((110, 100))
r2 = ImageTk.PhotoImage(resizedimage2)

b2 = Button(dbox,text="PAPER",image=r2,width=110,pady=30,borderwidth=0,command=click2)
b2.grid(row=4,column=2,pady=20)

i3= Image.open("images/scissor.jpg")
resizedimage3 = i3.resize((110, 100))
r3 = ImageTk.PhotoImage(resizedimage3)

b3 = Button(dbox,text="SCISSOR",image=r3,width=110,pady=30,borderwidth=0,command=click3)
b3.grid(row=4,column=3,pady=20)

global proceed
proceed =  Button(dbox,text="Proceed",width=7,borderwidth=0,bg="green",fg="white",font=("times",16,"bold"),activebackground="#008631",command=proceed1,state=DISABLED)
proceed.grid(row=5,column=2,pady=60)


dbox.mainloop()