import glob, os, json, sys
from array import array
from json.decoder import JSONDecodeError

local_folders_to_scan_json_file_path = "Book Worm\Book Worm\local_folders_to_scan.json"
local_folders_to_scan_dictionary_file_path = "Book Worm\Book Worm\local_folders_to_scan_dictonary.json"
array_or_pdf_files : array = []
array_or_epub_files : array = []
array_or_mobi_files : array = []

dictionary_of_valid_files = {
    "array_of_pdf_files": array_or_pdf_files,
    "array_of_epub_files": array_or_epub_files,
    "array_of_mobi_files": array_or_mobi_files,
}

def save_local_folders_array(folders_to_scan):
    with open(local_folders_to_scan_json_file_path, 'r+') as file:
        try:
            file_x = open(local_folders_to_scan_json_file_path, 'r')
            list_folders_to_scan = file_x.read()
            if list_folders_to_scan == "":
                folders_to_scan_list : list = []
                folders_to_scan_list.append(folders_to_scan)
                file.write(json.dumps(folders_to_scan_list))
                file.close()     
            else:
                helper_file = open(local_folders_to_scan_json_file_path, "r")
                json_file_data = helper_file.read()
                file_content = json.loads(json_file_data)
                if file_content.count(folders_to_scan) == 0 :
                    file_content.append(folders_to_scan)
                    file.write(json.dumps(file_content))
                file.close()     
                helper_file.close()
        except JSONDecodeError:
            print("error saving save_local_folders_array")
            if list_folders_to_scan == "":
                folders_to_scan_list : list = []
                folders_to_scan_list.append(folders_to_scan)
                file.write(json.dumps(folders_to_scan_list))
                file.close()     

def save_local_files_dictionary():
    dictionary_of_valid_files = {
    "array_of_pdf_files": array_or_pdf_files,
    "array_of_epub_files": array_or_epub_files,
    "array_of_mobi_files": array_or_mobi_files,
    }
    data = json.dumps(dictionary_of_valid_files)
    file = open(local_folders_to_scan_dictionary_file_path, 'w')
    file.write(data)
    file.close()    

def scan_folders(folders_to_scan, new_folder_bool):
    global dictionary_of_valid_files
    if type(folders_to_scan) is list:
        for folder in folders_to_scan:
            epub_files = glob.glob(folder + "/**/*.epub", recursive = True)
            for epub_file in epub_files:
                absolute_path_to_file = os.path.abspath(epub_file)
                if array_or_epub_files.count(absolute_path_to_file) == 0 :
                    array_or_epub_files.append(absolute_path_to_file)
            mobi_files = glob.glob(folder + "/**/*.mobi", recursive = True)
            for mobi_file in mobi_files:
                absolute_path_to_file = os.path.abspath(mobi_file)
                if array_or_mobi_files.count(absolute_path_to_file) == 0 :
                    array_or_mobi_files.append(absolute_path_to_file)
            pdf_files = glob.glob(folder + "/**/*.pdf", recursive = True)
            for pdf_file in pdf_files:
                absolute_path_to_file = os.path.abspath(pdf_file)
                if array_or_pdf_files.count(absolute_path_to_file) == 0 :
                    array_or_pdf_files.append(absolute_path_to_file)
        save_local_files_dictionary()
    elif type(folders_to_scan) is str:
        if new_folder_bool == True:
            folders_to_scan = folders_to_scan[1:]
            folders_to_scan = folders_to_scan[:-1]
            folders_to_scan = folders_to_scan[:-1]
            folders_to_scan = folders_to_scan[1:]
            epub_files = glob.glob(folders_to_scan + "/**/*.epub", recursive = True)
            for epub_file in epub_files:
                absolute_path_to_file = os.path.abspath(epub_file)
                if array_or_epub_files.count(absolute_path_to_file) == 0 :
                    array_or_epub_files.append(absolute_path_to_file)
            mobi_files = glob.glob(folders_to_scan + "/**/*.mobi", recursive = True)
            for mobi_file in mobi_files:
                absolute_path_to_file = os.path.abspath(mobi_file)
                if array_or_mobi_files.count(absolute_path_to_file) == 0 :
                    array_or_mobi_files.append(absolute_path_to_file)
            pdf_files = glob.glob(folders_to_scan + "/**/*.pdf", recursive = True)
            for pdf_file in pdf_files:
                absolute_path_to_file = os.path.abspath(pdf_file)
                if array_or_pdf_files.count(absolute_path_to_file) == 0 :
                    array_or_pdf_files.append(absolute_path_to_file)
            save_local_files_dictionary()
            save_local_folders_array(folders_to_scan)
        elif new_folder_bool == False:
            dictionary_of_valid_files = json.loads(folders_to_scan)
    return dictionary_of_valid_files