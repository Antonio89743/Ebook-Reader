import os
from pickle import NONE
import sys
from types import NoneType
import zipfile
from lxml import etree
from PIL import Image
import tkinter as tk
from PIL import ImageTk as itk

namespaces = {
   "calibre":"http://calibre.kovidgoyal.net/2009/metadata",
   "dc":"http://purl.org/dc/elements/1.1/",
   "dcterms":"http://purl.org/dc/terms/",
   "opf":"http://www.idpf.org/2007/opf",
   "u":"urn:oasis:names:tc:opendocument:xmlns:container",
   "xsi":"http://www.w3.org/2001/XMLSchema-instance",
}

def get_epub_cover_image(epub_path):
    ''' Return the cover image file from an epub archive. '''
    
    # We open the epub archive using zipfile.ZipFile():
    with zipfile.ZipFile(epub_path) as z:
    
        # We load "META-INF/container.xml" using lxml.etree.fromString():
        t = etree.fromstring(z.read("META-INF/container.xml"))
        # We use xpath() to find the attribute "full-path":
        '''
        <container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
          <rootfiles>
            <rootfile full-path="OEBPS/content.opf" ... />
          </rootfiles>
        </container>
        '''
        rootfile_path =  t.xpath("/u:container/u:rootfiles/u:rootfile",
                                             namespaces=namespaces)[0].get("full-path")
        # print("Path of root file found: " + rootfile_path)
        
        # We load the "root" file, indicated by the "full_path" attribute of "META-INF/container.xml", using lxml.etree.fromString():
        t = etree.fromstring(z.read(rootfile_path))
        # We use xpath() to find the attribute "content":
        '''
        <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
          ...
          <meta content="my-cover-image" name="cover"/>
          ...
        </metadata>
        '''
        cover_id = t.xpath("//opf:metadata/opf:meta[@name='cover']",
                                    namespaces=namespaces)[0].get("content")
        # print("ID of cover image found: " + cover_id)
        
        # We use xpath() to find the attribute "href":
        '''
        <manifest>
            ...
            <item id="my-cover-image" href="images/978.jpg" ... />
            ... 
        </manifest>
        '''
        cover_href = t.xpath("//opf:manifest/opf:item[@id='" + cover_id + "']",
                                         namespaces=namespaces)[0].get("href")

        if rootfile_path:
         if os.path.dirname(rootfile_path) == "":

            cover_path = (cover_href)

         else:

            cover_path = (os.path.dirname(rootfile_path) + "/" + cover_href)

        return z.open(cover_path)




def get_epub_book_title(epub_path):
    ''' Return the cover image file from an epub archive. '''
    
    # We open the epub archive using zipfile.ZipFile():
    with zipfile.ZipFile(epub_path) as z:
    
        # We load "META-INF/container.xml" using lxml.etree.fromString():
        t = etree.fromstring(z.read("META-INF/container.xml"))
        # We use xpath() to find the attribute "full-path":
        '''
        <container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
          <rootfiles>
            <rootfile full-path="OEBPS/content.opf" ... />
          </rootfiles>
        </container>
        '''
        rootfile_path =  t.xpath("/u:container/u:rootfiles/u:rootfile",
                                             namespaces=namespaces)[0].get("full-path")
        # print("Path of root file found: " + rootfile_path)
        
        # We load the "root" file, indicated by the "full_path" attribute of "META-INF/container.xml", using lxml.etree.fromString():
        # t = etree.fromstring(z.read(rootfile_path))
        # # print(t.findall("<metadata>"))
        # # We use xpath() to find the attribute "content":
        # '''
        # <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
        #   ...
        #   <meta content="my-cover-image" name="cover"/>
          
        #   ...
        # </metadata>
        # '''
        t = etree.fromstring(z.read(rootfile_path))
        # We use xpath() to find the attribute "content":
        '''
        <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
          ...
          <meta content="my-cover-image" name="cover"/>
          ...
        </metadata>
        '''
        cover_id = t.xpath("//opf:metadata",
                                    namespaces=namespaces)[0]
        # print("ZZZZZ", cover_id)
        file_title = cover_id.find('{http://purl.org/dc/elements/1.1/}title')
        # print("AAAAAAAAA", name.text)
        return file_title.text





def get_epub_book_author(epub_path):
    ''' Return the cover image file from an epub archive. '''
    
    # We open the epub archive using zipfile.ZipFile():
    with zipfile.ZipFile(epub_path) as z:
    
        # We load "META-INF/container.xml" using lxml.etree.fromString():
        t = etree.fromstring(z.read("META-INF/container.xml"))
        # We use xpath() to find the attribute "full-path":
        '''
        <container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
          <rootfiles>
            <rootfile full-path="OEBPS/content.opf" ... />
          </rootfiles>
        </container>
        '''
        rootfile_path =  t.xpath("/u:container/u:rootfiles/u:rootfile",
                                             namespaces=namespaces)[0].get("full-path")
        # print("Path of root file found: " + rootfile_path)
        
        # We load the "root" file, indicated by the "full_path" attribute of "META-INF/container.xml", using lxml.etree.fromString():
        # t = etree.fromstring(z.read(rootfile_path))
        # # print(t.findall("<metadata>"))
        # # We use xpath() to find the attribute "content":
        # '''
        # <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
        #   ...
        #   <meta content="my-cover-image" name="cover"/>
          
        #   ...
        # </metadata>
        # '''
        t = etree.fromstring(z.read(rootfile_path))
        # We use xpath() to find the attribute "content":
        '''
        <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
          ...
          <meta content="my-cover-image" name="cover"/>
          ...
        </metadata>
        '''
        cover_id = t.xpath("//opf:metadata",
                                    namespaces=namespaces)[0]
        # print("ZZZZZ", cover_id)
        file_title = cover_id.find('{http://purl.org/dc/elements/1.1/}creator')
        print(file_title, " ", epub_path)
        # print("gggggggg", file_title.text)
        # print("AAAAAAAAA", name.text)
        if cover_id == NONE:
          pass
        else:
          # if file_title.text == "None":
          #   pass
          if hasattr(file_title, 'text'):
            print("AAAAAAAAA", file_title.text)
            return file_title.text











# root = fromstring(xml_text)
# for actor in root.findall('{http://people.example.com}actor'):
#     name = actor.find('{http://people.example.com}name')
#     print(name.text)
#     for char in actor.findall('{http://characters.example.com}character'):
#         print(' |-->', char.text)
        
        # We load the "root" file, indicated by the "full_path" attribute of "META-INF/container.xml", using lxml.etree.fromString():
        # t = etree.fromstring(z.read(rootfile_path))
        # We use xpath() to find the attribute "content":
        '''
        <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
          ...
          <meta content="my-cover-image" name="cover"/>
          ...
        </metadata>
        '''
        # print(t)
        # print("CCC", t.findall('{http://purl.org/dc/elements/1.1/}dc'))
        # for actor in t.findall('{http://purl.org/dc/elements/1.1/}dc'):
        #   print(actor)



        # cover_id = t.xpath("//opf:metadata/opf:meta[@name='cover']",
        #                             namespaces=namespaces)[0].get("content")
# <base>
#    <element1>
#        <element2>asdada</element2>
#    </element>
# </base>
# root[0][0] will give u element 2

        # <dc:title>Lolita</dc:title> this is an element, not an attribute
        # <meta name="cover" content="cover"/>


        # cover_id = t.xpath("//opf:metadata/opf:meta[@name='cover']",
        #                             namespaces=namespaces)[0].get("content")




        # cover_href = t.xpath("//opf:manifest/opf:item[@id='" + cover_id + "']",
        #                                  namespaces=namespaces)[0].get("href")
        # print(rootfile_path)
        # print(z)
        # # print(etree.fromstring(rootfile_path))
        # import xml.etree.ElementTree as ET
        # print(etree.fromstring(z.read(rootfile_path)))
        # tree = etree.fromstring(z.read(rootfile_path))
        # root = tree.getroot()

        # cover_id = t.xpath("//opf:metadata/opf:dc:date",
        #                     namespaces=namespaces)[0]
        # print(cover_id)
        
        # for country in root.findall('dc:date'):
        #     rank = country.find('rank').text
        #     name = country.get('name')
        #     print(name, rank)
        



        # import xml.etree.ElementTree as ET
        # tree = ET.parse('country_data.xml')
        # root = tree.getroot()

        # cover_id = t.xpath("//opf:metadata/opf:dc:date",
        #                     namespaces=namespaces)[0]
        # print(cover_id)
        
        # for country in root.findall('dc:date'):
        #     rank = country.find('rank').text
        #     name = country.get('name')
        #     print(name, rank)


        

        # from xml.etree import ElementTree as ET
        # x =open(r"C:\Users\anton\OneDrive\Radna površina\Epub Reader\Epub-Reader\OEBPS\LastWish_opf.opf")
        # # x = z.open(os.path.abspath(r"C:\Users\anton\OneDrive\Radna površina\Epub Reader\Epub-Reader\OEBPS\LastWish_opf.opf"))


        
        # tree = ET.parse(x)
        # print(tree)




        # cover_id = t.xpath("//opf:metadata/opf:meta[@name='cover']",
        #                             namespaces=namespaces)[0].get("content")
        # print(cover_id)

        # from xml.etree import ElementTree as ET
        # print(os.path.abspath(rootfile_path))
        # tree = ET.parse(os.path.abspath(rootfile_path))
        # (os.path.dirname(rootfile_path) + "/" + cover_href)


        # title = find(".//{http://purl.org/dc/elements/1.1/}title")
      

        # dcNamespace = {"dc": "http://purl.org/dc/elements/1.1/"}
        # title = t.xpath("//opf:metadata/opf:meta[@name='cover']", namespaces=namespaces)
        # print(title)
        # x = 0
        # while x < len(title):
        #                                 # doc = etree.parse(filename)

        #                                 # memoryElem = doc.find('memory')
        #                                 # print memoryElem.text        # element text
        #                                 # print memoryElem.get('unit') # attribute
        #   # n = etree.parse(t.xpath("//opf:metadata/opf:meta", namespaces=namespaces))
        #   # c = n.find("dc")
        #   # print(c)
        #   y = title[x].get('title')
        #   print(y)
        #   x+=1
        



        # <dc:title>Lolita</dc:title>

        # cover_id = t.xpath("//opf:metadata/opf:meta[@name='cover']",
        #                   namespaces=namespaces)[0].get()
        # print(cover_id)
      # etree.parse()
        # 
        # print(t.xpath("//opf:metadata/opf:meta", namespaces=dcNamespace))
        # print(t)
        # OEBPS/LastWish_opf.opf


        # 
        # cover_id = t.xpath("//opf:metadata/opf:meta",
        #                             namespaces=dcNamespace)[0].get("title")

        # from xml.etree import ElementTree as ET
        # tree = ET.parse('content.opf')

        # title = tree.find(".//{http://purl.org/dc/elements/1.1/}title")

# echo $package->metadata->children('dc', true)->title."<br>";

# foreach($package->metadata->meta as $meta) {
#     echo "content:{$meta['content']}  name: {$meta['name']} <br>"; 
# }

# tree = ET.parse('content.opf')
# title = tree.find(".//{http://purl.org/dc/elements/1.1/}title")
# print(title.text)


        # print("XXXXXXXXXXXXXXXXXXXXXXX", title)

    # <dc:title>Lolita</dc:title>
    # <meta name="cover" content="cover"/>



        # print("ID of cover image found: " + cover_id)
        
        # We use xpath() to find the attribute "href":
        '''
        <manifest>
            ...
            <item id="my-cover-image" href="images/978.jpg" ... />
            ... 
        </manifest>
        '''


        
        # cover_href = t.xpath("//opf:manifest/opf:item[@id='" + cover_id + "']",
        #                                  namespaces=namespaces)[0].get("href")

        # if rootfile_path:
        #  if os.path.dirname(rootfile_path) == "":

        #     cover_path = (cover_href)

        #  else:

        #     cover_path = (os.path.dirname(rootfile_path) + "/" + cover_href)

        # return z.open(cover_path)


# get_epub_book_author(r"C:\Users\anton\OneDrive\Radna površina\Epub Reader\Epub-Reader\trash\The Last Wish by Andrzej Sapkowski .epub")