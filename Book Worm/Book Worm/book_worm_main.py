from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'minimum_width', '700')
Config.set('graphics', 'minimum_height', '400')
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivymd.uix.card import MDCard
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDIconButton
from kivy.uix.button import Button as KivyButton
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
import epub_file_data
# from kivy.core.window import Window
# Window.fullscreen = True
# Window.maximize()
import os, string
from os.path import sep, expanduser, isdir, dirname, exists
import sys
import json
import scan_folders
from io import StringIO 
import imghdr
import sys
from zipfile import ZipFile
from PIL import Image
import io
import zipfile
from kivy.core.image import Image as CoreImage
from itertools import cycle

Kivy = '''

#:import Factory kivy.factory.Factory

<LocalFolderPopUp@Popup>
    id: local_folder_popup
    auto_dismiss: False
    title: "Choose Folder"
    size_hint: (0.8, 0.8)
    pos_hint: {"center_x": 0.5}
    on_open: app.add_buttons_for_drives()

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

                    ScrollView:
                        id: scroll_view
                        always_overscroll: False
                        do_scroll_x: False
                        pos_hint: {"right": 1}
                        size_hint: (None, None)
                        width: root.width - 70
                        height: root.height - 70 - 40

                        GridLayout:
                            id: main_menu_grid_layout
                            pos_hint: {"top": 1}
                            size_hint: (None, None)
                            width: scroll_view.width 
                            height: self.minimum_height 
                            padding: [20, 20, 20, 20]
                            spacing: 20
                            cols: 5

                TabbedPanelItem:
                    text: "Collections"
                    Label:
                        text: "CCCC"    

                TabbedPanelItem:
                    text: "Authors"
                    Label:
                        text: "XXXXX"    
     
        Screen:
            name: "Read Currently Open File Screen"
            MDLabel:
                text: "Read Currently Open File Screen"
                halign: "center"
        
        Screen:
            name: "Settings Screen"
            
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
        canvas.before:
            Color:
                rgba: 0, 1, 1, 1

        id: nav_bar
        orientation: 'vertical'
        pos_hint: {"left": 0, "y": 0}

        MDIconButton:
            pos_hint: {"y": 1}
            width: 70
            height: 70
            on_press: screen_manager.current = "Main Menu"
        
        MDIconButton:
            pos_hint: {"center_y": 1}
            width: 70
            height: 70
            color : [1.0, 1.0, 1.0, 1.0]

        MDIconButton:
            pos_hint: {"center_y": 1}
            width: 70
            height: 70
            color : [1.0, 1.0, 1.0, 1.0]
            on_press: screen_manager.current = "Main Menu"
            on_press: toolbar.title = "Main Menu"

        MDIconButton:
            pos_hint: {"y": 1}
            width: 70
            height: 70
            color : [1.0, 1.0, 1.0, 1.0]
            on_press: screen_manager.current = "Read Currently Open File Screen"

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
                on_press: screen_manager.current = "Settings Screen"
                on_press: toolbar.title = "Settings"
                # add onperss that will add in element to array for previous frames

'''

#  see if you can get the location of the mouse and hide the navbar in the currently reading frame and only show it if mouse is in position
#  get the box layout to change position
#  add widget on the end of grid with button to remove and label that shows folder directory

# make widgets in main menu
# do the drives in fileselect
# add folder to scan func
# add widgets for folders in settings

class AddLocalFolderToScanDialog():
    '''AddLocalFolderToScanDialog'''

class LocalFoldersExpansionPanelContent(BoxLayout):
    '''LocalFoldersExpansionPanelContent'''

class FileReaderApp(MDApp):

    files_with_widgets_list : list = []

    def add_main_menu_widgets(self, file_list):

        for file in file_list["array_of_epub_files"]:
            
            if self.files_with_widgets_list.count(file) == 0 :

                file_title = epub_file_data.get_epub_book_title(file)
                file_author = epub_file_data.get_epub_book_author(file)
                file_cover = epub_file_data.get_epub_cover_image(file)

                card = MDCard(
                        orientation = "vertical",
                        size_hint = (None, None),
                        height = 500,
                        width = 300,
                        radius = [0, 0, 0, 0]
                    )
                self.root.ids.main_menu_grid_layout.add_widget(card)
                print(file_cover, " ", type(file_cover))

                box_layout = BoxLayout(
                    orientation = "vertical",
                )
                card.add_widget(box_layout)

                # img = Image.open(file_cover)
                # print(img.size, img.mode, len(img.getdata()))
                # print(type(img))


                # with zipfile.ZipFile("C:/Users/gmn/Downloads/Cover.zip") as myzip:
                #     with myzip.open('Cover.jpg') as myfile:
                #         ci = CoreImage(io.BytesIO(myfile.read()), ext="jpg")
                #         return Image(texture=ci.texture)

                # icon = MDIconButton(
                #         icon = ("icons and images\icons8-settings-500.png"),
                #         pos_hint = {"top": 1, "center_x": 1}
                        
                #     )
                # box_layout.add_widget(icon)

                if file_cover != None:
                    pass

                if file_title != None:
                    file_title_button = KivyButton(
                    text = file_title,
                    color = (0, 0, 0, 1),
                    size_hint = (1, None),
                    height = 50,
                    # width = 300,
                    # set position
                    )
                    card.add_widget(file_title_button)
                if file_author != None:
                    # on_press = ,
                    file_author_button = KivyButton(
                    text = file_author,
                    color = (0, 0, 0, 1),
                    size_hint = (1, None),
                    height = 50,
                    # width = 300,
                    )
                    card.add_widget(file_author_button)
                    self.files_with_widgets_list.append(file)

    def add_buttons_for_drives(self):
        available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
        for drive in available_drives:
            pass
            # super.LocalFolderPopUp.ids.folder_chooser_box_layout_vertical.add_widget(
            #     KivyButton(
            #         text = "{drive}"
            #     )
            # )
            # print(drive)

    def add_folder_to_scan_folder_selected(self, folder_selected):
        available_file_paths_dictonary = scan_folders.scan_folders(str(folder_selected), True)
        self.add_main_menu_widgets(available_file_paths_dictonary)

    def build(self):
        self.title = "Book Reader"
        return Builder.load_string(Kivy)
    
    def full_scan(self):
        if exists("Book Worm\Book Worm\local_folders_to_scan.json"):
            file = open("Book Worm\Book Worm\local_folders_to_scan.json", "r")
            json_file_data = file.read()
            file.close()
            if json_file_data != "":
                available_file_paths_dictonary = scan_folders.scan_folders(json_file_data.split(","), False)
                self.add_main_menu_widgets(available_file_paths_dictonary)

    def local_folders_and_files_scan(self): 
        if exists("Book Worm\Book Worm\local_folders_to_scan_dictonary.json"):
            file = open("Book Worm\Book Worm\local_folders_to_scan_dictonary.json", "r")
            json_file_data = file.read()
            file.close()
            if json_file_data != "":
                available_file_paths_dictonary = scan_folders.scan_folders(json_file_data, False)
                self.add_main_menu_widgets(available_file_paths_dictonary)
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

    def on_start(self):
        self.create_local_folders_to_scan_expansion_panel()
        self.local_folders_and_files_scan()
    
FileReaderApp().run()

# on navbar add a searchbar iconbutton, on press expand it to a full searchbar
# if cash exists then do fullscan seconds after the software has booted properly

# workaround for sorting is creating arrays that are sorted by date/alphabetically/etc, and just following array