import tkinter as tk
from turtle import xcor
import epub_file_data

def file_reader_main_frame(main_window, file_path):
    frame_file_reader = tk.Frame(main_window, background = 'pink')
    frame_file_reader.pack(side = "right", fill = "both", expand = True)

    if file_path.endswith(".epub"):

        x = epub_file_data.get_epub_book_text(file_path)

        text_frame = tk.Label(frame_file_reader, text=x, height=70, width=110)
        text_frame.pack()
   
    
    
    return frame_file_reader
