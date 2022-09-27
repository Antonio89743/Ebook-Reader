
# Python program to illustrate the usage of 
# autohiding scrollbars using tkinter
   
# Importing tkinter
from tkinter import *
   
# Creating class AutoScrollbar
class AutoScrollbar(Scrollbar):
       
    # Defining set method with all 
    # its parameter
    def set(self, low, high):
           
        if float(low) <= 0.0 and float(high) >= 1.0:
               
            # Using grid_remove
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        Scrollbar.set(self, low, high)
       
    # Defining pack method
    def pack(self, **kw):
           
        # If pack is used it throws an error
        raise (TclError,"pack cannot be used with \
        this widget")
       
    # Defining place method
    def place(self, **kw):
           
        # If place is used it throws an error
        raise (TclError, "place cannot be used  with \
        this widget")
  
# creating tkinter window 
root = Tk()
   
# Defining vertical scrollbar
verscrollbar = AutoScrollbar(root)
   
# Calling grid method with all its
# parameter w.r.t vertical scrollbar
verscrollbar.grid(row=0, column=1, 
                  sticky=N+S)
   
# Defining horizontal scrollbar
horiscrollbar = AutoScrollbar(root, 
                              orient=HORIZONTAL)
   
# Calling grid method with all its 
# parameter w.r.t horizontal scrollbar
horiscrollbar.grid(row=1, column=0, 
                   sticky=E+W)
   
# Creating scrolled canvas
canvas = Canvas(root,
                yscrollcommand=verscrollbar.set,
                xscrollcommand=horiscrollbar.set)
  
canvas.grid(row=0, column=0, sticky=N+S+E+W)
   
verscrollbar.config(command=canvas.yview)
horiscrollbar.config(command=canvas.xview)
   
# Making the canvas expandable
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
   
# creating canvas contents
frame = Frame(canvas)
frame.rowconfigure(1, weight=1)
frame.columnconfigure(1, weight=1)
   
# Defining number of rows and columns
rows = 20
for i in range(1,rows):
    for j in range(1,9):
        button = Button(frame, padx=8, pady=8, 
                        text="[%d,%d]" % (i,j))
        button.grid(row=i, column=j, sticky='news')
  
# Creating canvas window
canvas.create_window(0, 0, anchor=NW, window=frame)
   
# Calling update_idletasks method
frame.update_idletasks()
   
# Configuring canvas
canvas.config(scrollregion=canvas.bbox("all"))
   
# Calling mainloop method
root.mainloop()