from array import array
from asyncio.windows_events import NULL
import configparser
import string
from types import NoneType
from typing import List
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import glob, os
import configparser
import json

def epub2thtml(epub_path):
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters

blacklist = [   '[document]',   'noscript', 'header',   'html', 'meta', 'head','input', 'script',   ]
# there may be more elements you don't want, such as "style", etc.

def chap2text(chap):
    output = ''
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    return output

def thtml2ttext(thtml):
    Output = []
    for html in thtml:
        text =  chap2text(html)
        Output.append(text)
    return Output

def epub2text(epub_path):
    chapters = epub2thtml(epub_path)
    ttext = thtml2ttext(chapters)
    string = list_to_string(ttext)
    return string

def list_to_string(list):
    string = ""
    for i in list:
        string += str(i) + " " 
    return string

def load_folders_to_scan_array():
    file = open(os.path.join(save_folder_path, 'folders_to_scan.json'), 'r')
    json_file_data = file.read()
    json_data = json.loads(json_file_data)
    return json_data

main_window = Tk()
main_window.geometry("900x900")
main_window.title("Epub Reader")
main_window.config(background="#5cfcff")
main_window.rowconfigure(0,weight=1)
main_window.columnconfigure(0,weight=1)
folders_to_scan_array :array = []
save_folder_path = r"C:\Users\anton\AppData\Roaming\BookWorm"
folders_to_scan_array = load_folders_to_scan_array()
previous_frame = None

def scan_folders(folders_to_scan):
    print(type(folders_to_scan))
    if type(folders_to_scan) is list:
        for folder in folders_to_scan:
            epub_files = glob.glob(folder + "/**/*.epub", recursive = True)
            for epub_file in epub_files:
                print(epub_file)

    elif type(folders_to_scan) is str:
        print(folders_to_scan)
        epub_files = glob.glob(folders_to_scan + "/**/*.epub", recursive = True)
        for epub_file in epub_files:
             print(epub_file)

def main_menu():
    frame_main_menu = Frame(main_window, bg='red')
    frame_main_menu.grid(row=0,column=0,sticky='nsew')

    settings_button = Button(frame_main_menu, text='Settings', command=lambda:active_frame(settings(), main_menu()))
    settings_button.pack(side = RIGHT, anchor="s")
    return frame_main_menu

def active_frame(new_frame, previous_frame_is):
    previous_frame = previous_frame_is
    print(previous_frame)
    new_frame.tkraise()

def on_program_opened(): 
    load_folders_to_scan_array()
    scan_folders(folders_to_scan_array)
    active_frame(main_menu(), None)

on_program_opened()

def settings():
    frame_settings = Frame(main_window, bg='blue')
    frame_settings.grid(row=0,column=0,sticky='nsew')

    scan_folders_label = Label(frame_settings, text="Folders scanned for eligible files")
    scan_folders_label.pack()

    settings_button = Button(frame_settings, text='Scanned Folders', command=lambda:active_frame(folders_to_scan(), None))
    settings_button.pack()

    settings_button = Button(frame_settings, text='Return', command=lambda:active_frame(previous_frame, settings()))
    
    settings_button.pack(side = RIGHT, anchor="n")

    
    return frame_settings

def file_opener():
    # on load, put there the last opened file
    pass 

def folders_to_scan():
    folders_to_scan_window = Tk()
    folders_to_scan_window.geometry("400x400")
    folders_to_scan_window.title("Folders To Scan")
    folders_to_scan_window.config(background="yellow")

    add_new_folder_button = Button(folders_to_scan_window, text='+', command=lambda:active_frame(add_new_folder_to_scan()))
    add_new_folder_button.pack()
    
def save_folders_to_scan_array(folders_to_scan_array):
    data = json.dumps(folders_to_scan_array)
    file = open(os.path.join(save_folder_path, 'folders_to_scan.json'), 'w')
    file.write(data)
    file.close()

def add_new_folder_to_scan():
    new_folder = filedialog.askdirectory()
    scan_folders(new_folder)
    check_list_for_duplicates(folders_to_scan_array, new_folder)
    save_folders_to_scan_array(folders_to_scan_array)

def check_list_for_duplicates(list :List, new_list_member):
    duplicate :bool = False
    for list_member in list:
        if list_member == new_list_member:
            duplicate = True
    if duplicate == False:
        list.append(new_list_member)
    elif duplicate == True:
        pass


#  make main menu
#  for every epub file, add book icon, this will require some sort of a grid?
#  on book icon pressed open up the book contents
#  below book icon, have a text with the name of the book, and below that, name of the artist
#  on artist name pressed, go to a screen that will show you all books you've got from that artist

# on settings, top right add button to return to previous screen, whether it be bookreader screen or main menu



# have a vertical list of folders
# those are just div with 2 horizontal texts, one below another
# text 1 shows the name of the folder
# text 2 shows the full path to the folder
# on the right hand side of each div is a X button to remove the particular folder from use
# on the bottom just have done button







# chozen_file_location = "D:\Books\J. R. R. Tolkien\LotR\J.R.R. Tolkien - Lord of the Rings Collection-2000.epub"
# text = Text(main_window, wrap = WORD)
# text.insert(INSERT, epub2text(chozen_file_location))
# text.config(state=DISABLED)
# text.pack() 

main_window.mainloop()

# epub2text("D:\Books\J. R. R. Tolkien\LotR\J.R.R. Tolkien - Lord of the Rings Collection-2000.epub")))

# read folders from google drive
# make it so you can only have one yellow window open at any given time



# upon load, add a picture button in main with the pic of the book cover, below it set name of book, and below that, set name of author