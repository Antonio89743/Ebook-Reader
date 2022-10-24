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
    file_number :int = 0
    with zipfile.ZipFile(file_path) as z:
        file_list = z.namelist()
        for file in file_list:
            if file.endswith(".jpeg"):
                file_info = {"file" : z.read(file), "file_format" : "jpeg"}
                list_of_images.append(file_info)
                file_number += 1
    return list_of_images

def get_cbz_cover_image(file_path):
    list_of_images = get_cbz_file_content(file_path)
    for image in list_of_images:
        if image["file_format"] == "jpeg":
            file_cover = image
            break
    return file_cover

# PNG, JPEG, or GIF file formats, among others