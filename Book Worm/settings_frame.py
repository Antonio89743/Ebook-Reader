from array import array
import tkinter as tk
import scan_folders
import global_variables.load_folders_to_scan

folders_to_scan_array :array = []
folders_to_scan_array = global_variables.load_folders_to_scan.load_folders_to_scan()

def list_of_folders_to_scan(frame):

    for folder in folders_to_scan_array:
        
        frame = tk.Frame(frame).pack(side="right", fill="both", expand=True)
        
        folder_name_label = tk.Label(frame, text=folder).pack()



def settings_frame(main_window):
    frame_settings = tk.Frame(main_window, bg='blue')
    frame_settings.pack(side="right", fill="both", expand=True)

    scan_folders_label = tk.Label(frame_settings, text="Folders scanned for eligible files")
    scan_folders_label.pack()

    list_of_folders_to_scan(frame_settings)

    # settings_button = tk.Button(frame_settings, text='Scanned Folders', command=lambda:)
    # settings_button.pack()




    settings_button = tk.Button(frame_settings, text='Scanned Folders', command=lambda:active_frame(scan_folders.scan_folders(folders_to_scan), None))
    settings_button.pack()

    return frame_settings




#                 #     print(current_active_frame, new_active_frame)
#                 # return_button_array.append(current_active_frame)
#                 # current_active_frame.pack_forget()
#                 # new_active_frame.pack(side="right", fill="both", expand=True)
#                 # current_active_frame = new_active_frame


#                 def save_folders_to_scan_array(folders_to_scan_array):
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



# # on settings, top right add button to return to previous screen, whether it be bookreader screen or main menu

# # have a vertical list of folders, on yellow frame
# # those are just div with 2 horizontal texts, one below another
# # text 1 shows the name of the folder
# # text 2 shows the full path to the folder
# # on the right hand side of each div is a X button to remove the particular folder from use
# # on the bottom just have done button