import glob, os, json
from array import array

local_folders_to_scan_json_file_path = "Book Worm\Book Worm\local_folders_to_scan.json"
local_folders_to_scan_dictionary_file_path = "Book Worm\Book Worm\local_folders_to_scan_dictonary.json"
array_or_pdf_files : array = []
array_or_epub_files : array = []
array_or_mobi_files : array = []
list_folders_to_scan : list = []
dictionary_of_valid_files = {
    "array_of_pdf_files": array_or_pdf_files,
    "array_of_epub_files": array_or_epub_files,
    "array_of_mobi_files": array_or_mobi_files,
}

def save_local_folders_array(folders_to_scan):
    global list_folders_to_scan
    file = open(local_folders_to_scan_json_file_path, "r")
    list_folders_to_scan = file.read()


    if list_folders_to_scan != "":
        print(list_folders_to_scan)
        print(type(list_folders_to_scan))

        print(type([list_folders_to_scan]))
        file.close()

        # this still isn't laoding as a list but as a string

        if list_folders_to_scan.count(str(folders_to_scan)) == 0 :
            [list_folders_to_scan].append(folders_to_scan)
            print(list_folders_to_scan)
    #     data = json.dumps(list_folders_to_scan)
    #     file = open(local_folders_to_scan_json_file_path, 'w')
    #     file.write(data)
    #     file.close()    
    # elif list_folders_to_scan == "":
    #     data = json.dumps([folders_to_scan])
    #     file = open(local_folders_to_scan_json_file_path, 'a')
    #     file.write(data)
    #     file.close()      

def save_local_files_dictionary():
    dictionary_of_valid_files = {
    "array_of_pdf_files": array_or_pdf_files,
    "array_of_epub_files": array_or_epub_files,
    "array_of_mobi_files": array_or_mobi_files,
    }
    print(dictionary_of_valid_files)
    data = json.dumps(dictionary_of_valid_files)
    file = open(local_folders_to_scan_dictionary_file_path, 'w')
    file.write(data)
    file.close()    

def scan_folders(folders_to_scan, new_folder_bool):
    global dictionary_of_valid_files
    print(type(folders_to_scan))
    if type(folders_to_scan) is list:
        print("eng")
        print(folders_to_scan)
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
            dictonary_of_folders_to_scan = json.loads(folders_to_scan)
            dictionary_of_valid_files = dictonary_of_folders_to_scan

    return dictionary_of_valid_files