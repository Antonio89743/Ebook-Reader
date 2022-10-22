import zipfile
import os.path
from datetime import datetime

def get_cbz_file_modified_time(file_path):
    unix_time = os.path.getmtime(file_path)
    return datetime.fromtimestamp(unix_time).strftime("%d/%m/%Y %H:%M:%S")

def get_cbz_file_name(file_path):
    return file_path
#     with zipfile.ZipFile(file_path) as z:
#         file_list = z.namelist()
#         print(file_list)

def get_cbz_file_content(file_path):
    list_of_images = []
    with zipfile.ZipFile(file_path) as z:
        file_list = z.namelist()
        for file in file_list:
            if file.endswith(".jpeg"):
                list_of_images.append(z.read(file))
#  here store that file is jpeg

    print() # print the first file you've got, that will probably be the cover item for main menu widget

#  sort this here, sort the widget cover, then do the file reader screen

    return list_of_images


    # PNG, JPEG, or GIF file formats


get_cbz_file_content("trash\Attack on Titan v01 (2010) (Digital SD) (KG Manga).cbz")