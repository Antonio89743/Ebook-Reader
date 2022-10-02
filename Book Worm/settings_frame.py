from array import array
import tkinter as tk
from types import NoneType
import scan_folders
import global_variables.load_folders_to_scan
from tkscrolledframe import ScrolledFrame

folders_to_scan_array :array = []
folders_to_scan_array = global_variables.load_folders_to_scan.load_folders_to_scan()

def list_of_folders_to_scan(frame):

    # text_widget = tk.Text(scrollbar, borderwidth=0, highlightthickness=0, bg='gray', state="disabled", cursor="arrow")
    # text_widget.pack(fill="both", expand=True)

    # scrollbar = tk.Scrollbar(frame, command=text_widget.yview)
    # text_widget['yscroll'] = scrollbar.set
    # scrollbar.pack(side="right", fill="both", expand=False)

    # canvas = tk.Canvas(frame, bg="pink")
    # canvas.pack(fill="both", expand=True)

    # scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    # scrollbar.pack(side="right", fill="y")

    # canvas.configure(yscrollcommand=scrollbar.set)
    # canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

    # canvas_frame = tk.Frame(canvas, bg="white")

    # canvas.create_window((0,0), window=canvas_frame, anchor="nw")

    scrollbar = tk.Scrollbar(frame)
    text_widget = tk.Text(frame, height=10, width=10, yscrollcommand=scrollbar.set, bg='purple')
    scrollbar.config(command=text_widget.yview)
    scrollbar.pack(side='right', fill='y')
    text_widget.pack(fill="both", expand=True)

    folders_to_scan_list_frame = tk.Frame(text_widget, width = 500, height = 90, bg = 'red')
    folders_to_scan_list_frame.place(relwidth=0.8, y=50, relx=0.1)

    # text_widget.configure(state="normal")
    # text_widget.window_create("end", window = folders_to_scan_list_frame)
    # text_widget.configure(state="disabled")

    # folders_to_scan_list_frame.grid(row=3, column=4)

    folders_to_scan_list_frame_shrunk = True


    add_folder_to_scan_button = tk.Button(folders_to_scan_list_frame, height = 1, width = 10, pady=10, text=' + ')
    
    def add_element_for_folder_to_scan():

        y_position = 90

        for n in range (30):

            folders_to_scan_list_element_frame = tk.Frame(folders_to_scan_list_frame, width = 100, height = 120, bg = 'blue')
            folders_to_scan_list_element_frame.place(y = y_position, relx = 0.5)
            
            add_folder_to_scan_button = tk.Button(folders_to_scan_list_element_frame, height = 1, width = 1, pady=10, text=' X ')
            add_folder_to_scan_button.place(y = 20, relx = 0.7)

            y_position += 190

            text_widget.configure(state="normal")
            text_widget.window_create("end", window = folders_to_scan_list_frame)
            text_widget.configure(state="disabled")



            
    add_element_for_folder_to_scan()



    def folders_to_scan_list_frame_expand_shrink():
        nonlocal folders_to_scan_list_frame
        nonlocal folders_to_scan_list_frame_shrunk
        if folders_to_scan_list_frame_shrunk == True:
            folders_to_scan_list_frame.place(relwidth=0.8, y=50, height=4000, relx=0.1) # should adapt to the contents of the scroll container
            add_folder_to_scan_button.place(y = 30, relx = 0.5)

            # text_widget.configure(state="normal")
            # text_widget.window_create("end", window = folders_to_scan_list_frame)
            # text_widget.configure(state="disabled")

        elif folders_to_scan_list_frame_shrunk == False:
            folders_to_scan_list_frame.place(height=23, relwidth=0.8, y=50, relx=0.1)



        folders_to_scan_list_frame_shrunk = not folders_to_scan_list_frame_shrunk


    expand_folders_to_scan_list_button = tk.Button(folders_to_scan_list_frame, text='Expand', command = lambda: folders_to_scan_list_frame_expand_shrink())
    expand_folders_to_scan_list_button.pack(side = "right" , anchor="n")    

def active_tab(new_active_tab, relative):
    global current_active_tab
    # global return_button_array
    if relative == "return":
            # print(current_active_frame, new_active_tab)
            # forward_button_array.append(return_button_array[-1])
            # return_button_array.pop()
            current_active_tab.pack_forget()
            new_active_tab.pack(side="right", fill="both", expand=True)
            current_active_tab = new_active_tab

    # check if current_active_frame and new_active_frame are the same
        # issue is, the frames are different becaue they add a different number at the end
    
    else:
            # current_active_frame != new_active_frame:
            # print(current_active_frame, new_active_tab)
            # return_button_array.append(current_active_frame)
            current_active_tab.pack_forget()
            new_active_tab.pack(side="right", fill="both", expand=True)
            current_active_tab = new_active_tab

def settings_frame(main_window):

    global current_active_tab

    frame_settings = tk.Frame(main_window, bg = 'blue')
    frame_settings.pack(side = "right", fill = "both", expand = True)

    tab_frames = tk.Frame(frame_settings, bg='white', padx=40, pady=20)
    tab_frames.pack(side = "top", fill = "none", expand = False)


    themes_and_prefrences_frame = tk.Frame(frame_settings, bg = 'green')
    themes_and_prefrences_frame.pack(side="right", fill="both", expand = True)

    themes_and_prefrences_button = tk.Button(tab_frames, text='Themes & Preferences', command = lambda: active_tab(themes_and_prefrences_frame, "none"))
    themes_and_prefrences_button.pack(side = "left" , anchor="n", padx=5)


    folders_to_scan_frame = tk.Frame(frame_settings, bg='orange')

    list_of_folders_to_scan(folders_to_scan_frame)

    folders_to_scan_button = tk.Button(tab_frames, text='Folders To Scan', command = lambda: active_tab(folders_to_scan_frame, "none"))
    folders_to_scan_button.pack(side = "left" , anchor="n", padx=5)

    about_frame = tk.Frame(frame_settings, bg='pink')


    about_button = tk.Button(tab_frames, text='About', command = lambda: active_tab(about_frame, "none"))
    about_button.pack(side = "right" , anchor="n", padx=5)

    tabs = [themes_and_prefrences_frame, folders_to_scan_frame, about_frame]

    current_active_tab = themes_and_prefrences_frame
    active_tab(themes_and_prefrences_frame, "none")

    return frame_settings






#     def save_folders_to_scan_array(folders_to_scan_array):
#     data = json.dumps(folders_to_scan_array)
#     file = open(os.path.join(save_folder_path, 'folders_to_scan.json'), 'w')
#     file.write(data)
#     file.close()

# def add_new_folder_to_scan():
#     new_folder = filedialog.askdirectory()
#     scan_folders(new_folder)
#     check_list_for_duplicates(folders_to_scan_array, new_folder)
#     save_folders_to_scan_array(folders_to_scan_array)

# def check_list_for_duplicates(list :List, new_list_member):
#     duplicate :bool = False
#     for list_member in list:
#         if list_member == new_list_member:
#             duplicate = True
#     if duplicate == False:
#         list.append(new_list_member)
#     elif duplicate == True:
#         pass

# # have a vertical list of folders, on yellow frame
# # those are just div with 2 horizontal texts, one below another
# # text 1 shows the name of the folder
# # text 2 shows the full path to the folder
# # on the right hand side of each div is a X button to remove the particular folder from use
# # on the bottom just have done button