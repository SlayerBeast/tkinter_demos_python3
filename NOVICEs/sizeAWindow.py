#!/bin/python3

#problem:	say if we want to create a login window,
#we want to make sure that the size of the window is
#400* 600,how to make this?

#solution:	use the width and height keyword argument to set
#that for you.

import tkinter as tk

root=tk.Tk()

#root.pack(fill=tk.BOTH)
loginFrame=tk.Frame(root)
loginFrame.config(width=340,height=600)
loginFrame.pack(fill=tk.BOTH,expand=1)
#loginFrame=tk.Frame(root)

nameLabel=tk.Label(loginFrame,text="name")
passLabel=tk.Label(loginFrame,text="password")
loginButton=tk.Button(loginFrame,text="login")
nameEntry=tk.Entry(loginFrame)
passEntry=tk.Entry(loginFrame,show='*')


#start to pack them
nameLabel.grid(row=0,column=0)
nameEntry.grid(row=0,column=1)
passLabel.grid(row=1)
passEntry.grid(row=1,column=1)
loginButton.grid(row=2,columnspan=2,sticky="ew")


loginFrame.grid_propagate(False)

root.mainloop()

