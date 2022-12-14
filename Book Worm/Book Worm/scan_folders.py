from asyncio.windows_events import NULL
import glob, os, json, sys
from array import array
from collections import Counter
from json.decoder import JSONDecodeError
import cbz_file_data
import cbr_file_data
import text_file_data
import epub_file_data
import audio_file_data_music_tag

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
array_of_valid_files = []

def save_local_folders_array(folders_to_scan):
    with open(local_folders_to_scan_json_file_path, "r+") as file:
        try:
            file_x = open(local_folders_to_scan_json_file_path, "r")
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
            print("Error doing save_local_folders_array func, scan_folders.py")
            if list_folders_to_scan == "":
                folders_to_scan_list : list = []
                folders_to_scan_list.append(folders_to_scan)
                file.write(json.dumps(folders_to_scan_list))
                file.close()     

def save_local_files_dictionary(array_of_valid_files):
    data = json.dumps(array_of_valid_files)
    file = open(local_folders_to_scan_dictionary_file_path, "w")
    file.write(data)
    file.close()    

def scan_folders(folders_to_scan, new_folder_bool):
    global array_of_valid_files
    if type(folders_to_scan) is list:
        for folder in folders_to_scan:
            epub_files = glob.glob(folder + "/**/*.epub", recursive = True)
            for epub_file in epub_files:
                absolute_path_to_file = os.path.abspath(epub_file)
                if not any(dictionary["absolute_file_path"] == absolute_path_to_file for dictionary in array_of_valid_files):
                    file_title = epub_file_data.get_epub_book_title(absolute_path_to_file)
                    file_author = epub_file_data.get_epub_book_author(absolute_path_to_file)
                    file_cover = epub_file_data.get_epub_cover_image_path(absolute_path_to_file)
                    array_of_valid_files.append({
                        "absolute_file_path" : absolute_path_to_file, 
                        "file_format" : "epub", 
                        "file_name" : file_title, 
                        "file_author" : file_author,
                        "file_cover" : file_cover,
                        "release_date" : None,
                        "date_added" : None,
                        "publisher" : None, 
                        "genre" : None, # this could be an list?
                        "date_most_recently_opened" : None, 
                        "country_of_origin" : None,
                        "language" : None,
                        "file_size" : None})
            txt_files = glob.glob(folders_to_scan + "/**/*.txt", recursive = True)
            for txt_file in txt_files:
                absolute_path_to_file = os.path.abspath(txt_file)
                if not any(dictionary["absolute_file_path"] == absolute_path_to_file for dictionary in array_of_valid_files):
                    file_title = text_file_data.get_txt_file_name(absolute_path_to_file)
                    array_of_valid_files.append({
                        "absolute_file_path" : absolute_path_to_file, 
                        "file_format" : "txt", 
                        "file_name" : file_title, 
                        "file_author" : None,
                        "release_date" : None,
                        "date_added" : None,
                        "publisher" : None, 
                        "genre" : None, # this could be an list?
                        "date_most_recently_opened" : None, 
                        "country_of_origin" : None,
                        "language" : None,
                        "file_size" : None})     
            cbz_files = glob.glob(folders_to_scan + "/**/*.cbz", recursive = True)
            cbr_files = glob.glob(folders_to_scan + "/**/*.cbr", recursive = True)
            cb_files = {"cbz_files" : cbz_files, "cbr_files" : cbr_files}
            for cbz_file in cbz_files:
                absolute_path_to_file = os.path.abspath(cbz_file)
                if not any(dictionary["absolute_file_path"] == absolute_path_to_file for dictionary in array_of_valid_files):
                    file_title = cbz_file_data.get_cbz_file_title(absolute_path_to_file)
                    file_cover = cbz_file_data.get_cbz_cover_image(absolute_path_to_file)
                    array_of_valid_files.append({
                        "absolute_file_path" : absolute_path_to_file, 
                        "file_format" : "cbz", 
                        "file_name" : file_title, 
                        "file_author" : None,
                        "file_cover" : file_cover,
                        "release_date" : None,
                        "date_added" : None,
                        "publisher" : None, 
                        "genre" : None, # this could be an list?
                        "date_most_recently_opened" : None, 
                        "country_of_origin" : None,
                        "language" : None,
                        "file_size" : None})
            mp3_files = glob.glob(folders_to_scan + "/**/*.mp3", recursive = True)
            wav_files = glob.glob(folders_to_scan + "/**/*.wav", recursive = True)
            ogg_files = glob.glob(folders_to_scan + "/**/*.ogg", recursive = True)
            aac_files = glob.glob(folders_to_scan + "/**/*.aac", recursive = True)
            flac_files = glob.glob(folders_to_scan + "/**/*.flac", recursive = True)
            music_tag_compatible_audio_files = []
            music_tag_compatible_audio_files.extend(mp3_files)
            music_tag_compatible_audio_files.extend(wav_files)
            music_tag_compatible_audio_files.extend(ogg_files)
            music_tag_compatible_audio_files.extend(aac_files)
            music_tag_compatible_audio_files.extend(flac_files)
            list_of_albums = []
            list_of_tracks = []
            for music_tag_compatible_audio_file in music_tag_compatible_audio_files:
                absolute_path_to_file = os.path.abspath(music_tag_compatible_audio_file)
                if absolute_path_to_file.endswith(".mp3"):
                    file_format = "mp3"
                elif absolute_path_to_file.endswith(".wav"):
                    file_format = "wav"
                elif absolute_path_to_file.endswith(".ogg"):
                    file_format = "ogg"
                elif absolute_path_to_file.endswith(".aac"):
                    file_format = "aac"
                elif absolute_path_to_file.endswith(".flac"):
                    file_format = "flac"
                file_album_title = audio_file_data_music_tag.get_audio_file_data_music_tag_album_name(absolute_path_to_file)
                file_album_artist = audio_file_data_music_tag.get_audio_file_data_music_tag_album_artist(absolute_path_to_file)
                file_album_total_track_number = audio_file_data_music_tag.get_audio_file_data_music_tag_total_tracks(absolute_path_to_file)
                file_album_total_disk_number = audio_file_data_music_tag.get_audio_file_data_music_tag_total_discs(absolute_path_to_file)
                file_album_release_year = audio_file_data_music_tag.get_audio_file_data_music_tag_release_year(absolute_path_to_file)
                album_dictionary = {
                    "file_album_title" : file_album_title,
                    "file_album_artist" : file_album_artist,
                    "file_album_total_track_number" : file_album_total_track_number,
                    "file_album_total_disk_number" : file_album_total_disk_number,
                    "file_album_release_year" : file_album_release_year}
                list_of_albums.append(album_dictionary)
                track_title = audio_file_data_music_tag.get_audio_file_data_music_tag_title(absolute_path_to_file)
                track_artist = audio_file_data_music_tag.get_audio_file_data_music_tag_artist(absolute_path_to_file)
                track_number = audio_file_data_music_tag.get_audio_file_data_music_tag_track_number(absolute_path_to_file)
                track_genre = audio_file_data_music_tag.get_audio_file_data_music_tag_genre(absolute_path_to_file)
                track_lenght = audio_file_data_music_tag.get_audio_file_data_music_tag_length(absolute_path_to_file)
                track_dictionary = {
                    "track_album_title" : file_album_title,
                    "file_album_artist" : file_album_artist,
                    "file_album_total_track_number" : file_album_total_track_number,
                    "file_album_total_disk_number" : file_album_total_disk_number,
                    "file_album_release_year" : file_album_release_year,
                    "track_title" : track_title,
                    "track_artist" : track_artist,
                    "track_number" : track_number,
                    "track_genre" : track_genre,
                    "track_lenght" : track_lenght,
                    "absolute_file_path" : absolute_path_to_file,
                    "file_format" : file_format}
                list_of_tracks.append(track_dictionary)
            list_of_unique_albums = list(map(dict, set(tuple(sorted(sub.items())) for sub in list_of_albums)))
            for album in list_of_unique_albums:
                album_genres = []
                album_tracks_dictionary = []
                for track in list_of_tracks:
                    if album["file_album_title"] == track["track_album_title"] and album["file_album_artist"] == track["file_album_artist"]:
                        if album["file_album_total_track_number"] == track["file_album_total_track_number"] and album["file_album_total_disk_number"] == track["file_album_total_disk_number"]:
                            album_tracks_dictionary.append(track)
                            album_genres.append(track["track_genre"])
                            album_genres = [*set(album_genres)]
                            album_file_format = track["file_format"] + "_album"
                array_of_valid_files.append({
                    "absolute_file_path" : None, 
                    "file_format" : album_file_format,
                    "file_name" : album["file_album_title"], 
                    "file_author" : album["file_album_artist"],
                    "file_cover" : None,
                    "release_date" : album["file_album_release_year"],
                    "album_tracks_dictionary" : album_tracks_dictionary,
                    "date_added" : None,
                    "publisher" : None, 
                    "album_genre" : album_genres,
                    "date_most_recently_opened" : None, 
                    "country_of_origin" : None,
                    "language" : None,
                    "file_size" : None})

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
    #         cbr_files = glob.glob(folder + "/**/*.cbr", recursive = True)
    #         for cbr_file in cbr_files:
    #             absolute_path_to_file = os.path.abspath(cbr_file)
    #             if array_or_cbr_files.count(absolute_path_to_file) == 0 :
    #                 array_or_cbr_files.append(absolute_path_to_file)
        save_local_files_dictionary(array_of_valid_files)
    elif type(folders_to_scan) is str:
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
                file_cover = epub_file_data.get_epub_cover_image_path(absolute_path_to_file)
                array_of_valid_files.append({
                    "absolute_file_path" : absolute_path_to_file, 
                    "file_format" : "epub", 
                    "file_name" : file_title, 
                    "file_author" : file_author,
                    "file_cover" : file_cover,
                    "release_date" : None,
                    "date_added" : None,
                    "publisher" : None, 
                    "genre" : None, # this could be an list?
                    "date_most_recently_opened" : None, 
                    "country_of_origin" : None,
                    "language" : None,
                    "file_size" : None})
        txt_files = glob.glob(folders_to_scan + "/**/*.txt", recursive = True)
        for txt_file in txt_files:
            absolute_path_to_file = os.path.abspath(txt_file)
            if not any(dictionary["absolute_file_path"] == absolute_path_to_file for dictionary in array_of_valid_files):
                file_title = text_file_data.get_txt_file_name(absolute_path_to_file)
                array_of_valid_files.append({
                    "absolute_file_path" : absolute_path_to_file, 
                    "file_format" : "txt", 
                    "file_name" : file_title, 
                    "file_author" : None,
                    "release_date" : None,
                    "date_added" : None,
                    "publisher" : None, 
                    "genre" : None, # this could be an list?
                    "date_most_recently_opened" : None, 
                    "country_of_origin" : None,
                    "language" : None,
                    "file_size" : None})
        cb7_files = glob.glob(folders_to_scan + "/**/*.cb7", recursive = True)
        cba_files = glob.glob(folders_to_scan + "/**/*.cba", recursive = True)
        cbt_files = glob.glob(folders_to_scan + "/**/*.cbt", recursive = True)          
        cbz_files = glob.glob(folders_to_scan + "/**/*.cbz", recursive = True)
        for cbz_file in cbz_files:
            absolute_path_to_file = os.path.abspath(cbz_file)
            if not any(dictionary["absolute_file_path"] == absolute_path_to_file for dictionary in array_of_valid_files):
                file_title = cbz_file_data.get_cbz_file_title(absolute_path_to_file)
                file_cover = cbz_file_data.get_cbz_cover_image(absolute_path_to_file)
                array_of_valid_files.append({
                    "absolute_file_path" : absolute_path_to_file, 
                    "file_format" : "cbz", 
                    "file_name" : file_title, 
                    "file_author" : None,
                    "file_cover" : file_cover,
                    "release_date" : None,
                    "date_added" : None,
                    "publisher" : None, 
                    "genre" : None, # this could be an list?
                    "date_most_recently_opened" : None, 
                    "country_of_origin" : None,
                    "language" : None,
                    "file_size" : None})
        cbr_files = glob.glob(folders_to_scan + "/**/*.cbr", recursive = True)
        for cbr_file in cbr_files:
            absolute_path_to_file = os.path.abspath(cbr_file)
            if not any(dictionary["absolute_file_path"] == absolute_path_to_file for dictionary in array_of_valid_files):
                file_title = cbr_file_data.get_cbr_file_title(absolute_path_to_file)
                file_cover = cbr_file_data.get_cbr_cover_image(absolute_path_to_file)
                array_of_valid_files.append({
                    "absolute_file_path" : absolute_path_to_file, 
                    "file_format" : "cbr", 
                    "file_name" : file_title, 
                    "file_author" : None,
                    "file_cover" : file_cover,
                    "release_date" : None,
                    "date_added" : None,
                    "publisher" : None, 
                    "genre" : None, # this could be an list?
                    "date_most_recently_opened" : None, 
                    "country_of_origin" : None,
                    "language" : None,
                    "file_size" : None})        
        mp3_files = glob.glob(folders_to_scan + "/**/*.mp3", recursive = True)
        wav_files = glob.glob(folders_to_scan + "/**/*.wav", recursive = True)
        ogg_files = glob.glob(folders_to_scan + "/**/*.ogg", recursive = True)
        aac_files = glob.glob(folders_to_scan + "/**/*.aac", recursive = True)
        flac_files = glob.glob(folders_to_scan + "/**/*.flac", recursive = True)
        music_tag_compatible_audio_files = []
        music_tag_compatible_audio_files.extend(mp3_files)
        music_tag_compatible_audio_files.extend(wav_files)
        music_tag_compatible_audio_files.extend(ogg_files)
        music_tag_compatible_audio_files.extend(aac_files)
        music_tag_compatible_audio_files.extend(flac_files)
        list_of_albums = []
        list_of_tracks = []
        for music_tag_compatible_audio_file in music_tag_compatible_audio_files:
            absolute_path_to_file = os.path.abspath(music_tag_compatible_audio_file)
            if absolute_path_to_file.endswith(".mp3"):
                file_format = "mp3"
            elif absolute_path_to_file.endswith(".wav"):
                file_format = "wav"
            elif absolute_path_to_file.endswith(".ogg"):
                file_format = "ogg"
            elif absolute_path_to_file.endswith(".aac"):
                file_format = "aac"
            elif absolute_path_to_file.endswith(".flac"):
                file_format = "flac"
            file_album_title = audio_file_data_music_tag.get_audio_file_data_music_tag_album_name(absolute_path_to_file)
            file_album_artist = audio_file_data_music_tag.get_audio_file_data_music_tag_album_artist(absolute_path_to_file)
            file_album_total_track_number = audio_file_data_music_tag.get_audio_file_data_music_tag_total_tracks(absolute_path_to_file)
            file_album_total_disk_number = audio_file_data_music_tag.get_audio_file_data_music_tag_total_discs(absolute_path_to_file)
            file_album_release_year = audio_file_data_music_tag.get_audio_file_data_music_tag_release_year(absolute_path_to_file)
            album_dictionary = {
                "file_album_title" : file_album_title,
                "file_album_artist" : file_album_artist,
                "file_album_total_track_number" : file_album_total_track_number,
                "file_album_total_disk_number" : file_album_total_disk_number,
                "file_album_release_year" : file_album_release_year}
            list_of_albums.append(album_dictionary)
            track_title = audio_file_data_music_tag.get_audio_file_data_music_tag_title(absolute_path_to_file)
            track_artist = audio_file_data_music_tag.get_audio_file_data_music_tag_artist(absolute_path_to_file)
            track_number = audio_file_data_music_tag.get_audio_file_data_music_tag_track_number(absolute_path_to_file)
            track_genre = audio_file_data_music_tag.get_audio_file_data_music_tag_genre(absolute_path_to_file)
            track_lenght = audio_file_data_music_tag.get_audio_file_data_music_tag_length(absolute_path_to_file)
            track_dictionary = {
                "track_album_title" : file_album_title,
                "file_album_artist" : file_album_artist,
                "file_album_total_track_number" : file_album_total_track_number,
                "file_album_total_disk_number" : file_album_total_disk_number,
                "file_album_release_year" : file_album_release_year,
                "track_title" : track_title,
                "track_artist" : track_artist,
                "track_number" : track_number,
                "track_genre" : track_genre,
                "track_lenght" : track_lenght,
                "absolute_file_path" : absolute_path_to_file,
                "file_format" : file_format}
            list_of_tracks.append(track_dictionary)
        list_of_unique_albums = list(map(dict, set(tuple(sorted(sub.items())) for sub in list_of_albums)))
        for album in list_of_unique_albums:
            album_genres = []
            album_tracks_dictionary = []
            for track in list_of_tracks:
                if album["file_album_title"] == track["track_album_title"] and album["file_album_artist"] == track["file_album_artist"]:
                    if album["file_album_total_track_number"] == track["file_album_total_track_number"] and album["file_album_total_disk_number"] == track["file_album_total_disk_number"]:
                        album_tracks_dictionary.append(track)
                        album_genres.append(track["track_genre"])
                        album_genres = [*set(album_genres)]
                        album_file_format = track["file_format"] + "_album"
            array_of_valid_files.append({
                "absolute_file_path" : None, 
                "file_format" : album_file_format,
                "file_name" : album["file_album_title"], 
                "file_author" : album["file_album_artist"],
                "file_cover" : None,
                "release_date" : album["file_album_release_year"],
                "album_tracks_dictionary" : album_tracks_dictionary,
                "date_added" : None,
                "publisher" : None, 
                "album_genre" : album_genres,
                "date_most_recently_opened" : None, 
                "country_of_origin" : None,
                "language" : None,
                "file_size" : None})
        
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
    if new_folder_bool == True:
            save_local_files_dictionary(array_of_valid_files)
            save_local_folders_array(folders_to_scan)
    
        # elif new_folder_bool == False:
        #     array_of_valid_files = json.loads(folders_to_scan)
    return array_of_valid_files