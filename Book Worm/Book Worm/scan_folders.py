from array import array
import glob, os

array_or_pdf_files : array = []
array_or_epub_files : array = []
array_or_mobi_files : array = []
dictionary_of_valid_files = {
    "array_of_pdf_files": array_or_pdf_files,
    "array_of_epub_files": array_or_epub_files,
    "array_of_mobi_files": array_or_mobi_files,
}
#  in array of x files also place items you get from the cash scan
def scan_folders(folders_to_scan):
    if type(folders_to_scan) is list:
        for folder in folders_to_scan:

            epub_files = glob.glob(folder + "/**/*.epub", recursive = True)
            for epub_file in epub_files:
                absolute_path_to_file = os.path.abspath(epub_file)
                if array_or_epub_files.count(absolute_path_to_file) > 0 :
                    pass
                else:
                    array_or_epub_files.append(absolute_path_to_file)

            mobi_files = glob.glob(folder + "/**/*.mobi", recursive = True)
            for mobi_file in epub_files:
                absolute_path_to_file = os.path.abspath(mobi_file)
                if array_or_mobi_files.count(absolute_path_to_file) > 0 :
                    pass
                else:
                    array_or_mobi_files.append(absolute_path_to_file)

            pdf_files = glob.glob(folder + "/**/*.pdf", recursive = True)
            for pdf_file in epub_files:
                absolute_path_to_file = os.path.abspath(pdf_file)
                if array_or_pdf_files.count(absolute_path_to_file) > 0 :
                    pass
                else:
                    array_or_pdf_files.append(absolute_path_to_file)

    elif type(folders_to_scan) is str: #this will still mean that you'll have to create all widgets again, mark the new un widgeted files
        # make a seperate list and just call make main menu widgets func with that list instead

        epub_files = glob.glob(folders_to_scan + "/**/*.epub", recursive = True)
        for epub_file in epub_files:
            absolute_path_to_file = os.path.abspath(epub_file)
            if array_or_epub_files.count(absolute_path_to_file) > 0 :
                pass
            else:
                array_or_epub_files.append(absolute_path_to_file)

        mobi_files = glob.glob(folders_to_scan + "/**/*.mobi", recursive = True)
        for mobi_file in epub_files:
            absolute_path_to_file = os.path.abspath(mobi_file)
            if array_or_mobi_files.count(absolute_path_to_file) > 0 :
                pass
            else:
                array_or_mobi_files.append(absolute_path_to_file)

        pdf_files = glob.glob(folders_to_scan + "/**/*.pdf", recursive = True)
        for pdf_file in epub_files:
            absolute_path_to_file = os.path.abspath(pdf_file)
            if array_or_pdf_files.count(absolute_path_to_file) > 0 :
                pass
            else:
                array_or_pdf_files.append(absolute_path_to_file)

    return dictionary_of_valid_files
