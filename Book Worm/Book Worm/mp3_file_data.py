import os
import music_tag
from datetime import datetime

def get_mp3_file_modified_time(file_path):
    unix_time = os.path.getmtime(file_path)
    return datetime.fromtimestamp(unix_time).strftime("%d/%m/%Y %H:%M:%S")

def get_mp3_file_title(file_path):
    file = music_tag.load_file(file_path)
    return file["title"]

def get_mp3_file_artist(file_path):
    file = music_tag.load_file(file_path)
    return file["artist"]

def get_mp3_file_release_year(file_path):
    file = music_tag.load_file(file_path)
    return file["year"]

def get_mp3_file_album(file_path):
    file = music_tag.load_file(file_path)
    return file["album"]

def get_mp3_file_genre(file_path):
    file = music_tag.load_file(file_path)
    return file["genre"]

def get_mp3_file_album_artist(file_path):
    file = music_tag.load_file(file_path)
    return file["albumartist"]

def get_mp3_file_track_title(file_path):
    file = music_tag.load_file(file_path)
    return file["tracktitle"]

def get_mp3_file_track_number(file_path):
    file = music_tag.load_file(file_path)
    return file["tracknumber"]

def get_mp3_file_total_discs(file_path):
    file = music_tag.load_file(file_path)
    return file["totaldiscs"]

def get_mp3_file_total_tracks(file_path):
    file = music_tag.load_file(file_path)
    return file["totaltracks"]   

# def get_mp3_file_length(file_path):
#     file = music_tag.load_file(file_path)
#     return file["length"]   

# print(get_mp3_file_length(r"E:\Music\Black Pistol Fire\Black Pistol Fire - 2011 - Black Pistol Fire [FLAC]/01 - Cold Sun.flac"))


# def get_mp3_file_artwork(file_path):
#     file = music_tag.load_file(file_path)
#     x = file["artwork"]
#     print(x.value.data)

# get_mp3_file_artwork(r"E:\Music\Black Pistol Fire\Black Pistol Fire - 2011 - Black Pistol Fire [FLAC]/01 - Cold Sun.flac")




# comment
# compilation
# composer
# discnumber
# lyrics
# isrc
# #bitrate (read only)
# #codec (read only)
# #length (read only)
# #channels (read only)
# #bitspersample (read only)
# #samplerate (read only)


# art = f['artwork']

# # Note: `art` is a MetadataItem. Use ``art.value`` if there is
# #       only one image embeded in the file. This will raise a
# #       ValueError if there is more than one image. You can also
# #       use ``art.first``, or iterate through ``art.values``.

# art.first.mime  # -> 'image/jpeg'
# art.first.width  # -> 1280
# art.first.height  # -> 1280
# art.first.depth  # -> 24
# art.first.data  # -> b'... raw image data ...'