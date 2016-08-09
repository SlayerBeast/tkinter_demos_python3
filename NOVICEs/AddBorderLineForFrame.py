#!/bin/python3

#PROBlEM:
#   now we have a frame inside a window,to make it clearer,we want to add
#border lines that containing the frame.How?


#SOLUTION:

import tkinter as tk

root=tk.Tk()
root.config(width=340,height=520)

loginFrame=tk.Frame(root)
loginFrame.place(anchor="center",relx=0.5,rely=0.5)
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

#this turns off the ultilization

root.mainloop()

