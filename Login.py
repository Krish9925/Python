from tkinter import *

def getvals():
    a = uservalue.get()
    print(uservalue.get())
    b = passvalue.get()
    c = 9925
    if(b == c):
                lable = Label(root,text='welcome',bg='black',fg='#90EE90',font='verdan 40')
                lable.grid(row=5,column=1)
    else:
        lable = Label(root,text='Opps',fg='red',bg='black',font='verdan 40')
        lable.grid(row=5,column=1)
        lable = Label(root,text='Wrong Password',fg='red',bg='black',font='verdan 30')
        lable.grid(row=6,column=1)
root = Tk()

root.geometry("500x310")
root.title('LOGIN PAGE')
root.configure(background = "black")
user = Label(root, text="Username",padx=10,pady=15,bg='black',fg='white',font='verdan 20' )
password = Label(root, text="Password",padx=10,pady=15,bg='black',fg='white',font='verdan 20')
user.grid()
password.grid()

uservalue = StringVar()
passvalue = IntVar()


userentry = Entry(root,textvariable=uservalue,width='20',font='verdan 20')
userentry.grid(row=0,column=1)
passentry = Entry(root,textvariable=passvalue,width='20',font='verdan 20')
passentry.grid(row=1,column=1)
passentry.bind("<Return>",getvals)

btn = Button(text = "SUBMIT",padx=56,pady=1,bg = 'black',fg='white',font='verdan 20', command=getvals)
btn.grid(row=3,column=1)
root.mainloop()
