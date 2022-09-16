from array import array
import glob, os
import json

def load_folders_to_scan():
    save_folder_path = r"C:\Users\anton\AppData\Roaming\BookWorm"
    folders_to_scan_array :array = []
    file = open(os.path.join(save_folder_path, 'folders_to_scan.json'), 'r')
    json_file_data = file.read()
    folders_to_scan_array = json.loads(json_file_data)
    file.close()
    return folders_to_scan_array
