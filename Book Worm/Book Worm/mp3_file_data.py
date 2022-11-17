import os
import music_tag
from datetime import datetime

def get_mp3_file_modified_time(file_path):
    unix_time = os.path.getmtime(file_path)
    return datetime.fromtimestamp(unix_time).strftime("%d/%m/%Y %H:%M:%S")

def get_mp3_file_title(file_path):
    file = music_tag.load_file(file_path)
    return str(file["title"].values)[2:-2]

def get_mp3_file_artist(file_path):
    file = music_tag.load_file(file_path)
    return str(file["artist"].values)[2:-2] 

def get_mp3_file_release_year(file_path):
    file = music_tag.load_file(file_path)
    return str(file["year"].values)[2:-2]

def get_mp3_file_album_name(file_path):
    file = music_tag.load_file(file_path)
    return str(file["album"].values)[2:-2]

def get_mp3_file_genre(file_path):
    file = music_tag.load_file(file_path)
    #  what if there are multiple grenres, return a list of them?
    return str(file["genre"].values)[2:-2]

def get_mp3_file_album_artist(file_path):
    file = music_tag.load_file(file_path)
    return str(file["albumartist"].values)[2:-2]

def get_mp3_file_track_title(file_path):
    file = music_tag.load_file(file_path)
    return str(file["tracktitle"].values)[2:-2]  

def get_mp3_file_track_number(file_path):
    file = music_tag.load_file(file_path)
    return str(file["tracknumber"].values)[2:-2] 

def get_mp3_file_total_discs(file_path):
    file = music_tag.load_file(file_path)
    return str(file["totaldiscs"].values)[2:-2]  

def get_mp3_file_total_tracks(file_path):
    file = music_tag.load_file(file_path)
    return str(file["totaltracks"].values)[2:-2]

def get_mp3_file_artwork(file_path):
    file = music_tag.load_file(file_path)
    return file["artwork"].value.data

def get_mp3_file_length(file_path):
    file = music_tag.load_file(file_path)
    string_lenght = str(file["#length"].values)[1:-1]
    seconds = float(string_lenght)
    seconds = seconds % (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    if hours > 0:
        return "%d:%02d:%02d" % (hours, minutes, seconds)
    else:
        if minutes > 0:
            return "%02d:%02d" % (minutes, seconds)
        else:
            return "%0d:%02d" % (minutes, seconds)

# print(get_mp3_file_length(r"E:\Music\Larkin Poe\Larkin Poe - Kindred Spirits (2020) - WEB FLAC/01. Hellhound On My Trail.flac"))

# comment
# compilation
# composer
# discnumber
# lyrics
# isrc
# #bitrate (read only)
# #codec (read only)
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