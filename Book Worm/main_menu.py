from array import array
import tkinter as tk
import random
import settings_frame
import scan_folders
import global_variables.load_folders_to_scan

class DynamicGrid(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.frame = tk.Frame(self, bg='black')
        self.frame.pack(side="right", fill="both", expand=True)
        
        return_button_array = []


        self.text = tk.Text(self.frame, wrap="char", borderwidth=0, highlightthickness=0, bg='orange', state="disabled")
        self.text.pack(fill="both", expand=True)
        
        self.boxes = []
        
        current_active_frame = self.text

        def active_frame(new_active_frame):
            nonlocal current_active_frame
            nonlocal return_button_array

            # check if current_active_frame and new_active_frame are the same


            print(type(new_active_frame))

            # new_active_frame_1 = new_active_frame[-1]
            # print("1234567890", type(new_active_frame[-1]))

            # print("qwertyuioppasdfghjkl;", (new_active_frame_1))





            if current_active_frame != new_active_frame:





                print(current_active_frame, new_active_frame)
                return_button_array.append(current_active_frame)
                current_active_frame.pack_forget()
                new_active_frame.pack(side="right", fill="both", expand=True)
                current_active_frame = new_active_frame

        ribbon_frame = tk.Frame(parent,width = 100, height = 350, bg='yellow')
        ribbon_frame.pack(side="left", fill="both", expand=False)

        return_button_icon = tk.PhotoImage(file='icons and images\icons8-settings-500.png')
        return_button = tk.Button(
            ribbon_frame, 
            text="Curently Reading",
            image = return_button_icon, 
            width = 60, 
            height = 60,
            command=lambda:active_frame(return_button_array[len(return_button_array)-1])
            )
        return_button.image = return_button_icon
        return_button.pack()

        currently_reading_button_icon = tk.PhotoImage(file='icons and images\icons8-settings-500.png')
        currently_reading_button = tk.Button(
            ribbon_frame, 
            text="Curently Reading",
            image = currently_reading_button_icon, 
            width = 60, 
            height = 60,
            command=lambda:active_frame(settings())
            )
        currently_reading_button.image = currently_reading_button_icon
        currently_reading_button.pack()

        to_read_button_icon = tk.PhotoImage(file='icons and images\icons8-settings-500.png')
        to_read_button = tk.Button(
            ribbon_frame, 
            text="To Read",
            image = to_read_button_icon, 
            width = 60, 
            height = 60,
            command=lambda:active_frame(settings())
            )
        to_read_button.image = to_read_button_icon
        to_read_button.pack()

        have_read_button_icon = tk.PhotoImage(file='icons and images\icons8-settings-500.png')
        have_read_button = tk.Button(
            ribbon_frame, 
            text="Have Read",
            image = have_read_button_icon, 
            width = 60, 
            height = 60,
            command=lambda:active_frame(settings())
            )
        have_read_button.image = have_read_button_icon
        have_read_button.pack()

        settings_button_icon = tk.PhotoImage(file='icons and images\icons8-settings-500.png')
        settings_button = tk.Button(
            ribbon_frame, 
            image = settings_button_icon, 
            width = 60, 
            height = 60,
            command=lambda:active_frame(settings_frame.settings_frame(self.frame))
            )
        settings_button.image = settings_button_icon
        settings_button.pack(side = "left", anchor="s")




    def add_box(self, color=None):
        bg = color if color else random.choice(("red", "orange", "green", "blue", "violet"))
        box = tk.Frame(self.text, bd=1, relief="sunken", background=bg,
                       width=100, height=100)
        self.boxes.append(box)
        self.text.configure(state="normal")
        self.text.window_create("end", window=box)
        self.text.configure(state="disabled")



class Example(object):
    def __init__(self):

        folders_to_scan_array :array = []
        folders_to_scan_array = global_variables.load_folders_to_scan.load_folders_to_scan()
        scan_folders.scan_folders(folders_to_scan_array)

        self.root = tk.Tk()
        self.frame = tk.Frame(self.root,width = 100, height = 350, bg='white')
        self.frame.pack(side="left", fill="both", expand=True)

        self.dg = DynamicGrid(self.frame, width=500, height=200)
        self.dg.pack(side="top", fill="both", expand=True)
       


        # add a few boxes to start
        # for i in range(10):
        #     self.dg.add_box()


    def start(self):
        self.root.mainloop()
Example().start()