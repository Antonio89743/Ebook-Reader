import os
import sys
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
        # In order to get the full path for the cover image, we have to join rootfile_path and cover_href:

        if rootfile_path:
         if os.path.dirname(rootfile_path) == "":
            print("HAI")
            cover_path = (cover_href)
         else:
            print("NAI")
            cover_path = (os.path.dirname(rootfile_path) + "/" + cover_href)

            
        #  print("dfghjkl", rootfile_path)
        #  print("sdfghjkl", os.path.dirname(rootfile_path))
        
        # print("Path of cover image found: " + cover_path)
        print("L", epub_path)
        print("H", rootfile_path)
        # z.open(rootfile_path)
        # We return the image
      #   return z.open(r"OEBPS/images/LastWish-cover.jpg")
        print(cover_path, " ", os.path.abspath(cover_path))
        background = z.open(cover_path)
        # photo = itk.PhotoImage(file = background)
        # canvas = tk.Button(root,width=999,height=999, image=photo)


        return z.open(cover_path)





# image = Image.open(get_epub_cover_image(r"D:\Books\占星術殺人事件 改訂完全版 (講談社文庫)_島田荘司.epub")).show()
# image = Image.open(get_epub_cover_image(r"D:\Books\占星術殺人事件 改訂完全版 (講談社文庫)_島田荘司.epub"))


# image = get_epub_cover_image(r"D:\Books\占星術殺人事件 改訂完全版 (講談社文庫)_島田荘司.epub")
# root = tk.Tk()
# root.geometry('1000x1000')

# background = image
# print(image, " ", background)
# photo = itk.PhotoImage(file = background)
# print(photo)
# canvas = tk.Button(root,width=999,height=999, image=photo)
# canvas.pack()
# root.mainloop()


# <zipfile.ZipExtFile name='cover.jpeg' mode='r' compress_type=deflate>   <zipfile.ZipExtFile name='cover.jpeg' mode='r' compress_type=deflate>
# pyimage1


# label = tk.Label(window, image=image).pack()


# from Tkinter import *



# # pilImage = Image.open("ball.gif")
# pilImage = image
# image = tk.PhotoImage(Image(pilImage))
# imagesprite = canvas.create_image(400,400,image=image)
# 

# image = Image.ImageTk.PhotoImage(Image("ball.gif"))




# background = image
# photo = tk.PhotoImage(Image.open(background))
# This should be written correctly:



# Second, Tkinter does not support .png files. The correct class is ImageTk from module PIL.




# image = Image.open(get_epub_cover_image(r"C:\Users\anton\OneDrive\Radna površina\Epub Reader\Epub-Reader\trash\Lolita - Vladimir Vladimirovich Nabokov.epub"))
# image.show()

# HAI
# L C:\Users\anton\OneDrive\Radna površina\Epub Reader\Epub-Reader\trash\Lolita - Vladimir Vladimirovich Nabokov.epub
# H content.opf
# cover.jpeg   C:\Users\anton\OneDrive\Radna površina\Epub Reader\Epub-Reader\cover.jpeg
