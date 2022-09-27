import tkinter as tk
from turtle import xcor
import epub_file_data

def file_reader_main_frame(main_window, file_path):
    
    frame_file_reader = tk.Frame(main_window, background = 'pink')
    frame_file_reader.pack(side = "right", fill = "both", expand = True)

    if file_path.endswith(".epub"):

        epub_file_info = epub_file_data.get_epub_book_text(file_path)

        text_frame = tk.Label(frame_file_reader, text=epub_file_info, height=70, width=110)
        text_frame.pack()
   




        # text_box = tk.Text(
        #     ws,
        #     height=13,
        #     width=32, 
        #     font=(12)  
        # )

        # text_box.pack(side='left',expand=True)


        sb_ver = tk.Scrollbar(
            frame_file_reader,
            orient='vertical'
            )

        sb_ver.pack(side='right', fill='y')

        # text_frame.config(yscrollcommand=sb_ver.set)
        # sb_ver.config(command=text_frame.yview)



    return frame_file_reader
