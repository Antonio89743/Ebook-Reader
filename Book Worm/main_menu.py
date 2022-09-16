from array import array
import tkinter as tk
import random
import settings_frame
import scan_folders
import global_variables.load_folders_to_scan
import file_cover_image
from PIL import Image
import zipfile
from lxml import etree
from PIL import ImageTk as itk

class DynamicGrid(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.frame = tk.Frame(self, bg='black')
        self.frame.pack(side="right", fill="both", expand=True)
        
        return_button_array = []


        self.text = tk.Text(self.frame, wrap="char", borderwidth=0, highlightthickness=0, bg='orange', state="disabled")
        self.text.pack(fill="both", expand=True)
        

        
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
            text="Return",
            image = return_button_icon, 
            width = 60, 
            height = 60,
            command=lambda:active_frame(return_button_array[len(return_button_array)-1]) #don't do -1, the number needs to adapt
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




    def add_box(self, epub_file_path):
        # try to add here the zip stuff from the other file

        # self.button_image = Image.open(file_cover_image.get_epub_cover_image(epub_file_path))
        # print(self.button_image)

        # self.button_image = file_cover_image.get_epub_cover_image(epub_file_path)
        # photo = itk.PhotoImage(file = self.button_image)
        # canvas = tk.Button(self,width=999,height=999, image=photo)
        # canvas.pack()
        
        # image = file_cover_image.get_epub_cover_image(epub_file_path)
        # background = image
        # print(image, " ", background)
        # photo = itk.PhotoImage(file = background)
        # print(photo)
        # button = tk.Button(self.text,width=200,height=200, image=photo)
        # button.pack()






        # root = tk.Tk()
        # root.geometry('300x300')

        # background = file_cover_image.get_epub_cover_image(epub_file_path)
        # print(background)
        # photo = itk.PhotoImage(file = background)
        # print(photo)
        # button = tk.Button(root,width=300,height=300, image=photo)
        # button.pack()
        # root.mainloop()


#  maybe make the other file make all of these widgets too?


        # button = tk.Button(self.text, width=25, height=15, image = self.button_image)





        #The Pack geometry manager packs widgets in rows or columns.



        # bg = color if color else random.choice(("red", "orange", "green", "blue", "violet"))
        # box = tk.Frame(self.text, bd=1, relief="sunken", background=bg,
        #                width=100, height=100)
        self.text.configure(state="normal")
        self.text.window_create("end", window=button)
        self.text.configure(state="disabled")


def make_widgets_for_each_file(dictionary_of_valid_files, dynamic_grid):
    for epub_file in dictionary_of_valid_files["array_of_epub_files"]:
        dynamic_grid.add_box(epub_file)


class Example(object):
    def __init__(self):

        self.root = tk.Tk()
        self.frame = tk.Frame(self.root,width = 100, height = 350, bg='white')
        self.frame.pack(side="left", fill="both", expand=True)

        self.dg = DynamicGrid(self.frame, width=500, height=200)
        self.dg.pack(side="top", fill="both", expand=True)

        folders_to_scan_array :array = []
        folders_to_scan_array = global_variables.load_folders_to_scan.load_folders_to_scan()
        dictionary_of_valid_files = scan_folders.scan_folders(folders_to_scan_array)
        make_widgets_for_each_file(dictionary_of_valid_files, self.dg)


       


        # add a few boxes to start
        # for i in range(10):
        #     self.dg.add_box()


    def start(self):
        self.root.mainloop()
Example().start()