from tkinter import *
from functools import partial

from tkinter.ttk import *

win= Tk()

win.geometry("400x250")

def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(win)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("500x450")
 
    # A Label widget to show in toplevel
    lbl=Label( newWindow,text="Signup",font=("Arial Bold",20)).grid(row=0,column=1,padx=(50, 0))

    lbl1=Label( newWindow,text="Fist name:",).grid(row=1,column=2,padx=(30, 0), pady=(10, 0))
    txt1=Entry( newWindow,width=20).grid(row=1,column=3,padx=(30, 0), pady=(10, 0))

    lbl2=Label(newWindow,text="Last name:",).grid(row=2,column=2,padx=(30, 0), pady=(10, 0))
    txt2=Entry( newWindow,width=20).grid(row=2,column=3,padx=(30, 0), pady=(10, 0))

    lbl3=Label( newWindow,text="Age:",).grid(row=3,column=2,padx=(30, 0), pady=(10, 0))
    txt3=Entry( newWindow,width=20).grid(row=3,column=3,padx=(30, 0), pady=(10, 0))

    lbl4=Label( newWindow,text="Gender:",).grid(row=4,column=2,padx=(30, 0), pady=(10, 0))
    rad1=Radiobutton( newWindow,text="Male",value=1).grid(row=4,column=3,padx=(30, 0), pady=(10, 0))
    rad2=Radiobutton( newWindow,text="Female",value=2).grid(row=5,column=3,padx=(30, 0), pady=(10, 0))

    lbl5=Label( newWindow,text="City:",).grid(row=6,column=2,padx=(30, 0), pady=(10, 0))
    txt4=Entry( newWindow,width=20).grid(row=6,column=3,padx=(30, 0), pady=(10, 0))

    lbl6=Label( newWindow,text="Address:",).grid(row=7,column=2,padx=(30, 0), pady=(10, 0))
    txt5=Entry( newWindow,width=20).grid(row=7,column=3,padx=(30, 0), pady=(10, 0))

    lbl7=Label( newWindow,text="User name:",).grid(row=8,column=2,padx=(30, 0), pady=(10, 0))
    txt6=Entry( newWindow,width=20).grid(row=8,column=3,padx=(30, 0), pady=(10, 0))

    lbl8=Label( newWindow,text="Password:",).grid(row=9,column=2,padx=(30, 0), pady=(10, 0))
    txt7=Entry( newWindow,width=20).grid(row=9,column=3,padx=(30, 0), pady=(10, 0))
    lbl9=Label( newWindow,text="Verify password:",).grid(row=10,column=2,padx=(30, 0), pady=(10, 0))
    txt8=Entry( newWindow,width=20).grid(row=10,column=3,padx=(30, 0), pady=(10, 0))



def clear_text():
    text.delete(0, END)
    text1.delete(0,END)

def login(name,password):
    print("username entered :", name.get())
    print("password entered :", password.get())

name = StringVar()
password=StringVar()

lb=Label(win,text="Login",font=("Arial Bold",20)).grid(row=0,column=2)

lbl=Label(win,text="username:").grid(row=1,column=1)
text= Entry(win,textvariable=name, width=40)
text.grid(row=1,column=2)

lb1=Label(win,text="password:").grid(row=2,column=1)
text1= Entry(win,textvariable=password, width=40)
text1.grid(row=2,column=2)

login=partial(login, name, password)

Button(win,text="Clear", command=clear_text).grid(row=4,column=2)
Button(win,text="login", command=login).grid(row=4,column=1)

Button(win,text ="Click siout",command = openNewWindow).grid(row=0,column=2)


win.mainloop()