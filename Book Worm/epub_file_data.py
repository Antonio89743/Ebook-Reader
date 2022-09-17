import os
import zipfile
from lxml import etree

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
            cover_path = (cover_href)
         else:
            cover_path = (os.path.dirname(rootfile_path) + "/" + cover_href)
        return z.open(cover_path)

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
        rootfile_path =  t.xpath("/u:container/u:rootfiles/u:rootfile",
                                             namespaces=namespaces)[0].get("full-path")
        t = etree.fromstring(z.read(rootfile_path))
        cover_id = t.xpath("//opf:metadata",
                                    namespaces=namespaces)[0]
        file_title = cover_id.find('{http://purl.org/dc/elements/1.1/}creator')
        if hasattr(file_title, 'text'):
          return file_title.text

# get_epub_book_author(r"C:\Users\anton\OneDrive\Radna površina\Epub Reader\Epub-Reader\trash\The Last Wish by Andrzej Sapkowski .epub")

# lxml licence