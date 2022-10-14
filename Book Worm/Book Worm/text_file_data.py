import os.path

def get_txt_file_content(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        print(lines)
        f.close()
    return lines
# read text from the text file using the file read(), readline(), or readlines() method of the file object.

def get_txt_file_size(file_path):
    return os.path.getsize(file_path)

def get_txt_file_name(file_path):
    file_name_and_extension = os.path.splitext(os.path.basename(file_path))
    return file_name_and_extension[0]