from array import array
import os
import zipfile
from lxml import etree
import html_file_data

namespaces = {
   "calibre":"http://calibre.kovidgoyal.net/2009/metadata",
   "dc":"http://purl.org/dc/elements/1.1/",
   "dcterms":"http://purl.org/dc/terms/",
   "opf":"http://www.idpf.org/2007/opf",
   "u":"urn:oasis:names:tc:opendocument:xmlns:container",
   "xsi":"http://www.w3.org/2001/XMLSchema-instance",
}

def get_epub_cover_image(epub_path):
    with zipfile.ZipFile(epub_path) as z:
        t = etree.fromstring(z.read("META-INF/container.xml"))
        rootfile_path =  t.xpath("/u:container/u:rootfiles/u:rootfile", namespaces=namespaces)[0].get("full-path")
        t = etree.fromstring(z.read(rootfile_path))
        cover_id = t.xpath("//opf:metadata/opf:meta[@name='cover']", namespaces=namespaces)[0].get("content")
        cover_href = t.xpath("//opf:manifest/opf:item[@id='" + cover_id + "']", namespaces=namespaces)[0].get("href")
        if rootfile_path:
         if os.path.dirname(rootfile_path) == "":
            cover_path = cover_href
         else:
            cover_path = (os.path.dirname(rootfile_path) + "/" + cover_href)
        return cover_path#z.open(cover_path)

def get_epub_book_title(epub_path):
    with zipfile.ZipFile(epub_path) as z:
        t = etree.fromstring(z.read("META-INF/container.xml"))
        rootfile_path =  t.xpath("/u:container/u:rootfiles/u:rootfile", namespaces=namespaces)[0].get("full-path")
        t = etree.fromstring(z.read(rootfile_path))
        cover_id = t.xpath("//opf:metadata", namespaces=namespaces)[0]
        file_title = cover_id.find('{http://purl.org/dc/elements/1.1/}title')
        if hasattr(file_title, 'text'):
            return file_title.text

def get_epub_book_author(epub_path):
    with zipfile.ZipFile(epub_path) as z:
        t = etree.fromstring(z.read("META-INF/container.xml"))
        rootfile_path =  t.xpath("/u:container/u:rootfiles/u:rootfile", namespaces=namespaces)[0].get("full-path")
        t = etree.fromstring(z.read(rootfile_path))
        cover_id = t.xpath("//opf:metadata", namespaces=namespaces)[0]
        file_title = cover_id.find('{http://purl.org/dc/elements/1.1/}creator')
        if hasattr(file_title, 'text'):
            return file_title.text

def get_epub_book_publisher(epub_path):
    with zipfile.ZipFile(epub_path) as z:
        t = etree.fromstring(z.read("META-INF/container.xml"))
        rootfile_path =  t.xpath("/u:container/u:rootfiles/u:rootfile", namespaces=namespaces)[0].get("full-path")
        t = etree.fromstring(z.read(rootfile_path))
        cover_id = t.xpath("//opf:metadata", namespaces=namespaces)[0]
        file_publisher = cover_id.find('{http://purl.org/dc/elements/1.1/}publisher')
        if hasattr(file_publisher, 'text'):
            return file_publisher.text

def get_epub_book_language(epub_path):
    with zipfile.ZipFile(epub_path) as z:
        t = etree.fromstring(z.read("META-INF/container.xml"))
        rootfile_path =  t.xpath("/u:container/u:rootfiles/u:rootfile", namespaces=namespaces)[0].get("full-path")
        t = etree.fromstring(z.read(rootfile_path))
        cover_id = t.xpath("//opf:metadata", namespaces=namespaces)[0]
        file_language = cover_id.find('{http://purl.org/dc/elements/1.1/}language')
        if hasattr(file_language, 'text'):
            return file_language.text

def get_epub_book_text(epub_path): # return the entire book (combine htmls, pics, tables and other files), where you're left off
    spine_item_location :array = []
    with zipfile.ZipFile(epub_path) as z:
        t = etree.fromstring(z.read("META-INF/container.xml"))
        rootfile_path =  t.xpath("/u:container/u:rootfiles/u:rootfile", namespaces=namespaces)[0].get("full-path")
        t = etree.fromstring(z.read(rootfile_path))
        for item in t.xpath("//opf:spine/opf:itemref", namespaces=namespaces):
            spine_itemref = item.get("idref")
            spine_item_location.append(t.xpath("//opf:manifest/opf:item[@id='" + spine_itemref + "']", namespaces=namespaces)[0].get("href"))

        # if rootfile_path:
        #     if os.path.dirname(rootfile_path) == "":
        #         cover_path = (spine_item_location[1])
        
        x = []

        for spine_item_file in range(len(spine_item_location)):



            if spine_item_location[spine_item_file].endswith(".html"):

                print(spine_item_location[spine_item_file])
                x.append(html_file_data.get_html_text(z.read(spine_item_location[spine_item_file]).decode("utf-8")))

            elif spine_item_location[spine_item_file].endswith(".xhtml"):
                pass

            elif spine_item_location[spine_item_file].endswith(".xml"):
                pass

        return x

get_epub_book_text(r"C:\Users\anton\OneDrive\Radna površina\Epub Reader\Epub-Reader\trash\Lolita - Vladimir Vladimirovich Nabokov.epub")

# lxml licence
# html licence