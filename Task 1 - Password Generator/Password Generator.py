from tkinter import *
from tkinter.font import Font

def generate(datal,datac):
    import string
    import random

    alphabets = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = list(string.punctuation)
    symbols.remove("'")
    symbols.remove('"')
    symbols.remove("`")
    
    password = []
    temp=[]
    temp+=alphabets+numbers+symbols
    if datac=="strong" or datac=="Strong" or datac=="STRONG":
        for k in range(1,int(datal)+1):
            password.append(random.choice(temp))
        random.shuffle(password)
    elif datac=="weak" or datac=="Weak" or datac=="WEAK":
        temp=alphabets
        for k in range(1,int(datal)+1):
            password.append(random.choice(temp))
    
    ans = "".join(password)
    return ans

count = 0

def submit1():
    global count
    datal = length.get()
    datac = complexity.get()
    if datal!="" and datac!="":
        answer = generate(datal,datac)
        count+=1
        if count==1:
            global lab
            lab = Label(dbox,text=answer,font=("times",17,"bold"),pady=50,fg="white",bg="cornflowerblue")
        else:
            lab.config(text=answer)
        lab.pack()
       

def clear1():
    lab.destroy()
    length.delete(0,END)
    complexity.delete(0,END)
    length.focus_set()
    global count
    count=0
    
    
    
dbox = Tk()
width = 500
height = 500
screenwidth = dbox.winfo_screenwidth()
screenheight = dbox.winfo_screenheight()
reqwidth = (screenwidth/2)-(width/2)
reqheight = (screenheight/2)-(height/2)

dbox.geometry("%dx%d+%d+%d" %(width,height,reqwidth,reqheight))
dbox.title("Password Generator")
dbox.iconbitmap("favicon.ico")
dbox.resizable("False","False")
dbox.config(bg="cornflowerblue")
mfont = Font(family="times",size=19)
lb = Label(dbox,text="Enter the length of the Password : ",font=mfont,pady=30,bg="cornflowerblue")
lb.pack()

length = Entry(dbox,width=30,font=("times",13))
length.pack()
length.focus_set()

lb1 = Label(dbox,text="Enter the complexity of the Password\n(Weak or Strong) : ",font=mfont,pady=30,bg="cornflowerblue")
lb1.pack()

complexity = Entry(dbox,width=30,font=("times",13))
complexity.pack()

submit = Button(dbox,text="Submit",font=("times",16,"bold"),bg="green",fg="white",width=10,command=submit1)
submit.pack(side=RIGHT)

clear = Button(dbox,text="Clear",font=("times",16,"bold"),bg="red",fg="white",width=10,command=clear1)
clear.pack(side=LEFT)




dbox.mainloop()
