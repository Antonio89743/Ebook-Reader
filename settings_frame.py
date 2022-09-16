import tkinter as tk

def settings_frame(main_window):

    frame_settings = tk.Frame(main_window, bg='blue')
    frame_settings.pack(side="right", fill="both", expand=True)
    # frame_settings.pack()
    # frame_settings.grid(row=0,column=0,sticky='nsew')

    scan_folders_label = tk.Label(frame_settings, text="Folders scanned for eligible files")
    scan_folders_label.pack()

    settings_button = tk.Button(frame_settings, text='Scanned Folders', command=lambda:active_frame(folders_to_scan(), None))
    settings_button.pack()

    return frame_settings