from array import array
import os
import zipfile
from lxml import etree
import html_file_data
from datetime import datetime
import os.path
import base64
import io

namespaces = {
   "calibre":"http://calibre.kovidgoyal.net/2009/metadata",
   "dc":"http://purl.org/dc/elements/1.1/",
   "dcterms":"http://purl.org/dc/terms/",
   "opf":"http://www.idpf.org/2007/opf",
   "u":"urn:oasis:names:tc:opendocument:xmlns:container",
   "xsi":"http://www.w3.org/2001/XMLSchema-instance"}

def get_epub_file_modified_time(file_path):
    unix_time = os.path.getmtime(file_path)
    return datetime.fromtimestamp(unix_time).strftime("%d/%m/%Y %H:%M:%S")

def get_epub_cover_image_path(file_path):
    with zipfile.ZipFile(file_path) as z:
        t = etree.fromstring(z.read("META-INF/container.xml"))
        rootfile_path =  t.xpath("/u:container/u:rootfiles/u:rootfile", namespaces=namespaces)[0].get("full-path")
        t = etree.fromstring(z.read(rootfile_path))
        cover_id = t.xpath("//opf:metadata/opf:meta[@name='cover']", namespaces=namespaces)[0].get("content")
        cover_href = t.xpath("//opf:manifest/opf:item[@id='" + cover_id + "']", namespaces=namespaces)[0].get("href")
        if rootfile_path:
         if os.path.dirname(rootfile_path) == "":
            cover_path = cover_href
         else:
            cover_path = os.path.dirname(rootfile_path) + "/" + cover_href
        return cover_path

def get_epub_book_title(file_path):
    with zipfile.ZipFile(file_path) as z:
        t = etree.fromstring(z.read("META-INF/container.xml"))
        rootfile_path =  t.xpath("/u:container/u:rootfiles/u:rootfile", namespaces=namespaces)[0].get("full-path")
        t = etree.fromstring(z.read(rootfile_path))
        cover_id = t.xpath("//opf:metadata", namespaces=namespaces)[0]
        file_title = cover_id.find('{http://purl.org/dc/elements/1.1/}title')
        if hasattr(file_title, 'text'):
            return file_title.text

def get_epub_book_author(file_path):
    with zipfile.ZipFile(file_path) as z:
        t = etree.fromstring(z.read("META-INF/container.xml"))
        rootfile_path =  t.xpath("/u:container/u:rootfiles/u:rootfile", namespaces=namespaces)[0].get("full-path")
        t = etree.fromstring(z.read(rootfile_path))
        cover_id = t.xpath("//opf:metadata", namespaces=namespaces)[0]
        file_title = cover_id.find('{http://purl.org/dc/elements/1.1/}creator')
        if hasattr(file_title, 'text'):
            return file_title.text

def get_epub_book_publisher(file_path):
    with zipfile.ZipFile(file_path) as z:
        t = etree.fromstring(z.read("META-INF/container.xml"))
        rootfile_path =  t.xpath("/u:container/u:rootfiles/u:rootfile", namespaces=namespaces)[0].get("full-path")
        t = etree.fromstring(z.read(rootfile_path))
        cover_id = t.xpath("//opf:metadata", namespaces=namespaces)[0]
        file_publisher = cover_id.find('{http://purl.org/dc/elements/1.1/}publisher')
        if hasattr(file_publisher, 'text'):
            return file_publisher.text

def get_epub_book_language(file_path):
    with zipfile.ZipFile(file_path) as z:
        t = etree.fromstring(z.read("META-INF/container.xml"))
        rootfile_path =  t.xpath("/u:container/u:rootfiles/u:rootfile", namespaces=namespaces)[0].get("full-path")
        t = etree.fromstring(z.read(rootfile_path))
        cover_id = t.xpath("//opf:metadata", namespaces=namespaces)[0]
        file_language = cover_id.find('{http://purl.org/dc/elements/1.1/}language')
        if hasattr(file_language, 'text'):
            return file_language.text

def get_epub_file_content(file_path): # return the entire book (combine htmls, pics, tables and other files), where you've left off
    spine_item_location :array = []
    with zipfile.ZipFile(file_path) as z:
        t = etree.fromstring(z.read("META-INF/container.xml"))
        rootfile_path =  t.xpath("/u:container/u:rootfiles/u:rootfile", namespaces=namespaces)[0].get("full-path")
        t = etree.fromstring(z.read(rootfile_path))
        for item in t.xpath("//opf:spine/opf:itemref", namespaces=namespaces):
            spine_itemref = item.get("idref")
            spine_item_location.append(t.xpath("//opf:manifest/opf:item[@id='" + spine_itemref + "']", namespaces=namespaces)[0].get("href"))

        # if rootfile_path:
        #     if os.path.dirname(rootfile_path) == "":
        #         cover_path = (spine_item_location[1])
        
        file_contents = []

        for spine_item_file in range(len(spine_item_location)):
            # file_contents.append(spine_item_location[spine_item_file])

            if spine_item_location[spine_item_file].endswith(".html"):
                location_content = html_file_data.get_html_text(z.read(spine_item_location[spine_item_file]).decode("utf-8"))
                file_contents.append({"location_content" : location_content, "file_type" : "html"})

            elif spine_item_location[spine_item_file].endswith(".xhtml"):
                pass

            elif spine_item_location[spine_item_file].endswith(".xml"):
                pass

        return file_contents

# lxml licence
# html licence

# orwell - there is no item named 001.html in archive
# "There is no item named 'LastWish_copy.html' in the archive"
