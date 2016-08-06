#!/bin/python3

#problem:	say if we want to create a login window,
#we want to make sure that the size of the window is
#400* 600,how to make this?

#solution:	use the width and height keyword argument to set
#that for you.

import tkinter as tk

root=tk.Tk()

root.config(width=400,height=600)
loginFrame=tk.Frame(root)
loginFrame.grid()

root.mainloop()

