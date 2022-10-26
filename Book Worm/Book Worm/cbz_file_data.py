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
            elif file.endswith(".jpg"):
                file_info = {"file" : z.read(file), "file_format" : "jpg"}
                list_of_images.append(file_info)
                file_number += 1
            elif file.endswith(".png"):
                file_info = {"file" : z.read(file), "file_format" : "png"}
                list_of_images.append(file_info)
                file_number += 1
            elif file.endswith(".gif"):
                file_info = {"file" : z.read(file), "file_format" : "gif"}
                list_of_images.append(file_info)
                file_number += 1         
            elif file.endswith(".tiff"):
                file_info = {"file" : z.read(file), "file_format" : "tiff"}
                list_of_images.append(file_info)
                file_number += 1    
            elif file.endswith(".bmp"):
                file_info = {"file" : z.read(file), "file_format" : "bmp"}
                list_of_images.append(file_info)
                file_number += 1    
            elif file.endswith(".jpe"):
                file_info = {"file" : z.read(file), "file_format" : "jpe"}
                list_of_images.append(file_info)
                file_number += 1    
            elif file.endswith(".lbm"):
                file_info = {"file" : z.read(file), "file_format" : "lbm"}
                list_of_images.append(file_info)
                file_number += 1  
            elif file.endswith(".pcx"):
                file_info = {"file" : z.read(file), "file_format" : "pcx"} 
                list_of_images.append(file_info)
                file_number += 1    
            elif file.endswith(".pnm"):
                file_info = {"file" : z.read(file), "file_format" : "pnm"}
                list_of_images.append(file_info)
                file_number += 1  
            elif file.endswith(".webp"):
                file_info = {"file" : z.read(file), "file_format" : "webp"}
                list_of_images.append(file_info)
                file_number += 1    
            elif file.endswith(".tga"):
                file_info = {"file" : z.read(file), "file_format" : "tga"}
                list_of_images.append(file_info)
                file_number += 1  
            elif file.endswith(".xcf"):
                file_info = {"file" : z.read(file), "file_format" : "xcf"}
                list_of_images.append(file_info)
                file_number += 1  
            elif file.endswith(".xpm"):
                file_info = {"file" : z.read(file), "file_format" : "xpm"}
                list_of_images.append(file_info)
                file_number += 1    
            elif file.endswith(".xv"):
                file_info = {"file" : z.read(file), "file_format" : "xv"}
                list_of_images.append(file_info)
                file_number += 1  
    return list_of_images

def get_cbz_cover_image(file_path):
    list_of_images = get_cbz_file_content(file_path)
    for image in list_of_images:
        if image["file_format"] == "jpeg":
            file_cover = image
            break
        if image["file_format"] == "jpg":
            file_cover = image
            break
        elif image["file_format"] == "png":
            file_cover = image
            break
        elif image["file_format"] == "gif":
            file_cover = image
            break
        elif image["file_format"] == "xv":
            file_cover = image
            break
        elif image["file_format"] == "xpm":
            file_cover = image
            break
        elif image["file_format"] == "xcf":
            file_cover = image
            break
        elif image["file_format"] == "tga":
            file_cover = image
            break
        elif image["file_format"] == "webp":
            file_cover = image
            break
        elif image["file_format"] == "pnm":
            file_cover = image
            break
        elif image["file_format"] == "tiff":
            file_cover = image
            break
        elif image["file_format"] == "bmp":
            file_cover = image
            break
        elif image["file_format"] == "jpe":
            file_cover = image
            break
        elif image["file_format"] == "lbm":
            file_cover = image
            break
        elif image["file_format"] == "pcx":
            file_cover = image
            break
    return file_cover