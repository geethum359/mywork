from tkinter import*
win=Tk()
win.geometry("550x550")
lb1=Label(win,text="First Name").grid(row=1,column=2,padx=(30, 0), pady=(10, 0))
txt1=Entry( win,width=20).grid(row=1,column=3,padx=(30, 0), pady=(10, 0))

lb2=Label(win,text="Last Name",).grid(row=2,column=2,padx=(30, 0), pady=(10, 0))
txt2=Entry( win,width=20).grid(row=2,column=3,padx=(30, 0), pady=(10, 0))

lbl3=Label(win,text="Gender",).grid(row=3,column=2,padx=(30, 0), pady=(5, 0))
rad1=Radiobutton(win,text="Male",value=1).grid(row=3,column=3)
rad2=Radiobutton( win,text="Female",value=2).grid(row=3,column=4)
rad3=Radiobutton( win,text="Others",value=2).grid(row=3,column=5)

lb4=Label(win,text="Address",).grid(row=4,column=2,padx=(30, 0), pady=(10, 0))
txt4=Entry(win,width=20).grid(row=4,column=3,padx=(30, 0), pady=(10, 0))

lb5=Label( win,text="City",).grid(row=5,column=2,padx=(30, 0), pady=(10, 0))
txt5=Entry( win,width=20).grid(row=5,column=3,padx=(30, 0), pady=(10, 0))

lb6=Label( win,text="Pincod",).grid(row=5,column=4,padx=(30, 0), pady=(10, 0))
txt6=Entry(win,width=20).grid(row=5,column=5,padx=(30, 0), pady=(10, 0))

lb7=Label( win,text="Phone No",).grid(row=6,column=2,padx=(30, 0), pady=(10, 0))
txt7=Entry(win,width=20).grid(row=6,column=3,padx=(30, 0), pady=(10, 0))

lb8=Label( win,text="Email",).grid(row=6,column=4,padx=(30, 0), pady=(10, 0))
txt8=Entry(win,width=20).grid(row=6,column=5,padx=(30, 0), pady=(10, 0))

lb9=Label(win,text="Hobbies").grid(row=7,column=4,padx=(30, 0), pady=(10, 0))
chk1=Checkbutton(win,text="Reading").grid(row=10,column=5)
chk1=Checkbutton(win,text="Sketing").grid(row=10,column=5)
chk1=Checkbutton(win,text="Cooking").grid(row=10,column=5)
win.mainloop()