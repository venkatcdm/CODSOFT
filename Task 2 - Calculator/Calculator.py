from tkinter import *
from tkinter.font import Font

answer=""

def click1():
    global answer
    answer= b1.cget('text')
    if 'invalid' not in answer: 
        elab.insert(END, answer)
        elab.pack()
    add['state'] = NORMAL
    sub['state'] = NORMAL
    mul['state'] = NORMAL
    div['state'] = NORMAL
    
def click2():
    global answer
    answer= b2.cget('text')
    if 'invalid' not in answer: 
        elab.insert(END, answer)
        elab.pack()
    add['state'] = NORMAL
    sub['state'] = NORMAL
    mul['state'] = NORMAL
    div['state'] = NORMAL

def click3():
    global answer
    answer= b3.cget('text')
    if 'invalid' not in answer: 
        elab.insert(END, answer)
        elab.pack()
    add['state'] = NORMAL
    sub['state'] = NORMAL
    mul['state'] = NORMAL
    div['state'] = NORMAL

def click4():
    global answer
    answer= b4.cget('text')
    if 'invalid' not in answer: 
        elab.insert(END, answer)
        elab.pack()
    add['state'] = NORMAL
    sub['state'] = NORMAL
    mul['state'] = NORMAL
    div['state'] = NORMAL

def click5():
    global answer
    answer= b5.cget('text')
    if 'invalid' not in answer: 
        elab.insert(END, answer)
        elab.pack()
    add['state'] = NORMAL
    sub['state'] = NORMAL
    mul['state'] = NORMAL
    div['state'] = NORMAL

def click6():
    global answer
    answer= b6.cget('text')
    if 'invalid' not in answer: 
        elab.insert(END, answer)
        elab.pack()
    add['state'] = NORMAL
    sub['state'] = NORMAL
    mul['state'] = NORMAL
    div['state'] = NORMAL
    
def click7():
    global answer
    answer= b7.cget('text')
    if 'invalid' not in answer: 
        elab.insert(END, answer)
        elab.pack()
    add['state'] = NORMAL
    sub['state'] = NORMAL
    mul['state'] = NORMAL
    div['state'] = NORMAL
    
def click8():
    global answer
    answer= b8.cget('text')
    if 'invalid' not in answer: 
        elab.insert(END, answer)
        elab.pack()
    add['state'] = NORMAL
    sub['state'] = NORMAL
    mul['state'] = NORMAL
    div['state'] = NORMAL
    
def click9():
    global answer
    answer= b9.cget('text')
    if 'invalid' not in answer: 
        elab.insert(END, answer)
        elab.pack()
    add['state'] = NORMAL
    sub['state'] = NORMAL
    mul['state'] = NORMAL
    div['state'] = NORMAL
    
def click10():
    global answer
    answer= b10.cget('text')
    if 'invalid' not in answer: 
        elab.insert(END, answer)
        elab.pack()
    add['state'] = NORMAL
    sub['state'] = NORMAL
    mul['state'] = NORMAL
    div['state'] = NORMAL
    


def clickadd():
    global answer
    answer= add.cget('text')
    if 'invalid' not in answer: 
        elab.insert(END,'+')
    elab.pack()
    add['state'] = DISABLED
    sub['state'] = DISABLED
    mul['state'] = DISABLED
    div['state'] = DISABLED
    
def clicksub():
    global answer
    answer= sub.cget('text')
    if 'invalid' not in answer: 
        elab.insert(END, answer)
    elab.pack()
    add['state'] = DISABLED
    sub['state'] = DISABLED
    mul['state'] = DISABLED
    div['state'] = DISABLED
    
def clickmul():
    global answer
    answer= mul.cget('text')
    if 'invalid' not in answer: 
        elab.insert(END, answer)
    elab.pack()
    add['state'] = DISABLED
    sub['state'] = DISABLED
    mul['state'] = DISABLED
    div['state'] = DISABLED
    
def clickdiv():
    global answer
    answer= div.cget('text')
    if 'invalid' not in answer: 
        elab.insert(END, answer)
    elab.pack()
    add['state'] = DISABLED
    sub['state'] = DISABLED
    mul['state'] = DISABLED
    div['state'] = DISABLED
    
def clickdot():
    global answer
    answer= dot.cget('text')
    if 'invalid' not in answer: 
        elab.insert(END, answer)
        elab.pack()
   
def clickdelete():
    elab.delete(elab.index("end") - 1)
    
def clickac():
    elab.delete(0,END)
    add['state'] = NORMAL
    sub['state'] = NORMAL
    mul['state'] = NORMAL
    div['state'] = NORMAL
   
def clickequal():
    value = elab.get()
    clickac()
    if value!="":
        try:
            ans = eval(value)
        except:
            ans="invalid"
        elab.insert(0, str(ans))
        elab.pack()
    
    
                
dbox = Tk()
dbox.title("Calculator")
width = 380
height = 500
screenwidth = dbox.winfo_screenwidth()
screenheight = dbox.winfo_screenheight()
reqwidth = (screenwidth/2)-(width/2)
reqheight = (screenheight/2)-(height/2)
dbox.geometry("%dx%d+%d+%d" %(width,height,reqwidth,reqheight))

dbox.resizable("False","False")
dbox.iconbitmap("calculator.ico")
dbox.config(bg="#454545")

elab = Entry(dbox,width=50,bg="#A1A14C",fg="black",font=("times",50),insertbackground="white")
elab.pack(fill=X,padx=10,pady=30)
elab.focus_set()

b1 = Button(dbox,text="9",font=("times",20,"bold"),bg="#454545",fg="white",width="4",command=click1)
b1.place(x=20,y=150)

b2 = Button(dbox,text="8",font=("times",20,"bold"),bg="#454545",fg="white",width="4",command=click2)
b2.place(x=110,y=150)

b3 = Button(dbox,text="7",font=("times",20,"bold"),bg="#454545",fg="white",width="4",command=click3)
b3.place(x=200,y=150)

b4 = Button(dbox,text="6",font=("times",20,"bold"),bg="#454545",fg="white",width="4",command=click4)
b4.place(x=20,y=220)

b5 = Button(dbox,text="5",font=("times",20,"bold"),bg="#454545",fg="white",width="4",command=click5)
b5.place(x=110,y=220)

b6 = Button(dbox,text="4",font=("times",20,"bold"),bg="#454545",fg="white",width="4",command=click6)
b6.place(x=200,y=220)

b7 = Button(dbox,text="3",font=("times",20,"bold"),bg="#454545",fg="white",width="4",command=click7)
b7.place(x=20,y=290)

b8 = Button(dbox,text="2",font=("times",20,"bold"),bg="#454545",fg="white",width="4",command=click8)
b8.place(x=110,y=290)

b9 = Button(dbox,text="1",font=("times",20,"bold"),bg="#454545",fg="white",width="4",command=click9)
b9.place(x=200,y=290)

b10 = Button(dbox,text="0",font=("times",20,"bold"),bg="#454545",fg="white",width="4",command=click10)
b10.place(x=20,y=360)

delete = Button(dbox,text="DEL",font=("times",20,"bold"),bg="orange",fg="white",width="4",command=clickdelete)
delete.place(x=200,y=430)

ac = Button(dbox,text="AC",font=("times",20,"bold"),bg="red",fg="white",width="4",command=clickac)
ac.place(x=290,y=430)

add = Button(dbox,text="+",font=("times",19,"bold"),bg="#454545",fg="white",width="4",command=clickadd)
add.place(x=290,y=150)

sub = Button(dbox,text="-",font=("times",19,"bold"),bg="#454545",fg="white",width="4",command=clicksub)
sub.place(x=290,y=220)

mul = Button(dbox,text="*",font=("times",19,"bold"),bg="#454545",fg="white",width="4",command=clickmul)
mul.place(x=290,y=290)

div = Button(dbox,text="/",font=("times",19,"bold"),bg="#454545",fg="white",width="4",command=clickdiv)
div.place(x=290,y=360)

equal = Button(dbox,text="=",font=("times",20,"bold"),bg="#454545",fg="white",width="4",command=clickequal)
equal.place(x=110,y=360)

dot = Button(dbox,text=".",font=("times",20,"bold"),bg="#454545",fg="white",width="4",command=clickdot)
dot.place(x=200,y=360)

dbox.mainloop()