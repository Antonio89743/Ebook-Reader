from cProfile import label
from logging import root
from msilib.schema import File
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'minimum_width', '700')
Config.set('graphics', 'minimum_height', '400')
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.card import MDCard
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDIconButton
from kivy.core.image import Image as CoreImage
from kivy.uix.button import Button as KivyButton
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
import cbz_file_data
import text_file_data
import epub_file_data
from kivy.core.window import Window
import os, string
from os.path import sep, expanduser, isdir, dirname, exists
import sys
import json
import scan_folders
from io import StringIO 
import imghdr
import sys
from zipfile import ZipFile
import io
import zipfile
from itertools import cycle

Kivy = '''

#:import Factory kivy.factory.Factory

<LocalFolderPopUp@Popup>
    id: local_folder_popup
    auto_dismiss: False
    title: "Choose Folder"
    size_hint: (0.8, 0.8)
    pos_hint: {"center_x": 0.5}
    on_open: root.add_drives()

    BoxLayout:
        size: root.size
        pos: root.pos
        orientation: "horizontal"

        ScrollView:
            id: scroll_view
            always_overscroll: False
            do_scroll_x: False
            size_hint: (None, 1)
            pos_hint: {"left": 1}
            width: 70

            BoxLayout:
                id: folder_chooser_box_layout_vertical
                width: scroll_view.width 
                height: self.minimum_height 
                orientation: "vertical"

        BoxLayout:
            size: root.size
            pos: root.pos
            orientation: "vertical"

            FileChooserListView:
                id: folder_chooser
                dirselect: True   
                rootpath: "E:"

            BoxLayout:
                size_hint_y: None
                height: 30
                Button:
                    text: "Close"
                    on_release: root.dismiss()

                Button:
                    text: "Add Folder"
                    on_release: app.add_folder_to_scan_folder_selected(folder_chooser.selection)

<LocalFoldersExpansionPanelContent>
    id: expansion_panel
    height: self.minimum_height
    adaptive_height: True
    orientation: "vertical"
    pos_hint: {"center_x": 0.5}
    size_hint: (0.7, None)
    padding: [20, 20, 20, 20]
    spacing: 20

    Button:
        text: "Add Local Folder To Scan"
        size_hint: (0.7, None)
        pos_hint: {"center_x": 0.5, "top": 1}
        width: 100
        on_press: Factory.LocalFolderPopUp().open()

Screen:
    MDTopAppBar:
        id: toolbar
        size_hint: (None, None)
        pos_hint: {"right": 1, "top": 1}
        width: root.width - 70
        elevation: 10
        title: "Book Reader"

    ScreenManager:
        id: screen_manager

        Screen:
            id: main_menu_screen
            name: "Main Menu"
            on_enter: toolbar.title = "Main Menu"
            TabbedPanel:
                do_default_tab: False
                tab_pos: "top_left"
                size_hint: (None, None)
                tab_width: 150
                pos_hint: {"right": 1}
                width: root.width - 70
                height: root.height - 70
                
                TabbedPanelItem:
                    text: "Files"

                    BoxLayout:
                        orientation: "vertical"

                        BoxLayout:
                            orientation: "horizontal"

                            Label:
                                text: "Sort by: "
                                size_hint: (None, None)
                                width: 100
                                height: 30
                            
                            Spinner: 
                                id: main_menu_files_widget_sort_spinner
                                text: "Release Date"
                                values: ("Release Date", "File Name", "Author Name", "File Format")
                                size_hint: (None, None)
                                sync_height: True
                                width: 100
                                height: 30
                                on_text: app.add_main_menu_widgets()
                            
                            Button:
                                id: main_menu_files_widget_order
                                text: "Ascending"
                                size_hint: (None, None)
                                width: 100
                                height: 30
                                on_press: app.sort_order_button_pressed()

                            Button:
                                text: "Filter"
                                size_hint: (None, None)
                                width: 100
                                height: 30
                            
                            Slider:
                                id: main_menu_file_widget_size_slider
                                orientation: "horizontal"
                                size_hint: (None, None)
                                width: 300
                                height: 30
                                value: 0.5
                                step: 0.01
                                min: 0.1
                                max: 1
                                on_value: app.main_menu_file_widget_size(main_menu_file_widget_size_slider)

                        ScrollView:
                            id: main_menu_scroll_view
                            always_overscroll: False
                            do_scroll_x: False
                            pos_hint: {"right": 1}
                            size_hint: (None, None)
                            width: root.width - 70
                            height: root.height - 70 - 40 - 5 - 30

                            GridLayout:
                                id: main_menu_grid_layout
                                pos_hint: {"top": 1}
                                size_hint: (None, None)
                                width: main_menu_scroll_view.width 
                                height: self.minimum_height 
                                padding: [20, 20, 20, 20]
                                spacing: 20
                                cols: 5

                TabbedPanelItem:
                    text: "Authors"
                    Label:
                        text: "CCCC"    

                TabbedPanelItem:
                    text: "Collections"
                    Label:
                        text: "XXXXX"    
     
        Screen:
            name: "Read Currently Open File Screen"
            on_enter: toolbar.title = ""

            MDCard:
                id: file_reader_content_card
                orientation: "vertical"
                size_hint: (None, None)
                pos_hint: {"center_x": 0.5}
                width: 700
                height: root.height
                radius: [0, 0, 0, 0]

                ScrollView:
                    id: file_reader_content_scroll_view
                    always_overscroll: False
                    do_scroll_x: False
                    pos_hint: {"right": 1}
                    size_hint: (None, None)
                    width: file_reader_content_card.width
                    height: root.height
                    
                    BoxLayout:
                        id: file_reader_content_grid_layout
                        pos_hint: {"top": 1}
                        size_hint: (None, None)
                        width: file_reader_content_scroll_view.width 
                        height: self.minimum_height 
                        orientation: 'vertical'

        Screen:
            name: "File Details Screen"
            on_enter: toolbar.title = "File Detail Screen"
            MDLabel:
                text: "File Details Screen"
                halign: "center"

        Screen:
            name: "Settings Screen"
            on_enter: toolbar.title = "Settings"
            TabbedPanel:
                do_default_tab: False
                tab_pos: "top_mid"
                size_hint: (None, None)
                tab_width: 200
                pos_hint: {"right": 1}
                width: root.width - 70
                height: root.height - 70

                TabbedPanelItem:
                    text: "Themes & Preferences"
                    Label:
                        text: "CCCC"    
                
                TabbedPanelItem:
                    text: "Scanning Folders"

                    ScrollView:
                        id: scroll_view
                        always_overscroll: False
                        do_scroll_x: False
                        pos_hint: {"right": 1}
                        size_hint: (None, None)
                        width: root.width - 70
                        height: root.height - 70 - 40

                        BoxLayout:
                            id: settings_scanning_local_folders_box_layout
                            pos_hint: {"top": 1}
                            size_hint: (None, None)
                            width: scroll_view.width 
                            height: self.minimum_height 
                            orientation: 'vertical'

                            Label:
                                text: "Local Folders To Scan"
                                font_size: 20
                                halign: "left"
                                size_hint: (None, None)
                                pos_hint: {"left": 1, "top": 1}
                                width: 250
                                height: 50

                TabbedPanelItem:
                    text: "About"
                    Label:
                        text: "cxzczxc"

    BoxLayout:
        padding: [10, 10, 10, 10]
        spacing: 20
        id: nav_bar
        orientation: 'vertical'
        pos_hint: {"left": 0, "y": 0}

        MDIconButton:
            pos_hint: {"y": 1}
            width: 70
            height: 70
            icon: "icons and images\go back.png"
            on_press: app.return_to_previous_tab_or_screen()
        
        MDIconButton:
            pos_hint: {"center_y": 1}
            width: 70
            height: 70
            color : [1.0, 1.0, 1.0, 1.0]
            icon: "icons and images\search.png"

        MDIconButton:
            pos_hint: {"center_y": 1}
            width: 70
            height: 70
            color : [1.0, 1.0, 1.0, 1.0]
            icon: "icons and images\Home-icon.svg.png" 
            on_press: app.change_screen("Main Menu", False)

        MDIconButton:
            pos_hint: {"y": 1}
            width: 70
            height: 70
            color : [1.0, 1.0, 1.0, 1.0]
            on_press: app.change_screen("Read Currently Open File Screen", False)

        BoxLayout:
            id: nav_bar_settings
            orientation: 'vertical'
            pos_hint: {"left": 0, "y": 0}

            MDIconButton:
                width: 70
                height: 70
                pos_hint: {"y": 0}
                md_bg_color : [1.0, 1.0, 1.0, 1.0]
                icon: "icons and images\icons8-settings-500.png" 
                on_press: app.change_screen("Settings Screen", False)
                # add onperss that will add in element to array for previous frames

'''

# see if you can get the location of the mouse and hide the navbar in the currently reading frame and only show it if mouse is in position
# navbar searchbar buton on press expand it to a full searchbar

class LocalFolderPopUp(Popup):
    class DriveButton():
        def __init__(self, app, drive):
            app.ids.folder_chooser_box_layout_vertical.add_widget(
            KivyButton(
                text = drive,
                pos_hint = {"top": 1},
                size_hint = (1, None),
                height = 70,
                on_press = lambda x: app.drive_chosen(app, drive)
                )
            )

    def drive_chosen(self, app, drive):
        app.ids.folder_chooser.rootpath = drive

    def add_drives(self):
        available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
        for drive in available_drives:
            self.DriveButton(self, drive)

class AddLocalFolderToScanDialog():
    '''AddLocalFolderToScanDialog'''

class LocalFoldersExpansionPanelContent(BoxLayout):
    '''LocalFoldersExpansionPanelContent'''

class FileReaderApp(MDApp):
    class File():
        def __init__(self, app, file):
            if file["file_format"] == "txt":
                file_title = file["file_name"]
                card = MDCard(
                        orientation = "vertical",
                        size_hint = (None, None),
                        height = app.main_menu_files_widgets_height,
                        width = app.main_menu_files_widgets_width,
                        radius = [0, 0, 0, 0]
                    )
                app.root.ids.main_menu_grid_layout.add_widget(card)
                if file_title != None:
                    file_title_button = KivyButton(
                            on_press = lambda x: app.change_screen("Read Currently Open File Screen", False),
                            text = file_title,
                            color = (0, 0, 0, 1),
                            size_hint = (1, None),
                            height = 50,
                            # width = 300,
                        )
                else:
                    file_title_button = KivyButton(
                        on_press = lambda x: app.change_screen("Read Currently Open File Screen", False),
                        text = "File Title Not Found",
                        color = (0, 0, 0, 1),
                        size_hint = (1, None),
                        height = 50,
                        # width = 300,
                    )
                file_title_button.bind(on_press = lambda x: app.load_file_read_screen(file))  
                card.add_widget(file_title_button)   
            elif file["file_format"] == "epub":
                file_title = file["file_name"]
                file_author = file["file_author"]
                file_cover = zipfile.ZipFile(file["absolute_file_path"]).read(file["file_cover"])
                card = MDCard(
                        orientation = "vertical",
                        size_hint = (None, None),
                        height = app.main_menu_files_widgets_height,
                        width = app.main_menu_files_widgets_width,
                        radius = [0, 0, 0, 0]
                    )
                app.root.ids.main_menu_grid_layout.add_widget(card)

                cover_image = CoreImage(io.BytesIO(file_cover), ext = "jpg")
                if file_cover != None:
                    file_cover_button = Image(
                        texture = CoreImage(cover_image).texture,
                        # on_touch_down = lambda x: app.change_screen("Read Currently Open File Screen", False)
                    )
                else:
                    file_cover_button = KivyButton(
                        on_press = lambda x: app.change_screen("Read Currently Open File Screen", False),
                        text = "File Cover Image Not Found",
                        color = (0, 0, 0, 1),
                        size_hint = (1, None),
                        height = 50,
                        # width = 300,
                    )
                file_cover_button.bind(on_press = lambda x: app.load_file_read_screen(file))  
                card.add_widget(file_cover_button)                        
                if file_title != None:
                    file_title_button = KivyButton(
                        on_press = lambda x: app.change_screen("Read Currently Open File Screen", False),
                        text = file_title,
                        color = (0, 0, 0, 1),
                        size_hint = (1, None),
                        height = 50,
                        # width = 300,
                    )
                else:
                    file_title_button = KivyButton(
                    on_press = lambda x: app.change_screen("Read Currently Open File Screen", False),
                    text = "File Title Not Found",
                    color = (0, 0, 0, 1),
                    size_hint = (1, None),
                    height = 50,
                    # width = 300,
                    )
                file_title_button.bind(on_press = lambda x: app.load_file_read_screen(file))  
                card.add_widget(file_title_button)
                if file_author != None:
                    file_author_button = KivyButton(
                        text = file_author,
                        color = (0, 0, 0, 1),
                        size_hint = (1, None),
                        height = 50,
                        # width = 300,
                        )
                else:
                    file_author_button = KivyButton(
                    text = "File Author Not Found",
                    color = (0, 0, 0, 1),
                    size_hint = (1, None),
                    height = 50,
                    # width = 300,
                    ) 
                card.add_widget(file_author_button)
            elif file["file_format"] == "cbz":
                file_title = cbz_file_data.get_cbz_file_title(file["absolute_file_path"])
                file_author = file["file_author"]
                file_cover = zipfile.ZipFile(file["absolute_file_path"]).read(file["file_cover"])
                card = MDCard(
                        orientation = "vertical",
                        size_hint = (None, None),
                        height = app.main_menu_files_widgets_height,
                        width = app.main_menu_files_widgets_width,
                        radius = [0, 0, 0, 0]
                    )
                app.root.ids.main_menu_grid_layout.add_widget(card)
                cover_image = CoreImage(io.BytesIO(file_cover), ext = "jpg")
                if file_cover != None:
                    file_cover_button = Image(
                        texture = CoreImage(cover_image).texture,
                    )
                else:
                    file_cover_button = KivyButton(
                    on_press = lambda x: app.change_screen("Read Currently Open File Screen", False),
                    text = "File Cover Image Not Found",
                    color = (0, 0, 0, 1),
                    size_hint = (1, None),
                    height = 50,
                    # width = 300,
                    )
                file_cover_button.bind(on_press=lambda x: app.load_file_read_screen(file))  
                card.add_widget(file_cover_button)                        
                if file_title != None:
                    file_title_button = KivyButton(
                        on_press = lambda x: app.change_screen("Read Currently Open File Screen", False),
                        text = file_title,
                        color = (0, 0, 0, 1),
                        size_hint = (1, None),
                        height = 50,
                        # width = 300,
                        )
                else:
                    file_title_button = KivyButton(
                    on_press = lambda x: app.change_screen("Read Currently Open File Screen", False),
                    text = "File Title Not Found",
                    color = (0, 0, 0, 1),
                    size_hint = (1, None),
                    height = 50,
                    # width = 300,
                    )
                file_title_button.bind(on_press=lambda x: app.load_file_read_screen(file))  
                card.add_widget(file_title_button)
            elif file["file_format"] == "mp3_album":
                print(file)

    list_of_files = None
    currently_open_file = None 
    screen_currently_in_use :int = 0
    previous_screens_and_tabs_list = ["Main Menu"]
    main_menu_files_widgets_height = None
    main_menu_files_widgets_width = None

    def image_press(self, *args):
        print("SSS")

    def main_menu_file_widget_size(self, id):
        if id == self.root.ids.main_menu_file_widget_size_slider:
            self.main_menu_files_widgets_height = 1000 * id.value
            self.main_menu_files_widgets_width = 600 * id.value
            for child in self.root.ids.main_menu_grid_layout.children:
                child.height = self.main_menu_files_widgets_height
                child.width = self.main_menu_files_widgets_width
            self.responsive_grid_layout()

    audio_file_formats = ["mp3", "wav", "ogg"] 

    def load_file_read_screen(self, file):
        if file["file_format"] != self.audio_file_formats:
            if self.currently_open_file != file:
                self.file_read_screen_mode(file, "pages and infinite scroll") #second arg is temporary
        else:
            # here load screen for audio files
            self.root.ids.file_reader_content_grid_layout.clear_widgets()

    def file_read_screen_mode(self, file, *args):
        self.root.ids.file_reader_content_grid_layout.clear_widgets()
        file_content = self.get_file_contents(file)

        if args == ():
            # there isn't a specified reading mode, so check defaults or previously used modes for this type or just previously used modes for any type
            # file specific?, file type specific mode?
            pass

        if args:
            if args[0] == "pageless infinite scroll":
                if file["file_format"] == "txt":
                    label = Label(
                            text = file_content,
                            color = [0, 0, 0, 1],
                            size_hint = (None, None),
                            halign = "left",
                            valign = "top",
                            size = self.root.ids.file_reader_content_grid_layout.size
                        )
                    label.bind(texture_size = label.setter("size"))
                    self.root.ids.file_reader_content_grid_layout.add_widget(label)
                elif file["file_format"] == "epub": 
                    for file in file_content:
                        if file["file_type"] == "html":
                            label = Label(
                                text = file["location_content"],
                                color = [0, 0, 0, 1],
                                size_hint = (None, None),
                                halign = "left",
                                valign = "top",
                                size = self.root.ids.file_reader_content_grid_layout.size
                            )
                            label.bind(texture_size = label.setter("size"))
                            self.root.ids.file_reader_content_grid_layout.add_widget(label)
                            # should there only be one widget? will that make it better for pages?
                elif file["file_format"] == "cbz": 
                    # redirect to another value
                    pass
            elif args[0] == "pages and infinite scroll":
                if file["file_format"] == "cbz": 
                    for file_item in file_content:
                        if file_item["file_format"] in self.kivy_supported_image_files:

                            # this part of the code isn't working; sizes, size hints and such are issues
                            image = CoreImage(io.BytesIO(file_item["file"]), ext = "jpg")
                            file_image = Image(
                                texture = CoreImage(image).texture,
                                size_hint = (None, None),
                                # height = 400,
                                # width = 400,
                                pos_hint = {"center_x": 0.5}
                            )
                            self.root.ids.file_reader_content_grid_layout.add_widget(file_image)
                    self.root.ids.file_reader_content_grid_layout.size_hint = (None, 1)
                    self.root.ids.file_reader_content_grid_layout.height = self.root.ids.file_reader_content_grid_layout.minimum_height
                    self.root.ids.file_reader_content_grid_layout.size_hint_y = None

            elif args[0] == "book simulator":
                pass

        self.currently_open_file = file

    kivy_supported_image_files = ["jpeg", "jpg", "png", "gif"]

    def get_file_contents(self, file):
        if file["file_format"] == "txt":
            file_content = text_file_data.get_txt_file_content(file["absolute_file_path"])
        elif file["file_format"] == "epub": 
            file_content = epub_file_data.get_epub_file_content(file["absolute_file_path"])
        elif file["file_format"] == "mobi": 
            pass
        elif file["file_format"] == "pdf": 
            pass
        elif file["file_format"] == "doc": 
            pass
        elif file["file_format"] == "docx": 
            pass
        elif file["file_format"] == "cbz": 
            file_content = cbz_file_data.get_cbz_file_content(file["absolute_file_path"])
        elif file["file_format"] == "mp3_album": 
            pass
        return file_content

    def go_forward_to_next_tab_or_screen(self):
        self.change_screen(self.previous_screens_and_tabs_list[self.screen_currently_in_use + 1], True)

    def return_to_previous_tab_or_screen(self):
        self.change_screen(self.previous_screens_and_tabs_list[self.screen_currently_in_use - 1], True)
        self.screen_currently_in_use -= 1

    def change_screen(self, screen, using_return_bool):
        self.root.ids.screen_manager.current = screen
        self.previous_screens_and_tabs_list.append(screen)
        if using_return_bool == False:
            self.screen_currently_in_use += 1

    def add_main_menu_widgets(self):
        self.root.ids.main_menu_grid_layout.clear_widgets()
        self.sort_file_list()
        for file in self.list_of_files:
            self.File(self, file)
    
    def sort_file_list(self):
        def sort_release_year(list):
            if list["release_date"] == None:
                return ""
            else:
                return list["release_date"]
        def sort_file_format(list):
            if list["file_format"] == None:
                return ""
            else:
                return list["file_format"]
        def sort_file_name(list):
            if list["file_name"] == None:
                return ""
            else:
                return list["file_name"]
        def sort_author_name(list):
            if list["file_author"] == None:
                return ""
            else:
                return list["file_author"]

        if self.root.ids.main_menu_files_widget_order.text == "Ascending":
            reverse_bool = False
        else:
            reverse_bool = True

        if self.root.ids.main_menu_files_widget_sort_spinner.text == "File Name":
            self.list_of_files.sort(key = sort_file_name, reverse = reverse_bool)
        elif self.root.ids.main_menu_files_widget_sort_spinner.text == "Author Name":
            self.list_of_files.sort(key = sort_author_name, reverse = reverse_bool)
        elif self.root.ids.main_menu_files_widget_sort_spinner.text == "Release Date":
            self.list_of_files.sort(key = sort_release_year, reverse = reverse_bool)
        elif self.root.ids.main_menu_files_widget_sort_spinner.text == "File Format":
            self.list_of_files.sort(key = sort_file_format, reverse = reverse_bool)
    
    def sort_order_button_pressed(self):
        if self.root.ids.main_menu_files_widget_order.text == "Ascending":
            self.root.ids.main_menu_files_widget_order.text = "Descending"
        else:
            self.root.ids.main_menu_files_widget_order.text = "Ascending"
        self.add_main_menu_widgets()

    def add_folder_to_scan_folder_selected(self, folder_selected):
        self.list_of_files = scan_folders.scan_folders(str(folder_selected), True)
        self.add_main_menu_widgets()
    
    def full_scan(self):
        if exists("Book Worm\Book Worm\local_folders_to_scan.json"):
            file = open("Book Worm\Book Worm\local_folders_to_scan.json", "r")
            json_file_data = file.read()
            file.close()
            if json_file_data != "":
                self.list_of_files = scan_folders.scan_folders(json_file_data.split(","), False)
                self.add_main_menu_widgets()

    def local_folders_and_files_scan(self): 
        if exists("Book Worm\Book Worm\local_folders_to_scan_dictonary.json"):
            file = open("Book Worm\Book Worm\local_folders_to_scan_dictonary.json", "r")
            json_file_data = file.read()
            file.close()
            if json_file_data != "":
                self.list_of_files = scan_folders.scan_folders(json_file_data, False)
                self.add_main_menu_widgets()
        elif exists("Book Worm\Book Worm\local_folders_to_scan_dictonary.json") == False:
            open("Book Worm\Book Worm\local_folders_to_scan_dictonary.json", "a").close()
            self.full_scan()            
            if exists("Book Worm\Book Worm\local_folders_to_scan.json") == False: 
                open("Book Worm\Book Worm\local_folders_to_scan.json", "a").close()

    def create_local_folders_to_scan_expansion_panel(self):
        self.root.ids.settings_scanning_local_folders_box_layout.add_widget(
            MDExpansionPanel(
                content = LocalFoldersExpansionPanelContent(),
                panel_cls = MDExpansionPanelOneLine(
                    text = "Local Folders To Scan",
                    size_hint = (1, None),
                    pos_hint = {"center_x": 0.5}
                    # position this in the middle of the screen and set size hit x to 0.8
                    )
                )   
            ) 
    
    def responsive_grid_layout(self, *args):
        self.root.ids.main_menu_grid_layout.cols = int(self.root.ids.main_menu_grid_layout.width / (self.main_menu_files_widgets_width + 20))

    def set_main_menu_widget_sizes(self, *args):
        if type(args[0]) == dict:
            self.root.ids.main_menu_file_widget_size_slider.value = args[0]["main_menu_file_widget_size_slider_value"]
            self.main_menu_files_widgets_height = args[0]["main_menu_file_widget_height"]
            self.main_menu_files_widgets_width = args[0]["main_menu_file_widget_width"]
        else:
            self.main_menu_files_widgets_height = 1000
            self.main_menu_files_widgets_width = 600

    def save_last_used_settings(self):
        save_app_data_dictionary = {
            "main_menu_file_sort" : self.root.ids.main_menu_files_widget_sort_spinner.text,
            "main_menu_file_sort_order" : self.root.ids.main_menu_files_widget_order.text,
            "main_menu_file_widget_height" : self.main_menu_files_widgets_height,
            "main_menu_file_widget_width" : self.main_menu_files_widgets_width,
            "main_menu_file_widget_size_slider_value" : self.root.ids.main_menu_file_widget_size_slider.value,
        }
        file = open("Book Worm\Book Worm\saved_app_data_dictionary.json", "w")
        file.write(json.dumps(save_app_data_dictionary))
        file.close()

    def set_main_menu_widget_sort(self, *args):
        if type(args) == dict:
            self.root.ids.main_menu_files_widget_sort_spinner.text = args["main_menu_file_sort"]
    
    def set_main_menu_widget_sort_order(self, *args):
        if type(args) == dict:
            self.root.ids.main_menu_files_widget_order.text = args["main_menu_file_sort_order"]

    def load_last_used_settings(self):
        saved_app_data_dictionary = None
        if exists("Book Worm\Book Worm\saved_app_data_dictionary.json"):
            file = open("Book Worm\Book Worm\saved_app_data_dictionary.json", "r")
            saved_app_data_dictionary = json.load(file)
            file.close()
        else: 
            saved_app_data_dictionary = {
                "main_menu_file_sort": "Release Date", 
                "main_menu_file_sort_order": "Ascending", 
                "main_menu_file_widget_height": 840.0, 
                "main_menu_file_widget_width": 504.0, 
                "main_menu_file_widget_size_slider_value": 0.84
                }
            pass
        self.set_main_menu_widget_sizes(saved_app_data_dictionary)
        self.set_main_menu_widget_sort(saved_app_data_dictionary)
        self.set_main_menu_widget_sort_order(saved_app_data_dictionary)

    def build(self):
        self.title = "Book Reader"
        Window.bind(on_resize = self.responsive_grid_layout)
        Window.bind(on_restore = self.responsive_grid_layout)
        Window.bind(on_maximize = self.responsive_grid_layout)
        Window.bind(on_request_close = self.on_request_close)
        Window.bind(on_key_down = self.on_key_down)
        return Builder.load_string(Kivy)
    
    def on_start(self):
        self.load_last_used_settings()
        self.responsive_grid_layout()
        self.create_local_folders_to_scan_expansion_panel()
        self.local_folders_and_files_scan()
        # print(Config.get('graphics', 'window_state'), Config.get("graphics", "fullscreen"))
        # Config.set('graphics', 'window_state', 'hidden')

    def on_request_close(self, *args):
        self.save_last_used_settings()

    def on_key_down(self, *args):
        print(args, print(type(args)))
    #     if args[3] == "Ĥ":
    #         if Config.get("graphics", "fullscreen") == "0":
    #             Config.set("graphics", "fullscreen", "1")
    #             Config.set("graphics", "window_state", "maximized")
    #         elif Config.get("graphics", "fullscreen") == "1":
    #             Config.set("graphics", "fullscreen", "0")
    #             Config.set("graphics", "window_state", "visible")

FileReaderApp().run()