from tkinter import *
tic = Tk()
tic.geometry("330x315")
tic.configure(background = "black")
tic.resizable(0,0)

# Button1
def bton1(event):
        lable = Label(tic,text='o',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=1,column=1)
def btoon1(event):
        lable = Label(tic,text='x',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=1,column=1)
btn1 = Button(padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2, command=bton1)
btn1.bind("<Button-3>",bton1)
btn1.bind("<Button-1>",btoon1)
btn1.grid(row=1,column=1)

# Button2

def bton2(event):
        lable = Label(tic,text='o',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=1,column=2)
def btoon2(event):
        lable = Label(tic,text='x',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=1,column=2)
btn2 = Button(padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2, command=bton2)
btn2.bind("<Button-3>",bton2)
btn2.bind("<Button-1>",btoon2)
btn2.grid(row=1,column=2)

#Button3

def bton3(event):
        lable = Label(tic,text='o',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=1,column=3)
def btoon3(event):
        lable = Label(tic,text='x',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=1,column=3)
btn3 = Button(padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2, command=bton3)
btn3.bind("<Button-3>",bton3)
btn3.bind("<Button-1>",btoon3)
btn3.grid(row=1,column=3)

# Button4
def bton4(event):
        lable = Label(tic,text='o',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=2,column=1)
def btoon4(event):
        lable = Label(tic,text='x',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=2,column=1)
btn4 = Button(padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2, command=bton4)
btn4.bind("<Button-3>",bton4)
btn4.bind("<Button-1>",btoon4)
btn4.grid(row=2,column=1)

# Button5

def bton5(event):
        lable = Label(tic,text='o',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=2,column=2)
def btoon5(event):
        lable = Label(tic,text='x',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=2,column=2)
btn5 = Button(padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2, command=bton5)
btn5.bind("<Button-3>",bton5)
btn5.bind("<Button-1>",btoon5)
btn5.grid(row=2,column=2)

#Button6

def bton6(event):
        lable = Label(tic,text='o',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=2,column=3)
def btoon6(event):
        lable = Label(tic,text='x',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=2,column=3)
btn6 = Button(padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2, command=bton6)
btn6.bind("<Button-3>",bton6)
btn6.bind("<Button-1>",btoon6)
btn6.grid(row=2,column=3)

# Button7
def bton7(event):
        lable = Label(tic,text='o',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=3,column=1)
def btoon7(event):
        lable = Label(tic,text='x',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=3,column=1)
btn7 = Button(padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2, command=bton7)
btn7.bind("<Button-3>",bton7)
btn7.bind("<Button-1>",btoon7)
btn7.grid(row=3,column=1)

# Button8

def bton8(event):
        lable = Label(tic,text='o',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=3,column=2)
def btoon8(event):
        lable = Label(tic,text='x',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=3,column=2)
btn8 = Button(padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2, command=bton8)
btn8.bind("<Button-3>",bton8)
btn8.bind("<Button-1>",btoon8)
btn8.grid(row=3,column=2)

#Button9

def bton9(event):
        lable = Label(tic,text='o',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=3,column=3)
def btoon9(event):
        lable = Label(tic,text='x',padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2)
        lable.grid(row=3,column=3)
btn9 = Button(padx=20,pady=1,bg = 'black',fg='white',font='verdan 40',width=2, command=bton9)
btn9.bind("<Button-3>",bton9)
btn9.bind("<Button-1>",btoon9)
btn9.grid(row=3,column=3)

tic.mainloop()