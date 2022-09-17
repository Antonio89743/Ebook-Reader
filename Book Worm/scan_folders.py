from array import array
import glob, os

array_or_epub_files : array = []
dictionary_of_valid_files = {
    "array_of_epub_files": array_or_epub_files,
}

def scan_folders(folders_to_scan):
    if type(folders_to_scan) is list:
        for folder in folders_to_scan:
            epub_files = glob.glob(folder + "/**/*.epub", recursive = True)
            for epub_file in epub_files:
                array_or_epub_files.append(os.path.abspath(epub_file))
                # book = epub.read_epub(epub_file)
                
                # cover_image = book.get_item_with_id('cover-image')
                # print("Gdsdffsa", cover_image)
                # print(type(cover_image)) #ebooklib.epub.EpubImage

                if epub_file == glob.glob("*.png", recursive = True):
                    pass
                # imag = Image.open(cover_image)

                
                
                # cover_image = book.get_item_with_id('cover-image')
                # if cover_image:
                #     # just take this as a cover image
                #     print("gsdgsd", cover_image)
                #     print("123tyu", cover_image.get_content())
                #     x = cover_image.get_content() # return raw image?
                    # image_content = open(x, "rb").read()

                    # image_file = Image.open('test').read()
                    # The object was bytes-like, so in
                    # order to display it in the google colab I needed to use IPython.display
                    # rather than PIL (saving the images to file by writing as binary and then opening with PIL also worked).




                    # image_file = Image.open(cover_image).read()
                    # image_file = Image.open(cover_image, 'rb').read()


                    # image_file = Image.open(image)
                    # image_file.resize(300,300)
                    # photo_image = ImageTk.PhotoImage(image_file)
                    # button = Button(frame_main_menu)


                #     pass
                # elif cover_image == None:
                #     images = book.get_items_of_type(ebooklib.ITEM_IMAGE)




#  should this part be done with css/html?

                    # pass




# from PIL import Image as pil_image
# fname = 'my_image.jpg'
# with open(fname, 'rb') as f:
#     img = pil_image.open(io.BytesIO(f.read()))

                # I did try it with blob.upload_from_file(buf) using buf = TemporaryFile() as well as with buf = NamedTemporaryFile().


                # for image in images:
                #     if image.get_name() == "cover.jpeg":
                #         # print(image.get_content())


                #         image_file = Image.open(image.get_content())


                #         image_file = Image.open(image)
                #         image_file.resize(300,300)
                #         photo_image = ImageTk.PhotoImage(image_file)
                #         button = Button(frame_main_menu)
                    # print(image.get_name())



                # if filetype.is_image(epub_file):
                #     print(f"{epub_file} is a valid image...", epub_file)


                # file_cover = ImageTk.PhotoImage(Image.open(book.get_item_with_id('cover-image')))
                # label = Label(image=file_cover, backgroundcolor = 'green')
                # label.pack(side = RIGHT, anchor="n")

    # settings_button = Button(frame_main_menu, text='Settings', command=lambda:active_frame(settings(), main_menu()))
    # settings_button.pack(side = RIGHT, anchor="s")

                # print(epub_file)

    elif type(folders_to_scan) is str:
        print(folders_to_scan)
        epub_files = glob.glob(folders_to_scan + "/**/*.epub", recursive = True)
        for epub_file in epub_files:
             array_or_epub_files.append(os.path.abspath(epub_file))
    

    return dictionary_of_valid_files