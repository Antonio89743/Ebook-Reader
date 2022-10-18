from asyncio.windows_events import NULL
import glob, os, json, sys
from pydoc import doc
from array import array
from collections import Counter
from json.decoder import JSONDecodeError
import text_file_data
import epub_file_data

local_folders_to_scan_json_file_path = "Book Worm\Book Worm\local_folders_to_scan.json"
local_folders_to_scan_dictionary_file_path = "Book Worm\Book Worm\local_folders_to_scan_dictonary.json"
array_or_pdf_files : array = []
array_or_epub_files : array = []
array_or_mobi_files : array = []
array_or_doc_files : array = []
array_or_docx_files : array = []
array_or_kpf_files : array = []
array_or_txt_files : array = []
array_or_cbr_files : array = []
array_or_cbz_files : array = []
# dictionary_of_valid_files = {
#     "array_of_pdf_files": array_or_pdf_files,
#     "array_of_epub_files": array_or_epub_files,
#     "array_of_mobi_files": array_or_mobi_files,
#     "array_of_doc_files": array_or_doc_files,
#     "array_of_docx_files": array_or_docx_files,
#     "array_of_kpf_files": array_or_kpf_files,
#     "array_of_txt_files": array_or_txt_files,
#     "array_of_cbr_files": array_or_cbr_files,
#     "array_of_cbz_files": array_or_cbz_files}
array_of_valid_files = []

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
    array_of_valid_files = []
    # {
    #     "array_of_pdf_files": array_or_pdf_files,
    #     "array_of_epub_files": array_or_epub_files,
    #     "array_of_mobi_files": array_or_mobi_files,
    #     "array_of_doc_files": array_or_doc_files,
    #     "array_of_docx_files": array_or_docx_files,
    #     "array_of_kpf_files": array_or_kpf_files,
    #     "array_of_txt_files": array_or_txt_files,
    #     "array_of_cbr_files": array_or_cbr_files,
    #     "array_of_cbz_files": array_or_cbz_files}
    data = json.dumps(array_of_valid_files)
    file = open(local_folders_to_scan_dictionary_file_path, 'w')
    file.write(data)
    file.close()    

def scan_folders(folders_to_scan, new_folder_bool):
    global array_of_valid_files
    if type(folders_to_scan) is list:
        for folder in folders_to_scan:
           
            epub_files = glob.glob(folder + "/**/*.epub", recursive = True)
            for epub_file in epub_files:
                print(epub_file)
                absolute_path_to_file = os.path.abspath(epub_file)

                if not any(dictionary["absolute_file_path"] == absolute_path_to_file for dictionary in array_of_valid_files):

                    file_title = epub_file_data.get_epub_book_title(absolute_path_to_file)
                    file_author = epub_file_data.get_epub_book_author(absolute_path_to_file)

                    array_of_valid_files.append({
                        "absolute_file_path" : absolute_path_to_file, 
                        "file_format" : "epub", 
                        "file_name" : file_title, 
                        "file_author" : file_author,
                        "release_date" : None,
                        "date_added" : None,
                        "publisher" : None, 
                        "genre" : None, # this could be an list?
                        "date_most_recently_opened" : None, 
                        "country_of_origin" : None,
                        "language" : None,
                        "file_size" : None,
                        })


            # mobi_files = glob.glob(folder + "/**/*.mobi", recursive = True)
            # for mobi_file in mobi_files:
    #             absolute_path_to_file = os.path.abspath(mobi_file)
    #             if array_or_mobi_files.count(absolute_path_to_file) == 0 :
    #                 array_or_mobi_files.append(absolute_path_to_file)
    #         pdf_files = glob.glob(folder + "/**/*.pdf", recursive = True)
    #         for pdf_file in pdf_files:
    #             absolute_path_to_file = os.path.abspath(pdf_file)
    #             if array_or_pdf_files.count(absolute_path_to_file) == 0 :
    #                 array_or_pdf_files.append(absolute_path_to_file)
    #         doc_files = glob.glob(folder + "/**/*.doc", recursive = True)
    #         for doc_file in doc_files:
    #             absolute_path_to_file = os.path.abspath(doc_file)
    #             if array_or_doc_files.count(absolute_path_to_file) == 0 :
    #                 array_or_doc_files.append(absolute_path_to_file)
    #         docx_files = glob.glob(folder + "/**/*.docx", recursive = True)
    #         for docx_file in docx_files:
    #             absolute_path_to_file = os.path.abspath(docx_file)
    #             if array_or_docx_files.count(absolute_path_to_file) == 0 :
    #                 array_or_docx_files.append(absolute_path_to_file)
    #         kpf_files = glob.glob(folder + "/**/*.kpf", recursive = True)
    #         for kpf_file in kpf_files:
    #             absolute_path_to_file = os.path.abspath(kpf_file)
    #             if array_or_kpf_files.count(absolute_path_to_file) == 0 :
    #                 array_or_kpf_files.append(absolute_path_to_file)
    #         txt_files = glob.glob(folder + "/**/*.txt", recursive = True)
    #         for txt_file in txt_files:
    #             absolute_path_to_file = os.path.abspath(txt_file)
    #             if array_or_txt_files.count(absolute_path_to_file) == 0 :
    #                 array_or_txt_files.append(absolute_path_to_file)
    #         cbr_files = glob.glob(folder + "/**/*.cbr", recursive = True)
    #         for cbr_file in cbr_files:
    #             absolute_path_to_file = os.path.abspath(cbr_file)
    #             if array_or_cbr_files.count(absolute_path_to_file) == 0 :
    #                 array_or_cbr_files.append(absolute_path_to_file)
    #         cbz_files = glob.glob(folder + "/**/*.cbz", recursive = True)
    #         for cbz_file in cbz_files:
    #             absolute_path_to_file = os.path.abspath(cbz_file)
    #             if array_or_cbz_files.count(absolute_path_to_file) == 0 :
    #                 array_or_cbz_files.append(absolute_path_to_file)
        save_local_files_dictionary()
    elif type(folders_to_scan) is str:
        if new_folder_bool == True:
            folders_to_scan = folders_to_scan[1:]
            folders_to_scan = folders_to_scan[:-1]
            folders_to_scan = folders_to_scan[:-1]
            folders_to_scan = folders_to_scan[1:]
            epub_files = glob.glob(folders_to_scan + "/**/*.epub", recursive = True)
            for epub_file in epub_files:
                absolute_path_to_file = os.path.abspath(epub_file) # is this really needed or is there a better way of getting rid of // from epub_file

                if not any(dictionary["absolute_file_path"] == absolute_path_to_file for dictionary in array_of_valid_files):
                    file_title = epub_file_data.get_epub_book_title(absolute_path_to_file)
                    file_author = epub_file_data.get_epub_book_author(absolute_path_to_file)
                    array_of_valid_files.append({
                        "absolute_file_path" : absolute_path_to_file, 
                        "file_format" : "epub", 
                        "file_name" : file_title, 
                        "file_author" : file_author,
                        "release_date" : None,
                        "date_added" : None,
                        "publisher" : None, 
                        "genre" : None, # this could be an list?
                        "date_most_recently_opened" : None, 
                        "country_of_origin" : None,
                        "language" : None,
                        "file_size" : None,
                        })


    #             absolute_path_to_file = os.path.abspath(epub_file)
    #             if array_or_epub_files.count(absolute_path_to_file) == 0 :
    #                 array_or_epub_files.append(absolute_path_to_file)
    #         mobi_files = glob.glob(folders_to_scan + "/**/*.mobi", recursive = True)
    #         for mobi_file in mobi_files:
    #             absolute_path_to_file = os.path.abspath(mobi_file)
    #             if array_or_mobi_files.count(absolute_path_to_file) == 0 :
    #                 array_or_mobi_files.append(absolute_path_to_file)
    #         pdf_files = glob.glob(folders_to_scan + "/**/*.pdf", recursive = True)
    #         for pdf_file in pdf_files:
    #             absolute_path_to_file = os.path.abspath(pdf_file)
    #             if array_or_pdf_files.count(absolute_path_to_file) == 0 :
    #                 array_or_pdf_files.append(absolute_path_to_file)
    #         doc_files = glob.glob(folders_to_scan + "/**/*.doc", recursive = True)
    #         for doc_file in doc_files:
    #             absolute_path_to_file = os.path.abspath(doc_file)
    #             if array_or_doc_files.count(absolute_path_to_file) == 0 :
    #                 array_or_doc_files.append(absolute_path_to_file)
    #         docx_files = glob.glob(folders_to_scan + "/**/*.docx", recursive = True)
    #         for docx_file in docx_files:
    #             absolute_path_to_file = os.path.abspath(docx_file)
    #             if array_or_docx_files.count(absolute_path_to_file) == 0 :
    #                 array_or_docx_files.append(absolute_path_to_file)
    #         kpf_files = glob.glob(folders_to_scan + "/**/*.kpf", recursive = True)
    #         for kpf_file in kpf_files:
    #             absolute_path_to_file = os.path.abspath(kpf_file)
    #             if array_or_kpf_files.count(absolute_path_to_file) == 0 :
    #                 array_or_kpf_files.append(absolute_path_to_file)
    #         txt_files = glob.glob(folders_to_scan + "/**/*.txt", recursive = True)
    #         for txt_file in txt_files:
    #             absolute_path_to_file = os.path.abspath(txt_file)
    #             if array_or_txt_files.count(absolute_path_to_file) == 0 :
    #                 array_or_txt_files.append(absolute_path_to_file)
    #         cbr_files = glob.glob(folders_to_scan + "/**/*.cbr", recursive = True)
    #         for cbr_file in cbr_files:
    #             absolute_path_to_file = os.path.abspath(cbr_file)
    #             if array_or_cbr_files.count(absolute_path_to_file) == 0 :
    #                 array_or_cbr_files.append(absolute_path_to_file)
    #         cbz_files = glob.glob(folders_to_scan + "/**/*.cbz", recursive = True)
    #         for cbz_file in cbz_files:
    #             absolute_path_to_file = os.path.abspath(cbz_file)
    #             if array_or_cbz_files.count(absolute_path_to_file) == 0 :
    #                 array_or_cbz_files.append(absolute_path_to_file)     
            save_local_files_dictionary()
            save_local_folders_array(folders_to_scan)
        elif new_folder_bool == False:
            array_of_valid_files = json.loads(folders_to_scan)
    return array_of_valid_files