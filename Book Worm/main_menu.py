from array import array
import tkinter as tk
import random
import settings_frame
import scan_folders
import global_variables.load_folders_to_scan
import epub_file_data
from PIL import Image
import zipfile
from lxml import etree
from PIL import ImageTk as itk
import file_reader_frame

return_button_array = []
forward_button_array = []

def active_frame(new_active_frame, relative):
    global current_active_frame
    global return_button_array
    if relative == "return":
        print(current_active_frame, new_active_frame)
        forward_button_array.append(return_button_array[-1])
        return_button_array.pop()
        current_active_frame.pack_forget()
        new_active_frame.pack(side="right", fill="both", expand=True)
        current_active_frame = new_active_frame

    # check if current_active_frame and new_active_frame are the same
        # issue is, the frames are different becaue they add a different number at the end
    
    else:# current_active_frame != new_active_frame:
        print(current_active_frame, new_active_frame)
        return_button_array.append(current_active_frame)
        current_active_frame.pack_forget()
        new_active_frame.pack(side="right", fill="both", expand=True)
        current_active_frame = new_active_frame

class DynamicGrid(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        global current_active_frame
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.frame = tk.Frame(self, bg='black')
        self.frame.pack(side="right", fill="both", expand=True)
        
        self.text = tk.Text(self.frame, wrap="char", borderwidth=0, highlightthickness=0, bg='orange', state="disabled")
        self.text.pack(fill="both", expand=True)
        
        current_active_frame = self.text   

        ribbon_frame = tk.Frame(parent,width = 100, height = 350, bg='yellow')
        ribbon_frame.pack(side="left", fill="both", expand=False)

        return_button_icon = tk.PhotoImage(file='icons and images\icons8-settings-500.png')
        return_button = tk.Button(
            ribbon_frame, 
            text = "Return",
            image = return_button_icon, 
            width = 60, 
            height = 60,
            command = lambda:active_frame(return_button_array[len(return_button_array)-1], "return") #don't do -1, the number needs to adapt
            )
        return_button.image = return_button_icon
        return_button.pack()

        currently_open_button_icon = tk.PhotoImage(file='icons and images\icons8-settings-500.png')
        currently_open_button = tk.Button(
            ribbon_frame, 
            text="Currently Open",
            image = currently_open_button_icon, 
            width = 60, 
            height = 60,
            # command=lambda:active_frame()
            )
        currently_open_button.image = currently_open_button_icon
        currently_open_button.pack()

        # currently_reading_button_icon = tk.PhotoImage(file='icons and images\icons8-settings-500.png')
        # currently_reading_button = tk.Button(
        #     ribbon_frame, 
        #     text="Curently Reading",
        #     image = currently_reading_button_icon, 
        #     width = 60, 
        #     height = 60,
        #     command=lambda:active_frame(settings())
        #     )
        # currently_reading_button.image = currently_reading_button_icon
        # currently_reading_button.pack()

        # to_read_button_icon = tk.PhotoImage(file='icons and images\icons8-settings-500.png')
        # to_read_button = tk.Button(
        #     ribbon_frame, 
        #     text="To Read",
        #     image = to_read_button_icon, 
        #     width = 60, 
        #     height = 60,
        #     command=lambda:active_frame(settings())
        #     )
        # to_read_button.image = to_read_button_icon
        # to_read_button.pack()

        # have_read_button_icon = tk.PhotoImage(file='icons and images\icons8-settings-500.png')
        # have_read_button = tk.Button(
        #     ribbon_frame, 
        #     text="Have Read",
        #     image = have_read_button_icon, 
        #     width = 60, 
        #     height = 60,
        #     command=lambda:active_frame(settings())
        #     )
        # have_read_button.image = have_read_button_icon
        # have_read_button.pack()

        settings_button_icon = tk.PhotoImage(file='icons and images\icons8-settings-500.png')
        settings_button = tk.Button(
            ribbon_frame, 
            image = settings_button_icon, 
            width = 60, 
            height = 60,
            command=lambda:active_frame(settings_frame.settings_frame(self.frame), "np")
            )
        settings_button.image = settings_button_icon
        settings_button.pack(side = "left", anchor="s")




#     def add_book_cover_and_info(self, epub_file_path, file_type):

#         background = None

#         frame = tk.Frame(self.text, width = 100, height = 350, bg='purple')
#         frame.pack()
        
#         if file_type == "epub":
#             image = epub_file_data.get_epub_cover_image(epub_file_path)
#             file_title = epub_file_data.get_epub_book_title(epub_file_path)
#             file_author = epub_file_data.get_epub_book_author(epub_file_path)
#             background = image

#         photo = itk.PhotoImage(file = background)
#         file_cover_image_button = tk.Button(
#             frame,
#             width = 200,
#             height = 400, 
#             image = photo,
#             command = lambda: active_frame(file_reader_frame(self.frame), "np") #get it to go to a frame for reading
#             )
#         file_cover_image_button.image = photo
#         file_cover_image_button.pack()
            
#         file_title_button = tk.Button(
#         frame, 
#         text = file_title,
#         width = 30, 
#         height = 2
    
#         ).pack()

#         file_author_button = tk.Button(
#         frame, 
#         text= file_author,
#         width = 30, 
#         height = 2
# #       got to page with all the info about the author and his works, maybe hook there a wiki article
#         ).pack()



#         #The Pack geometry manager packs widgets in rows or columns.
#         # bg = color if color else random.choice(("red", "orange", "green", "blue", "violet"))
#         # box = tk.Frame(self.text, bd=1, relief="sunken", background=bg,
#         #                width=100, height=100)
#         self.text.configure(state="normal")
#         self.text.window_create("end", window = frame)
#         self.text.configure(state="disabled")

# def make_widgets_for_each_file(dictionary_of_valid_files, dynamic_grid):
#     for epub_file in dictionary_of_valid_files["array_of_epub_files"]:
#         dynamic_grid.add_book_cover_and_info(epub_file, "epub")
    
#     # for mobi_file in dictionary_of_valid_files["array_of_mobi_files"]:
#     #     dynamic_grid.add_book_cover_and_info(mobi_file, "mobi")
    
#     # for pdf_file in dictionary_of_valid_files["array_of_pdf_files"]:
#     #     dynamic_grid.add_book_cover_and_info(pdf_file, "pdf")


    def add_book_cover_and_info(self, file_path, file_type):

        background = None

        frame = tk.Frame(self.text, width = 100, height = 350, bg='purple')
        frame.pack()
        
        if file_type == "epub":
            image = epub_file_data.get_epub_cover_image(file_path)
            file_title = epub_file_data.get_epub_book_title(file_path)
            file_author = epub_file_data.get_epub_book_author(file_path)
            background = image

        photo = itk.PhotoImage(file = background)
        file_cover_image_button = tk.Button(
            frame,
            width = 200,
            height = 400, 
            image = photo,
            command = lambda: active_frame(file_reader_frame.file_reader_main_frame(self.frame, file_path), "np")
            )
        file_cover_image_button.image = photo
        file_cover_image_button.pack()
            
        file_title_button = tk.Button(
        frame, 
        text = file_title,
        width = 30, 
        height = 2
    
        ).pack()

        file_author_button = tk.Button(
        frame, 
        text= file_author,
        width = 30, 
        height = 2
#       got to page with all the info about the author and his works, maybe hook there a wiki article
        ).pack()

        #The Pack geometry manager packs widgets in rows or columns.
        # bg = color if color else random.choice(("red", "orange", "green", "blue", "violet"))
        # box = tk.Frame(self.text, bd=1, relief="sunken", background=bg,
        #                width=100, height=100)
        self.text.configure(state="normal")
        self.text.window_create("end", window = frame)
        self.text.configure(state="disabled")

def make_widgets_for_each_file(dictionary_of_valid_files, dynamic_grid):
    for epub_file in dictionary_of_valid_files["array_of_epub_files"]:
        dynamic_grid.add_book_cover_and_info(epub_file, "epub")

# for mobi_file in dictionary_of_valid_files["array_of_mobi_files"]:
#     dynamic_grid.add_book_cover_and_info(mobi_file, "mobi")

# for pdf_file in dictionary_of_valid_files["array_of_pdf_files"]:
#     dynamic_grid.add_book_cover_and_info(pdf_file, "pdf")



class Example(object):
    def __init__(self):

        self.root = tk.Tk()
        self.root.minsize(300, 400)

        self.frame = tk.Frame(self.root,width = 100, height = 350, bg='white')
        self.frame.pack(side="left", fill="both", expand=True)
        
        self.dg = DynamicGrid(self.frame, width=500, height=200)
        self.dg.pack(side="top", fill="both", expand=True)

        folders_to_scan_array :array = []
        folders_to_scan_array = global_variables.load_folders_to_scan.load_folders_to_scan()
        dictionary_of_valid_files = scan_folders.scan_folders(folders_to_scan_array)
        make_widgets_for_each_file(dictionary_of_valid_files, self.dg)

    def start(self):
        self.root.mainloop()

Example().start()


# read folders from google drive
#  make it work with audio books too