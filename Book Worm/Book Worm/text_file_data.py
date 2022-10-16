import os.path

def get_txt_file_content(file_path):
    with open(file_path) as open_file:
        text = open_file.read()
        open_file.close()
    return text
    
def get_txt_file_size(file_path):
    return os.path.getsize(file_path)

def get_txt_file_name(file_path):
    file_name_and_extension = os.path.splitext(os.path.basename(file_path))
    return file_name_and_extension[0]