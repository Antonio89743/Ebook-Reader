from array import array
import tkinter as tk
from types import NoneType
import scan_folders
import global_variables.load_folders_to_scan

folders_to_scan_array :array = []
folders_to_scan_array = global_variables.load_folders_to_scan.load_folders_to_scan()

def list_of_folders_to_scan(frame):

    folders_to_scan_list_frame = tk.Frame(frame, width = 500, height = 90, bg = 'red')
    folders_to_scan_list_frame.pack(side="top", fill="x", expand=True)
    folders_to_scan_list_frame_shrunk = True

    def create_list_of_folders_to_scan():

        settings_button = tk.Button(folders_to_scan_list_frame, height = 20, pady=10, text=' + ')
        settings_button.pack()

    
    def folders_to_scan_list_frame_expand_shrink():
        nonlocal folders_to_scan_list_frame
        nonlocal folders_to_scan_list_frame_shrunk
        if folders_to_scan_list_frame_shrunk == True:
            folders_to_scan_list_frame.pack(side="right", fill="both", expand=True)
            create_list_of_folders_to_scan()

        elif folders_to_scan_list_frame_shrunk == False:
            folders_to_scan_list_frame.pack(side="top", fill="x", expand=True)
        folders_to_scan_list_frame_shrunk = not folders_to_scan_list_frame_shrunk


    settings_button = tk.Button(folders_to_scan_list_frame, text='Expand', command = lambda: folders_to_scan_list_frame_expand_shrink())
    settings_button.pack(side = "right" , anchor="n")

    # for folder in range(20):
        
    #     frame = tk.Frame(frame, width = 500, height = 50, pady = 90, bg = 'red')
    #     frame.pack(side="left", fill="both", expand=True)

    #     settings_button = tk.Button(frame, text='+')
    #     settings_button.pack(side = "right" , anchor="n")


        # settings_button = tk.Button(frame, text='+')
        # settings_button.grid()


        # folder_name_label = tk.Label(frame, text = folder, bg = 'purple', state="disabled").grid(sticky='EW')

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

    tab_frames = tk.Frame(main_window, bg='blue')
    tab_frames.place(anchor="center", relx=0.5, y = 20)

    themes_and_prefrences_frame = tk.Frame(frame_settings, bg = 'green')
    themes_and_prefrences_frame.pack(side="right", fill="both", expand = True)

    themes_and_prefrences_button = tk.Button(tab_frames, text='Themes & Preferences', command = lambda: active_tab(themes_and_prefrences_frame, "none"))
    themes_and_prefrences_button.pack(side = "left" , anchor="n", padx=5)


    folders_to_scan_frame = tk.Frame(frame_settings, bg='orange')







    folders_to_scan_list_frame = tk.Frame(folders_to_scan_frame, width = 500, height = 90, bg = 'red')
    folders_to_scan_list_frame.pack(side="top", fill="x", expand=True)
    folders_to_scan_list_frame_shrunk = True

    def create_list_of_folders_to_scan():

        settings_button = tk.Button(folders_to_scan_list_frame, height = 20, pady=10, text=' + ')
        settings_button.pack()

    
    def folders_to_scan_list_frame_expand_shrink():
        nonlocal folders_to_scan_list_frame
        nonlocal folders_to_scan_list_frame_shrunk
        if folders_to_scan_list_frame_shrunk == True:
            folders_to_scan_list_frame.pack(side="right", fill="both", expand=True)
            create_list_of_folders_to_scan()

        elif folders_to_scan_list_frame_shrunk == False:
            folders_to_scan_list_frame.pack(side="top", fill="x", expand=True)
        folders_to_scan_list_frame_shrunk = not folders_to_scan_list_frame_shrunk


    settings_button = tk.Button(folders_to_scan_list_frame, text='Expand', command = lambda: folders_to_scan_list_frame_expand_shrink())
    settings_button.pack(side = "right" , anchor="n")











    folders_to_scan_button = tk.Button(tab_frames, text='Folders To Scan', command = lambda: active_tab(folders_to_scan_frame, "none"))
    folders_to_scan_button.pack(side = "left" , anchor="n", padx=5)

    about_frame = tk.Frame(frame_settings, bg='pink')


    about_button = tk.Button(tab_frames, text='About', command = lambda: active_tab(about_frame, "none"))
    about_button.pack(side = "right" , anchor="n", padx=5)

    tabs = [themes_and_prefrences_frame, folders_to_scan_frame, about_frame]

    current_active_tab = themes_and_prefrences_frame
    active_tab(themes_and_prefrences_frame, "none")









    # settings_button = tk.Button(frame_settings, text='Scanned Folders', command=lambda:active_frame(scan_folders.scan_folders(folders_to_scan), None))
    # settings_button.pack()

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