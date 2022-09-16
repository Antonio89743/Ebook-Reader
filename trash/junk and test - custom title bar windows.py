# where should the app open on screen?

# import tkinter as tk
# from ctypes import windll

# # --- constants --- (UPPER_CASE_NAMES)

# # title bar colors
# TITLE_FOREGROUND = "white"
# TITLE_BACKGROUND = "#2c2c2c"

# BUTTON_FOREGROUND = "white"
# BUTTON_BACKGROUND = TITLE_BACKGROUND
# BUTTON_FOREGROUND_HOVER = BUTTON_FOREGROUND
# BUTTON_BACKGROUND_HOVER = 'red'

# # window colors
# WINDOW_BACKGROUND = "white"
# WINDOW_FOREGROUND = "black"

# # --- classes --- (CamelCaseNames)

# class MyButton(tk.Button):

#     def __init__(self, master, text='x', command=None, **kwargs):
#         super().__init__(master, bd=0, font="bold", padx=5, pady=2, 
#                          fg=BUTTON_FOREGROUND, 
#                          bg=BUTTON_BACKGROUND,
#                          activebackground=BUTTON_BACKGROUND_HOVER,
#                          activeforeground=BUTTON_FOREGROUND_HOVER, 
#                          highlightthickness=0, 
#                          text=text,
#                          command=command)

#         self.bind('<Enter>', self.on_enter)
#         self.bind('<Leave>', self.on_leave)

#     def on_enter(self, event):
#         self['bg'] = BUTTON_BACKGROUND_HOVER

#     def on_leave(self, event):
#         self['bg'] = BUTTON_BACKGROUND

# class MyTitleBar(tk.Frame):

#     def __init__(self, master, *args, **kwargs):
#         super().__init__(master, relief='raised', bd=1, 
#                          bg=TITLE_BACKGROUND,
#                          highlightcolor=TITLE_BACKGROUND, 
#                          highlightthickness=0)

#         self.title_label = tk.Label(self, 
#                                     bg=TITLE_BACKGROUND, 
#                                     fg=TITLE_FOREGROUND)
                                    
#         self.set_title("Book Worm")

#         self.close_button = MyButton(self, text='x', command=master.destroy)
#         self.minimize_button = MyButton(self, text='-', command=self.on_minimize)
#         self.other_button = MyButton(self, text='#', command=self.on_other)
                         
#         self.pack(expand=True, fill='x')
#         self.title_label.pack(side='left')
#         self.close_button.pack(side='right')
#         self.minimize_button.pack(side='right')
#         self.other_button.pack(side='right')

#         self.bind("<ButtonPress-1>", self.on_press)
#         self.bind("<ButtonRelease-1>", self.on_release)
#         self.bind("<B1-Motion>", self.on_move)
        
#     def set_title(self, title):
#         self.title = title
#         self.title_label['text'] = title
        
#     def on_press(self, event):
#         self.xwin = event.x
#         self.ywin = event.y

#     def on_release(self, event):
#         self['bg'] = TITLE_BACKGROUND
#         self.title_label['bg'] = TITLE_BACKGROUND
        
#     def on_move(self, event):
#         x = event.x_root - self.xwin
#         y = event.y_root - self.ywin
#         self.master.geometry(f'+{x}+{y}')
        
#     def on_minimize(self):
#         print('TODO: minimize')
                
#     def on_other(self):
#         print('TODO: other')

# # --- functions ---

# # empty

# # --- main ---


# GWL_EXSTYLE = -20
# WS_EX_APPWINDOW = 0x00040000
# WS_EX_TOOLWINDOW = 0x00000080

# def set_appwindow(root):
#     hwnd = windll.user32.GetParent(root.winfo_id())
#     style = windll.user32.GetWindowLongPtrW(hwnd, GWL_EXSTYLE)
#     style = style & ~WS_EX_TOOLWINDOW
#     style = style | WS_EX_APPWINDOW
#     res = windll.user32.SetWindowLongPtrW(hwnd, GWL_EXSTYLE, style)
#     # re-assert the new window style
#     root.withdraw()
#     root.after(10, root.deiconify)

# root = tk.Tk()

# def main():
#     root.geometry("700x700")
#     root.wm_title("AppWindow Test")
#     button = tk.Button(root, text='Exit', command=root.destroy)
#     button.place(x=10, y=10)
#     root.overrideredirect(True)
#     root.after(10, set_appwindow, root)
    
# if __name__ == '__main__':
#     main()
# # root = tk.Tk()
# # turns off title bar, geometry
# root.overrideredirect(True)

# # set new geometry
# root.geometry('400x100+200+200')

# title_bar = MyTitleBar(root) 
# #title_bar.pack()  # it is inside `TitleBar.__init__()`

# # a canvas for the main area of the window
# window = tk.Canvas(root, bg=WINDOW_BACKGROUND, highlightthickness=0)

# # pack the widgets
# window.pack(expand=True, fill='both')

# root.mainloop()





#  RESIZABLE WINDOW



# import tkinter as tk

# #  set minimum size
# # expand greens up to the blues

# class FloatingWindow(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.overrideredirect(True)
#         self.center()

#         self.label = tk.Label(self, text="Grab one of the blue")
#         self.label.pack(side="top", fill="both", expand=True)

#         self.grip_se = tk.Label(self,bg='blue')
#         self.grip_se.place(relx=1.0, rely=1.0, anchor="se")
#         self.grip_se.bind("<B1-Motion>",lambda e, mode='se':self.OnMotion(e,mode))

#         self.grip_e = tk.Label(self,bg='green')
#         self.grip_e.place(relx=1.0, rely=0.5, anchor="e")
#         self.grip_e.bind("<B1-Motion>",lambda e, mode='e':self.OnMotion(e,mode))
        
#         self.grip_ne = tk.Label(self,bg='blue')
#         self.grip_ne.place(relx=1.0, rely=0, anchor="ne")
#         self.grip_ne.bind("<B1-Motion>",lambda e, mode='ne':self.OnMotion(e,mode))

#         self.grip_n = tk.Label(self,bg='green')
#         self.grip_n.place(relx=0.5, rely=0, anchor="n")
#         self.grip_n.bind("<B1-Motion>",lambda e, mode='n':self.OnMotion(e,mode))

#         self.grip_nw = tk.Label(self,bg='blue')
#         self.grip_nw.place(relx=0, rely=0, anchor="nw")
#         self.grip_nw.bind("<B1-Motion>",lambda e, mode='nw':self.OnMotion(e,mode))

#         self.grip_w = tk.Label(self,bg='green')
#         self.grip_w.place(relx=0, rely=0.5, anchor="w")
#         self.grip_w.bind("<B1-Motion>",lambda e, mode='w':self.OnMotion(e,mode))

#         self.grip_sw = tk.Label(self,bg='blue')
#         self.grip_sw.place(relx=0, rely=1, anchor="sw")
#         self.grip_sw.bind("<B1-Motion>",lambda e, mode='sw':self.OnMotion(e,mode))

#         self.grip_s = tk.Label(self,bg='green')
#         self.grip_s.place(relx=0.5, rely=1, anchor="s")
#         self.grip_s.bind("<B1-Motion>",lambda e, mode='s':self.OnMotion(e,mode))

#     def OnMotion(self, event, mode):
#         abs_x = self.winfo_pointerx() - self.winfo_rootx()
#         abs_y = self.winfo_pointery() - self.winfo_rooty()
#         width = self.winfo_width()
#         height= self.winfo_height()
#         x = self.winfo_rootx()
#         y = self.winfo_rooty()
        
#         if mode == 'se' and abs_x >0 and abs_y >0:
#                 self.geometry("%sx%s" % (abs_x,abs_y)
#                               )
                
#         if mode == 'e':
#             if height >0 and abs_x >0:
#                 self.geometry("%sx%s" % (abs_x,height)
#                               )
#         if mode == 'ne' and abs_x >0:
#                 y = y+abs_y
#                 height = height-abs_y
#                 if height >0:
#                     self.geometry("%dx%d+%d+%d" % (abs_x,height,
#                                                    x,y))
#         if mode == 'n':
#             height=height-abs_y
#             y = y+abs_y
#             if height >0 and width >0:
#                 self.geometry("%dx%d+%d+%d" % (width,height,
#                                                x,y))
            
#         if mode == 'nw':
#             width = width-abs_x
#             height=height-abs_y
#             x = x+abs_x
#             y = y+abs_y
#             if height >0 and width >0:
#                 self.geometry("%dx%d+%d+%d" % (width,height,
#                                                x,y))
#         if mode == 'w':
#             width = width-abs_x
#             x = x+abs_x
#             if height >0 and width >0:
#                 self.geometry("%dx%d+%d+%d" % (width,height,
#                                                x,y))
#         if mode == 'sw':
#             width = width-abs_x
#             height=height-(height-abs_y)
#             x = x+abs_x
#             if height >0 and width >0:
#                 self.geometry("%dx%d+%d+%d" % (width,height,
#                                                x,y))
#         if mode == 's':
#             height=height-(height-abs_y)
#             if height >0 and width >0:
#                 self.geometry("%dx%d+%d+%d" % (width,height,
#                                                x,y))
            
        
#     def center(self):
#         width = 300
#         height = 300
#         screen_width = self.winfo_screenwidth()
#         screen_height = self.winfo_screenheight()
#         x_coordinate = (screen_width/2) - (width/2)
#         y_coordinate = (screen_height/2) - (height/2)

#         self.geometry("%dx%d+%d+%d" % (width, height,
#                                        x_coordinate, y_coordinate))

# app=FloatingWindow()
# app.mainloop()



#  resizable corner



# import tkinter as tk
# from tkinter import ttk

# class Example(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self.floater = FloatingWindow(self)

# class FloatingWindow(tk.Toplevel):
#     def __init__(self, *args, **kwargs):
#         tk.Toplevel.__init__(self, *args, **kwargs)
#         self.overrideredirect(True)
#         self.wm_geometry("400x400")

#         self.label = tk.Label(self, text="Grab the lower-right corner to resize")
#         self.label.pack(side="top", fill="both", expand=True)

#         self.grip = ttk.Sizegrip(self)
#         self.grip.place(relx=1.0, rely=1.0, anchor="se")
#         self.grip.lift(self.label)
#         self.grip.bind("<B1-Motion>", self.OnMotion)


#     def OnMotion(self, event):
#         x1 = self.winfo_pointerx()
#         y1 = self.winfo_pointery()
#         x0 = self.winfo_rootx()
#         y0 = self.winfo_rooty()
#         self.geometry("%sx%s" % ((x1-x0),(y1-y0)))
#         return

# app=Example()
# app.mainloop()








#  resize from code with the title bar staying on top


# from tkinter import *
# from ctypes import windll

# root=Tk() # root (your app doesn't go in root, it goes in window)
# root.overrideredirect(True) # turns off title bar, geometry
# root.geometry('600x700+75+75') # set new geometry the + 75 + 75 is where it starts on the screen
# root.minimized = False # only to know if root is minimized
# root.maximized = False # only to know if root is maximized

# LGRAY = '#3e4042' # button color effects in the title bar (Hex color)
# DGRAY = '#25292e' # window background color               (Hex color)
# RGRAY = '#10121f' # title bar color                       (Hex color)

# root.config(bg="#25292e")
# title_bar = Frame(root, bg="RGRAY", relief='raised', bd=0,highlightthickness=0)


# def set_appwindow(mainWindow): # to display the window icon on the taskbar, 
#                                # even when using root.overrideredirect(True
#     # Some WindowsOS styles, required for task bar integration
#     GWL_EXSTYLE = -20
#     # 4 = 0x00040000
#     WS_EX_TOOLWINDOW = 0x00000080
#     # Magic
#     hwnd = windll.user32.GetParent(mainWindow.winfo_id())
#     stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
#     stylew = stylew & ~WS_EX_TOOLWINDOW
#     # stylew = stylew | WS_EX_APPWINDOW
#     res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
   
#     mainWindow.wm_withdraw()
#     mainWindow.after(10, lambda: mainWindow.wm_deiconify())


# # put a close button on the title bar
# title_bar_title = Label(title_bar, text="tkasdfghjk", bg=RGRAY,bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)

# # a frame for the main area of the window, this is where the actual app will go
# window = Frame(root, bg=DGRAY,highlightthickness=0)

# # pack the widgets
# title_bar.pack(fill=X)
# title_bar_title.pack(side=LEFT, padx=10)
# window.pack(expand=1, fill=BOTH) # replace this with your main Canvas/Frame/etc.
# #xwin=None
# #ywin=None
# # bind title bar motion to the move window function    

# def get_pos(event): # this is executed when the title bar is clicked to move the window
#     if root.maximized == False:
 
#         xwin = root.winfo_x()
#         ywin = root.winfo_y()
#         startx = event.x_root
#         starty = event.y_root

#         ywin = ywin - starty
#         xwin = xwin - startx

        
#         def move_window(event): # runs when window is dragged
#             root.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')


#         def release_window(event): # runs when window is released
#             root.config(cursor="arrow")
            
            
#         title_bar.bind('<B1-Motion>', move_window)
#         title_bar.bind('<ButtonRelease-1>', release_window)
#         title_bar_title.bind('<B1-Motion>', move_window)
#         title_bar_title.bind('<ButtonRelease-1>', release_window)
#     else:
#         # expand_button.config(text=" 🗖 ")
#         root.maximized = not root.maximized

# title_bar.bind('<Button-1>', get_pos) # so you can drag the window from the title bar
# title_bar_title.bind('<Button-1>', get_pos) # so you can drag the window from the title 

# # button effects in the title bar when hovering over buttons

# # resize the window width
# resizex_widget = Frame(window,bg=DGRAY,cursor='sb_h_double_arrow')
# resizex_widget.pack(side=RIGHT,ipadx=2,fill=Y)


# def resizex(event):
#     xwin = root.winfo_x()
#     difference = (event.x_root - xwin) - root.winfo_width()
    
#     if root.winfo_width() > 150 : # 150 is the minimum width for the window
#         try:
#             root.geometry(f"{ root.winfo_width() + difference }x{ root.winfo_height() }")
#         except:
#             pass
#     else:
#         if difference > 0: # so the window can't be too small (150x150)
#             try:
#                 root.geometry(f"{ root.winfo_width() + difference }x{ root.winfo_height() }")
#             except:
#                 pass
              
#     resizex_widget.config(bg=DGRAY)

# resizex_widget.bind("<B1-Motion>",resizex)

# # resize the window height
# resizey_widget = Frame(window,bg=DGRAY,cursor='sb_v_double_arrow')
# resizey_widget.pack(side=BOTTOM,ipadx=2,fill=X)

# def resizey(event):
#     ywin = root.winfo_y()
#     difference = (event.y_root - ywin) - root.winfo_height()

#     if root.winfo_height() > 150: # 150 is the minimum height for the window
#         try:
#             root.geometry(f"{ root.winfo_width()  }x{ root.winfo_height() + difference}")
#         except:
#             pass
#     else:
#         if difference > 0: # so the window can't be too small (150x150)
#             try:
#                 root.geometry(f"{ root.winfo_width()  }x{ root.winfo_height() + difference}")
#             except:
#                 pass

#     resizex_widget.config(bg=DGRAY)

# resizey_widget.bind("<B1-Motion>",resizey)

# # some settings
# root.after(10, lambda: set_appwindow(root)) # to see the icon on the task bar

# root.mainloop()























# from tkinter import *
# from ctypes import windll

# #this code works fine on windows 10, i didn't try it in any other OS, if you use window 8, 7, ... 
# #or you use a distro of linux, you can try it anyway
# #this code works fine as a exe made in pyinstaller

# tk_title = "tk" # Put here your window title

# root=Tk() # root (your app doesn't go in root, it goes in window)
# root.title(tk_title) 
# root.overrideredirect(True) # turns off title bar, geometry
# root.geometry('200x200+75+75') # set new geometry the + 75 + 75 is where it starts on the screen
# #root.iconbitmap("your_icon.ico") # to show your own icon 
# root.minimized = False # only to know if root is minimized
# root.maximized = False # only to know if root is maximized

# LGRAY = '#3e4042' # button color effects in the title bar (Hex color)
# DGRAY = '#25292e' # window background color               (Hex color)
# RGRAY = '#10121f' # title bar color                       (Hex color)

# root.config(bg="#25292e")
# title_bar = Frame(root, bg=RGRAY, relief='raised', bd=0,highlightthickness=0)


# def set_appwindow(mainWindow): # to display the window icon on the taskbar, 
#                                # even when using root.overrideredirect(True
#     # Some WindowsOS styles, required for task bar integration
#     GWL_EXSTYLE = -20
#     WS_EX_APPWINDOW = 0x00040000
#     WS_EX_TOOLWINDOW = 0x00000080
#     # Magic
#     hwnd = windll.user32.GetParent(mainWindow.winfo_id())
#     stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
#     stylew = stylew & ~WS_EX_TOOLWINDOW
#     stylew = stylew | WS_EX_APPWINDOW
#     res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
   
#     mainWindow.wm_withdraw()
#     mainWindow.after(10, lambda: mainWindow.wm_deiconify())
    

# def minimize_me():
#     root.attributes("-alpha",0) # so you can't see the window when is minimized
#     root.minimized = True       


# def deminimize(event):

#     root.focus() 
#     root.attributes("-alpha",1) # so you can see the window when is not minimized
#     if root.minimized == True:
#         root.minimized = False                              
        

# def maximize_me():

#     if root.maximized == False: # if the window was not maximized
#         root.normal_size = root.geometry()
#         expand_button.config(text=" 🗗 ")
#         root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
#         root.maximized = not root.maximized 
#         # now it's maximized
        
#     else: # if the window was maximized
#         expand_button.config(text=" 🗖 ")
#         root.geometry(root.normal_size)
#         root.maximized = not root.maximized
#         # now it is not maximized

# # put a close button on the title bar
# close_button = Button(title_bar, text='  ×  ', command=root.destroy,bg=RGRAY,padx=2,pady=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
# expand_button = Button(title_bar, text=' 🗖 ', command=maximize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
# minimize_button = Button(title_bar, text=' 🗕 ',command=minimize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
# title_bar_title = Label(title_bar, text=tk_title, bg=RGRAY,bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)

# # a frame for the main area of the window, this is where the actual app will go
# window = Frame(root, bg=DGRAY,highlightthickness=0)

# # pack the widgets
# title_bar.pack(fill=X)
# close_button.pack(side=RIGHT,ipadx=7,ipady=1)
# expand_button.pack(side=RIGHT,ipadx=7,ipady=1)
# minimize_button.pack(side=RIGHT,ipadx=7,ipady=1)
# title_bar_title.pack(side=LEFT, padx=10)
# window.pack(expand=1, fill=BOTH) # replace this with your main Canvas/Frame/etc.
# #xwin=None
# #ywin=None
# # bind title bar motion to the move window function

# def changex_on_hovering(event):
#     global close_button
#     close_button['bg']='red'
    
    
# def returnx_to_normalstate(event):
#     global close_button
#     close_button['bg']=RGRAY
    

# def change_size_on_hovering(event):
#     global expand_button
#     expand_button['bg']=LGRAY
    
    
# def return_size_on_hovering(event):
#     global expand_button
#     expand_button['bg']=RGRAY
    

# def changem_size_on_hovering(event):
#     global minimize_button
#     minimize_button['bg']=LGRAY
    
    
# def returnm_size_on_hovering(event):
#     global minimize_button
#     minimize_button['bg']=RGRAY
    

# def get_pos(event): # this is executed when the title bar is clicked to move the window
#     if root.maximized == False:
 
#         xwin = root.winfo_x()
#         ywin = root.winfo_y()
#         startx = event.x_root
#         starty = event.y_root

#         ywin = ywin - starty
#         xwin = xwin - startx

        
#         def move_window(event): # runs when window is dragged
#             root.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')


#         def release_window(event): # runs when window is released
#             root.config(cursor="arrow")
            
            
#         title_bar.bind('<B1-Motion>', move_window)
#         title_bar.bind('<ButtonRelease-1>', release_window)
#         title_bar_title.bind('<B1-Motion>', move_window)
#         title_bar_title.bind('<ButtonRelease-1>', release_window)
#     else:
#         expand_button.config(text=" 🗖 ")
#         root.maximized = not root.maximized

# title_bar.bind('<Button-1>', get_pos) # so you can drag the window from the title bar
# title_bar_title.bind('<Button-1>', get_pos) # so you can drag the window from the title 

# # button effects in the title bar when hovering over buttons
# close_button.bind('<Enter>',changex_on_hovering)
# close_button.bind('<Leave>',returnx_to_normalstate)
# expand_button.bind('<Enter>', change_size_on_hovering)
# expand_button.bind('<Leave>', return_size_on_hovering)
# minimize_button.bind('<Enter>', changem_size_on_hovering)
# minimize_button.bind('<Leave>', returnm_size_on_hovering)

# # resize the window width
# resizex_widget = Frame(window,bg=DGRAY,cursor='sb_h_double_arrow')
# resizex_widget.pack(side=RIGHT,ipadx=2,fill=Y)


# def resizex(event):
#     xwin = root.winfo_x()
#     difference = (event.x_root - xwin) - root.winfo_width()
    
#     if root.winfo_width() > 150 : # 150 is the minimum width for the window
#         try:
#             root.geometry(f"{ root.winfo_width() + difference }x{ root.winfo_height() }")
#         except:
#             pass
#     else:
#         if difference > 0: # so the window can't be too small (150x150)
#             try:
#                 root.geometry(f"{ root.winfo_width() + difference }x{ root.winfo_height() }")
#             except:
#                 pass
              
#     resizex_widget.config(bg=DGRAY)

# resizex_widget.bind("<B1-Motion>",resizex)

# # resize the window height
# resizey_widget = Frame(window,bg=DGRAY,cursor='sb_v_double_arrow')
# resizey_widget.pack(side=BOTTOM,ipadx=2,fill=X)

# def resizey(event):
#     ywin = root.winfo_y()
#     difference = (event.y_root - ywin) - root.winfo_height()

#     if root.winfo_height() > 150: # 150 is the minimum height for the window
#         try:
#             root.geometry(f"{ root.winfo_width()  }x{ root.winfo_height() + difference}")
#         except:
#             pass
#     else:
#         if difference > 0: # so the window can't be too small (150x150)
#             try:
#                 root.geometry(f"{ root.winfo_width()  }x{ root.winfo_height() + difference}")
#             except:
#                 pass

#     resizex_widget.config(bg=DGRAY)

# resizey_widget.bind("<B1-Motion>",resizey)

# # some settings
# root.bind("<FocusIn>",deminimize) # to view the window by clicking on the window icon on the taskbar
# root.after(10, lambda: set_appwindow(root)) # to see the icon on the task bar


# #YOUR CODE GOES between the lines :)
# # ===================================================================================================





# # Uncomment below to see example of packing a label
# #Label(window,text="Hello :D",bg=DGRAY,fg="#fff").pack(expand=1) # example 
# root.mainloop()














#  fix minimize
#  get it to resize on window mouse on border

# on left hand side, put in a colored line on which place settings button
# make settings it's own file?





# style = ttk.Style()
# style.configure('Vertical.TFrame', bg='red')

# verticak_frame = ttk.Frame(root, width = 100, height = 350, style = 'Vertical.TFrame')
# verticak_frame.grid(row = 0, column = 2, rowspan = 3, sticky = 'NSEW')