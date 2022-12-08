from cProfile import label
from logging import root
from msilib.schema import File
from kivy.config import Config
Config.set("input", "mouse", "mouse,multitouch_on_demand")
Config.set("graphics", "minimum_width", "700")
Config.set("graphics", "minimum_height", "400")
# config kivy window_icon
# graphics:
#  window_state 
# height
# width
# left
# position
# top
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.card import MDCard
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.button import MDIconButton
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.image import Image as CoreImage
from kivy.uix.button import Button as KivyButton
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
import cbz_file_data
import cbr_file_data
import text_file_data 
import epub_file_data
import audio_file_data_music_tag
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
import rarfile
from itertools import cycle
import kivy_garden.contextmenu as ContextMenu
from kivy.factory import Factory

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
            id: local_folder_popup_scroll_view
            always_overscroll: False
            do_scroll_x: False
            size_hint: (None, 1)
            pos_hint: {"left": 1}
            width: 70
            BoxLayout:
                id: folder_chooser_box_layout_vertical
                width: local_folder_popup_scroll_view.width 
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
    local_folders_to_scan_expansion_panel_content_box_layout_folders_widget_list: local_folders_to_scan_expansion_panel_content_box_layout_folders_widget_list
    id: expansion_panel
    height: self.minimum_height
    adaptive_height: True
    orientation: "vertical"
    pos_hint: {"center_x": 0.5}
    size_hint: (1, None)
    padding: [20, 20, 20, 20]
    spacing: 20
    BoxLayout:
        height: self.minimum_height
        adaptive_height: True
        orientation: "vertical"
        pos_hint: {"center_x": 0.5}
        size_hint: (1, None)
        padding: [20, 20, 20, 20]
        spacing: 20
        Button:
            text: "Add Local Folder To Scan"
            size_hint: (1, None)
            pos_hint: {"center_x": 0.5, "top": 1}
            on_press: Factory.LocalFolderPopUp().open()
        BoxLayout:
            id: local_folders_to_scan_expansion_panel_content_box_layout_folders_widget_list
            height: self.minimum_height
            adaptive_height: True
            orientation: "vertical"
            pos_hint: {"center_x": 0.5}
            size_hint: (1, None)
            padding: [20, 20, 20, 20]
            spacing: 20

<MainMenuFilesContextMenu>
    ContextMenu:
        id: context_menu
        visible: True
        cancel_handler_widget: layout

        ContextMenuTextItem:
            text: "SubMenu #2"
        ContextMenuTextItem:
            text: "SubMenu #3"

Screen:
    GridLayout:
        id: root_screen_horizontal_box_layout
        cols: 2
        width: self.minimum_width
        size_hint: (None, 1)
        MDCard:
            id: navbar
            size_hint: (None, 1)
            width: 50
            pos_hint: {"left": 0, "y": 0}
            md_bg_color: (0, 0, 1, 1)
            radius: [0, 0, 0, 0]
            ScrollView:
                id: navbar_scroll_view
                always_overscroll: False
                do_scroll_x: False
                pos_hint: {"right": 1}
                size_hint: (None, None)
                width: 50
                height: root.height
                BoxLayout:
                    id: nav_bar
                    padding: [10, 10, 10, 10]
                    spacing: 20    
                    orientation: "vertical"
                    pos_hint: {"left": 0, "y": 0}
                    size_hint_x: None
                    width: navbar.width
                    height: self.minimum_height
                    MDIconButton:
                        pos_hint: {"y": 1}
                        width: navbar.width
                        height: navbar.width
                        icon: "icons and images\go back.png"
                        icon_size: 5
                        on_press: app.return_to_previous_tab_or_screen()
                    MDIconButton:
                        pos_hint: {"center_y": 1}
                        width: navbar.width
                        height: navbar.width
                        color : [1.0, 1.0, 1.0, 1.0]      
                        icon: "icons and images\search.png"
                        icon_size: 5
                    MDIconButton:
                        pos_hint: {"center_y": 1}
                        width: navbar.width
                        height: navbar.width
                        color : [1.0, 1.0, 1.0, 1.0]
                        icon: "icons and images\Home-icon.svg.png" 
                        icon_size: 5
                        on_press: app.change_screen("Main Menu", False)
                    MDIconButton:
                        pos_hint: {"y": 1}
                        width: navbar.width
                        height: navbar.width
                        color : [1.0, 1.0, 1.0, 1.0]
                        icon_size: 5
                        on_press: app.change_screen("Read Currently Open File Screen", False)
                    MDIconButton:
                        pos_hint: {"y": 1}
                        width: navbar.width
                        height: navbar.width
                        color : [1.0, 1.0, 1.0, 1.0]
                        icon_size: 5
                        on_press: app.change_screen("Album Inspector Screen", False)


                    # <HoverItem@MDIconButton+HoverBehavior>:
                    #     id: reading_sign_collections_navbar_button
                    #     pos_hint: {"y": 1}
                    #     width: navbar.width
                    #     height: navbar.width
                    #     color : [1.0, 1.0, 1.0, 1.0]
                    #     icon_size: 5
                    #     on_enter: reading_sign_collections_navbar_card.height = reading_sign_collections_navbar_button.height
                    #     on_enter: reading_sign_collections_navbar_card.width = 150

                    MDIconButton:
                        id: reading_sign_collections_navbar_button
                        pos_hint: {"y": 1}
                        width: navbar.width
                        height: navbar.width
                        color : [1.0, 1.0, 1.0, 1.0]
                        icon_size: 5

                        on_press: app.change_widget_width(reading_sign_collections_navbar_card, 150)
                        on_press: reading_sign_collections_navbar_card.height = reading_sign_collections_navbar_button.height

                    #     HoverBehavior:
                    #         on_enter: reading_sign_collections_navbar_card.height = reading_sign_collections_navbar_button.height
                    #         on_enter: reading_sign_collections_navbar_card.width = 150

                    #     # on enter and on press get the thing to expand and show up, animate it
                    #     # on leave, reverse the animation


                    #     # on_enter: reading_sign_collections_navbar_card.height = reading_sign_collections_navbar_button.height
                    #     # on_enter: reading_sign_collections_navbar_card.width = 150


                    #     # on_leave: reading_sign_collections_navbar_card.height = 0
                    #     # on_leave: reading_sign_collections_navbar_card.width = 0


                    BoxLayout:
                        id: nav_bar_settings
                        orientation: "vertical"
                        pos_hint: {"left": 0, "y": 0}
                        MDIconButton:
                            width: navbar.width
                            height: navbar.width
                            pos_hint: {"y": 0}
                            md_bg_color : [1.0, 1.0, 1.0, 1.0]
                            icon: "icons and images\icons8-settings-500.png" 
                            icon_size: 5
                            on_press: app.change_screen("Settings Screen", False)
        GridLayout:
            id: root_screen_vertical_box_layout
            size_hint: (None, None)
            width: root.width - navbar.width
            height: root.height
            rows: 3
            MDCard:
                id: toolbar
                size_hint: (1, None)
                height: 50
                md_bg_color: (0, 145, 255, 1)
                radius: [0, 0, 0, 0]
                Label:
                    id: toolbar_label
                    font_size: "25sp"
                    text: "Book Reader"
                    color: (0, 0, 0, 1)
                    text_size: self.size
                    halign: "left"
                    valign: "center"
            ScreenManager:
                id: screen_manager
                Screen:
                    id: main_menu_screen
                    name: "Main Menu"
                    on_pre_enter: app.change_widget_height(toolbar, 50)
                    on_pre_enter: app.change_widget_opacity(toolbar, 1)
                    on_enter: toolbar_label.text = "Main Menu"
                    size_hint: (None, None)
                    width: root.width - navbar.width
                    height: root_screen_vertical_box_layout.height - audio_player_card.height - toolbar.height
                    y: 0
                    TabbedPanel:
                        id: main_menu_tabbed_panel
                        do_default_tab: False
                        tab_pos: "top_left"
                        size_hint: (None, None)
                        width: root.width - navbar.width
                        height: root_screen_vertical_box_layout.height - audio_player_card.height - toolbar.height
                        tab_width: 150
                        pos_y: 0
                        y: 0
                        TabbedPanelItem:
                            id: main_menu_files_tab
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
                                    width: root.width - navbar.width
                                    height: root.height - toolbar.height - 40 - 5 - 30 - audio_player_card.height
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
                            id: main_menu_authors_tab
                            text: "Authors"
                            Label:
                                text: "CCCC"    
                        TabbedPanelItem:
                            id: main_menu_collections_tab
                            text: "Collections"
                            Label:
                                text: "XXXXX"
                Screen:
                    name: "Read Currently Open File Screen"
                    on_pre_enter: app.change_widget_height(toolbar, 0)
                    on_pre_enter: app.change_widget_opacity(toolbar, 0)
                    on_pre_enter: app.change_widget_width(navbar, 0)
                    on_enter: toolbar_label.text = ""
                    MDCard:
                        id: file_reader_content_card
                        orientation: "vertical"
                        size_hint: (None, None)
                        pos_hint: {"center_x": 0.5}
                        width: 1100
                        height: root.height - audio_player_card.height - toolbar.height
                        radius: [0, 0, 0, 0]
                        ScrollView:
                            id: file_reader_content_scroll_view
                            always_overscroll: False
                            do_scroll_x: False
                            pos_hint: {"right": 1}
                            size_hint: (None, None)
                            width: file_reader_content_card.width
                            height: file_reader_content_card.height
                            BoxLayout:
                                id: file_reader_content_box_layout
                                pos_hint: {"top": 1}
                                size_hint: (None, None)
                                width: file_reader_content_scroll_view.width 
                                height: self.minimum_height 
                                orientation: 'vertical'
                    FloatLayout:
                        size_hint: (1, 1)
                        MDCard:
                            id: file_reader_floating_options_card
                            size_hint: (None, None)
                            height: 40
                            width: self.minimum_width
                            pos: (300, 300)
                            radius: [0, 0, 0, 0]
                            md_bg_color: (0, 0, 0, 1)
                            BoxLayout:
                                id: file_reader_floating_options_card_horizontal_box_layout
                                orientation: "horizontal"
                                padding: [5, 5, 5, 5]
                                spacing: 5
                                size_hint: (1, 1)
                                BoxLayout:
                                    id: file_reader_floating_options_card_move_button_box_layout
                                    orientation: "horizontal"
                                    size_hint: (1, 1)
                                    Button:
                                        id: file_reader_floating_options_card_move_button
                                        text: ":"
                Screen:
                    name: "File Details Screen"
                    on_pre_enter: app.change_widget_height(toolbar, 50)
                    on_pre_enter: app.change_widget_opacity(toolbar, 1)
                    on_enter: toolbar_label.text = "File Detail Screen"
                    MDLabel:
                        text: "File Details Screen"
                        halign: "center"
                Screen:
                    name: "Album Inspector Screen"
                    on_pre_enter: app.change_widget_height(toolbar, 0)
                    on_pre_enter: app.change_widget_opacity(toolbar, 0)
                    on_enter: toolbar_label.text = ""
                    ScrollView:
                        id: album_inspector_scroll_view
                        always_overscroll: False
                        do_scroll_x: False
                        pos_hint: {"right": 1}
                        size_hint: (None, None)
                        width: root.width - navbar.width
                        height: root.height - audio_player_card.height
                        BoxLayout:
                            id: album_inspector_box_layout
                            pos_hint: {"top": 1}
                            size_hint: (None, None)
                            width: album_inspector_scroll_view.width 
                            height: self.minimum_height 
                            orientation: "vertical"
                Screen:
                    name: "Settings Screen"
                    on_pre_enter: app.change_widget_height(toolbar, 50)
                    on_pre_enter: app.change_widget_opacity(toolbar, 1)
                    on_enter: toolbar_label.text = "Settings"
                    TabbedPanel:
                        do_default_tab: False
                        tab_pos: "top_mid"
                        size_hint: (None, None)
                        tab_width: 200
                        pos_hint: {"right": 1}
                        width: root.width - navbar.width
                        height: root.height - audio_player_card.height - toolbar.height
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
                                width: root.width - navbar.width
                                height: root.height - toolbar.height - 40
                                BoxLayout:
                                    id: settings_scanning_folders_tab_box_layout
                                    pos_hint: {"top": 1}
                                    size_hint: (None, None)
                                    width: scroll_view.width 
                                    height: self.minimum_height 
                                    orientation: "vertical"
                                    Label:
                                        text: "Local Folders To Scan"
                                        font_size: 20
                                        halign: "left"
                                        size_hint: (None, None)
                                        pos_hint: {"left": 1, "top": 1}
                                        width: 250
                                        height: 50
                                    BoxLayout:
                                        id: settings_scanning_local_folders_tab_box_layout
                                        pos_hint: {"center_x": 0.5}
                                        size_hint: (0.8, None)
                                        height: self.minimum_height 
                                        orientation: "vertical"
                        TabbedPanelItem:
                            text: "About"
                            Label:
                                text: "cxzczxc"
            MDCard:
                id: audio_player_card
                size_hint: (None, None)
                height: 70
                width: root.width - 70
                pos_hint: {"right": 1, "bottom": 0}
                md_bg_color: (1, 1, 1, 1)
                radius: [0, 0, 0, 0]
                BoxLayout:
                    orientation: "horizontal"
                    width: root.width - navbar.width
                    Button:
                        id: audio_player_card_file_viewer_button
                        pos_hint: {"bottom": 1}
                        size_hint: (None, 1)
                        width: 300
                        BoxLayout:
                            orientation: "horizontal"
                            pos_hint: {"bottom": 1, "left": 1}
                            size_hint: (None, None)
                            pos: audio_player_card_file_viewer_button.pos
                            height: audio_player_card_file_viewer_button.height
                            Image:
                                id: audio_player_card_cover_image
                                allow_stretch: True
                                keep_ratio: True
                                pos_hint: {"bottom": 1, "left": 1}
                        BoxLayout:
                            orientation: "vertical"
                            pos_hint: {"bottom": 1, "right": 1}
                            size_hint: (None, None)
                            pos: audio_player_card_file_viewer_button.pos
                            x: audio_player_card_cover_image.x + audio_player_card_cover_image.width + 10
                            height: audio_player_card_file_viewer_button.height
                            Label:
                                id: audio_player_card_file_title_label
                            Label:
                                id: audio_player_card_file_author_label
                    BoxLayout:
                        orientation: "vertical"
                        BoxLayout:
                            orientation: "horizontal"
                            Button:
                                id: audio_player_card_play_previous_track_button
                                on_press: app.on_play_previous_audio_file_button_pressed()
                                text: "<"
                                size_hint: (None, 1)
                                width: 60
                            Button:
                                id: audio_player_card_pause_resume_button
                                on_press: app.on_pause_resume_audio_file_button_pressed()
                                text: "||"
                                size_hint: (None, 1)
                                width: 60
                            Button:
                                id: audio_player_card_play_next_track_button                     
                                on_press: app.on_play_next_audio_file_button_pressed()
                                text: ">"
                                size_hint: (None, 1)
                                width: 60
                        BoxLayout:
                            orientation: "horizontal"

                            # time current

                            # timeline
                            Label:
                                id: audio_player_card_file_lenght_label 
    FloatLayout:
        size_hint: (1, 1)
        MDCard:
            id: reading_sign_collections_navbar_card
            size_hint: (None, None)
            # width: 150
            # height: reading_sign_collections_navbar_button.height
            # size: (0, 0)
            width: 0
            height: 0
            x: reading_sign_collections_navbar_button.x + reading_sign_collections_navbar_button.width
            y: reading_sign_collections_navbar_button.y
            md_bg_color: (0, 0, 1, 1)
            radius: [0, 0, 0, 0]

'''

# navbar searchbar buton on press expand it to a full searchbar
# audio file module for playing audio files
# in the future check if file that gets to sound loader is compatible with sound loader

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
    
class MainMenuFilesContextMenu():
    '''MainMenuFilesContextMenu'''

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
                        radius = [0, 0, 0, 0],
                        md_bg_color = (0, 0, 0, 0)
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
                        radius = [0, 0, 0, 0],
                        md_bg_color = (0, 0, 0, 0)
                    )
                app.root.ids.main_menu_grid_layout.add_widget(card)
                if file_cover != None:
                    cover_image = CoreImage(io.BytesIO(file_cover), ext = "jpg")
                    file_cover_button = KivyButton(
                        background_color = (0, 0, 0, 0),
                        pos_hint = {"bottom": 1}
                        )
                    file_cover_image = Image(
                        texture = CoreImage(cover_image).texture,
                        allow_stretch = True,
                        keep_ratio = True,
                        pos_hint = {"bottom": 1},
                        )
                    file_cover_button.bind(size = file_cover_image.setter("size"))
                    file_cover_button.bind(pos = file_cover_image.setter("pos"))
                    file_cover_button.add_widget(file_cover_image)
                else:
                    file_cover_button = KivyButton(
                        on_press = lambda x: app.change_screen("Read Currently Open File Screen", False),
                        text = "File Cover Image Not Found",
                        color = (0, 0, 0, 1),
                        size_hint = (1, None),
                        height = 50,
                        # width = 300,
                    )
                file_cover_button.bind(on_press = lambda button: app.main_menu_file_widget_pressed(file, button))
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
                        radius = [0, 0, 0, 0],
                        md_bg_color = (0, 0, 0, 0)
                    )
                app.root.ids.main_menu_grid_layout.add_widget(card)
                if file_cover != None:
                    cover_image = CoreImage(io.BytesIO(file_cover), ext = "jpg")
                    file_cover_button = KivyButton(
                        background_color = (0, 0, 0, 0),
                        pos_hint = {"bottom": 1}
                        )
                    file_cover_image = Image(
                        texture = CoreImage(cover_image).texture,
                        allow_stretch = True,
                        keep_ratio = True,
                        pos_hint = {"bottom": 1},
                        )
                    file_cover_button.bind(size = file_cover_image.setter("size"))
                    file_cover_button.bind(pos = file_cover_image.setter("pos"))
                    file_cover_button.add_widget(file_cover_image)
                else:
                    file_cover_button = KivyButton(
                        on_press = lambda x: app.change_screen("Read Currently Open File Screen", False),
                        text = "File Cover Image Not Found",
                        color = (0, 0, 0, 1),
                        size_hint = (1, None),
                        height = 50,
                        # width = 300,
                    )
                file_cover_button.bind(on_press = lambda button: app.main_menu_file_widget_pressed(file, button))
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
            elif file["file_format"] == "cbr":
                file_title = cbr_file_data.get_cbr_file_title(file["absolute_file_path"])
                print(file_title)
                file_author = file["file_author"]
                print(file["file_cover"], type(file["file_cover"]))
                # cbr_file_data.get_cbr_file_content(file["absolute_file_path"])
                # file_cover = rarfile.RarFile(file["absolute_file_path"])
                # file_cover.read(file["file_cover"])
                # print(file_cover, type(file_cover))
                file_cover = None
                card = MDCard(
                        orientation = "vertical",
                        size_hint = (None, None),
                        height = app.main_menu_files_widgets_height,
                        width = app.main_menu_files_widgets_width,
                        radius = [0, 0, 0, 0],
                        md_bg_color = (0, 0, 0, 0)
                    )
                app.root.ids.main_menu_grid_layout.add_widget(card)
                if file_cover != None:
                    cover_image = CoreImage(io.BytesIO(file_cover), ext = "jpg")
                    file_cover_button = KivyButton(
                        background_color = (0, 0, 0, 0),
                        pos_hint = {"bottom": 1}
                        )
                    file_cover_image = Image(
                        texture = CoreImage(cover_image).texture,
                        allow_stretch = True,
                        keep_ratio = True,
                        pos_hint = {"bottom": 1},
                        )
                    file_cover_button.bind(size = file_cover_image.setter("size"))
                    file_cover_button.bind(pos = file_cover_image.setter("pos"))
                    file_cover_button.add_widget(file_cover_image)
                else:
                    file_cover_button = KivyButton(
                        on_press = lambda x: app.change_screen("Read Currently Open File Screen", False),
                        text = "File Cover Image Not Found",
                        color = (0, 0, 0, 1),
                        size_hint = (1, None),
                        height = 50,
                        # width = 300,
                    )
                file_cover_button.bind(on_press = lambda button: app.main_menu_file_widget_pressed(file, button))
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
            elif (file["file_format"] in app.music_tag_compatible_file_formats):
                album_title = file["file_name"]
                album_author = file["file_author"]
                file_cover = audio_file_data_music_tag.get_audio_file_data_music_tag_artwork(file["album_tracks_dictionary"][0]["absolute_file_path"])
                card = MDCard(
                        orientation = "vertical",
                        size_hint = (None, None),
                        height = app.main_menu_files_widgets_height,
                        width = app.main_menu_files_widgets_width,
                        radius = [0, 0, 0, 0],
                        md_bg_color = (0, 0, 0, 0)
                    )
                app.root.ids.main_menu_grid_layout.add_widget(card)
                if file_cover != None:
                    cover_image = CoreImage(io.BytesIO(file_cover), ext = "jpg")
                    file_cover_button = KivyButton( 
                        background_color = (0, 0, 0, 0),
                        pos_hint = {"bottom": 1}
                        )
                    file_cover_image = Image(
                        texture = CoreImage(cover_image).texture,
                        allow_stretch = True,
                        keep_ratio = True,
                        pos_hint = {"bottom": 1},
                        y = 0
                        )
                    file_cover_button.bind(size = file_cover_image.setter("size"))
                    file_cover_button.bind(pos = file_cover_image.setter("pos"))
                    file_cover_button.add_widget(file_cover_image)
                else:
                    file_cover_button = KivyButton(
                        on_press = lambda x: app.change_screen("Album Inspector Screen", False),
                        text = "File Cover Image Not Found",
                        color = (0, 0, 0, 1),
                        size_hint = (1, None),
                        height = 50,
                        # width = 300,
                    )
                file_cover_button.bind(on_press = lambda button: app.main_menu_file_widget_pressed(file, button))
                card.add_widget(file_cover_button)                        
                if album_title != None:
                    file_title_button = KivyButton(
                        on_press = lambda x: app.change_screen("Album Inspector Screen", False),
                        text = album_title,
                        color = (0, 0, 0, 1),
                        size_hint = (1, None),
                        height = 50,
                        # width = 300,
                    )
                else:
                    file_title_button = KivyButton(
                    on_press = lambda x: app.change_screen("Album Inspector Screen", False),
                    text = "File Title Not Found",
                    color = (0, 0, 0, 1),
                    size_hint = (1, None),
                    height = 50,
                    # width = 300,
                    )
                file_title_button.bind(on_press = lambda x: app.load_album_inspector_screen(file))  
                card.add_widget(file_title_button)
                if album_author != None:
                    file_author_button = KivyButton(
                        text = album_author,
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

    class Album_Track():
        def __init__(self, app, album_track, track_item_number, album_track_list):
            if (track_item_number % 2) == 0:
                card_background_color = app.album_track_card_primary_color
            else:
                card_background_color = app.album_track_card_secondary_color
            card = MDCard(
                orientation = "horizontal",
                size_hint = (1, None),
                height = 50,
                radius = [0, 0, 0, 0],
                md_bg_color = card_background_color
            )
            play_button = KivyButton(
                text = "Play",
                size_hint = (None, 1),
                width = 50,
                # on_press = lambda x: app.play_album_track(album_track)
                on_press = lambda x: app.play_audio_file_list(album_track, False, True)
            )
            card.add_widget(play_button)
            track_number_label = Label(
                size_hint = (None, 1),
                width = 30,
                color = (0, 0, 0, 1)
            )
            if album_track["track_number"] != "":
                album_track.text = album_track["track_number"] + ".",
            card.add_widget(track_number_label)
            track_title_label = Label(
                text = album_track["track_title"],
                halign = "left",
                size_hint = (None, 1),
                width = 300,
                color = (0, 0, 0, 1)
            )
            card.add_widget(track_title_label)
            track_artist_label = KivyButton(
                text = album_track["track_artist"],
                size_hint = (None, 1),
                width = 300,
                color = (0, 0, 0, 1)
            )
            card.add_widget(track_artist_label)
            track_lenght_label = Label(
                text = album_track["track_lenght"],
                size_hint = (None, 1),
                width = 100,
                color = (0, 0, 0, 1),
                halign = "right"
            )
            track_lenght_label.bind(texture_size = track_lenght_label.setter("size"))
            card.add_widget(track_lenght_label)
            album_track_list.add_widget(card)

    class Album_Genres():
        def __init__(self, app, album_genre, header_genre_layout):
            genre_button = KivyButton(
                text = album_genre
            )
            header_genre_layout.add_widget(genre_button)

    class Folder_To_Scan_Card():
        def __init__(self, app, folder_selected):
            card = MDCard(
                orientation = "vertical",
                size_hint = (1, None),
                radius = [0, 0, 0, 0],
                md_bg_color = (0, 0, 0, 1),
                pos_hint = {"center_x": 0.5, "top": 1}
            )
            folder_selected_string = str(folder_selected)
            if folder_selected_string.startswith("['") and folder_selected_string.endswith("']"):
                folder_selected_string = folder_selected_string[2:-2]
            folder_path_label = Label(
                text = folder_selected_string
            )
            card.add_widget(folder_path_label)
            remove_folder_from_scan_list_button = KivyButton(
                on_press = lambda x: self.remove_folder_from_scan_list(app, card, folder_selected_string),
                text = "X",
                size = (50, 50),
                pos_hint = {"top": 1, "right": 1} 
            )
            card.add_widget(remove_folder_from_scan_list_button)
            app.root.ids.local_folders_to_scan_expansion_panel.content.ids.local_folders_to_scan_expansion_panel_content_box_layout_folders_widget_list.add_widget(card)

            # this isn't really doing anything
            app.root.ids.local_folders_to_scan_expansion_panel.content.height = app.root.ids.local_folders_to_scan_expansion_panel.content.minimum_height
            app.root.ids.local_folders_to_scan_expansion_panel.content.bind(minimum_height = app.root.ids.local_folders_to_scan_expansion_panel.content.setter("height"))

            # the problem might be the first box view in 'content' kv, not the second one

            # app.root.ids.local_folders_to_scan_expansion_panel.close_panel(app.root.ids.local_folders_to_scan_expansion_panel, app.root.ids.local_folders_to_scan_expansion_panel)
            # # Exception has occurred: TypeError
            # # MDExpansionPanel.close_panel() missing 2 required positional arguments: 'instance_expansion_panel' and 'press_current_panel'
            # app.root.ids.local_folders_to_scan_expansion_panel.open_panel()

            # fix position in regards to expansion panel and it going up
            # maybe just fix height

            # it's fine on reopening the expansion panel, so maybe just do that? 
            # or just do minimal size?

        def remove_folder_from_list_of_folders_json(self, folder):   
            if exists("Book Worm\Book Worm\local_folders_to_scan.json"):
                file = open("Book Worm\Book Worm\local_folders_to_scan.json", "r")
                json_file_data = file.read()
                file.close()
                if json_file_data != "":
                    list_of_folders_to_scan = eval(json_file_data)
                    if folder in list_of_folders_to_scan:
                        file = open("Book Worm\Book Worm\local_folders_to_scan.json", "w")
                        list_of_folders_to_scan.remove(folder)
                        file.write(json.dumps(list_of_folders_to_scan))
                        file.close()
        # when adding fodlers to folders to scan, check if it's a unique one, or if one already exists
        def remove_folder_files_from_file_dictionary_json(self, app, folder):
            list_of_subfolders = [name for name in os.listdir(folder)
                if os.path.isdir(os.path.join(folder, name))]
            # as it stands, to remove folder you've gotta open the file bellow twice, cut down on that
            local_folders_to_scan = open("Book Worm\Book Worm\local_folders_to_scan.json", "r")
            list_of_local_folders_to_scan = local_folders_to_scan.read()
            local_folders_to_scan.close()
            with open("Book Worm\Book Worm\local_folders_to_scan_dictonary.json") as local_files_dictionary:
                local_folders_to_scan_dictionary = json.load(local_files_dictionary)
                for subfolder in list_of_subfolders:
                    if subfolder not in list_of_local_folders_to_scan:
                        for file_index, file in enumerate(local_folders_to_scan_dictionary):
                            try:
                                if subfolder in file["absolute_file_path"]:
                                    local_folders_to_scan_dictionary.pop(file_index)          
                                else:
                                    print("nein", subfolder, file["absolute_file_path"])
                            except TypeError:
                                print("XXXX TypeError")
                                # absolute file path will be null for mp3 albums
                                # nabokov audio book sample doesn't show any info on the album view screen -> software is fine, it's the file's problem, but why can't you play that file?
                                pass


                # for file_index, file in enumerate(local_folders_to_scan_dictionary):

                    # if file["absolute_file_path"] # contains only root, and no further subfodlers
                        # do this by getting rid of the 'folder' string in file["absolute_file_path"] and cehcking if there are any other / signs left

                        # local_folders_to_scan_dictionary.pop(file_index)    

                print(local_folders_to_scan_dictionary)
                file = open("Book Worm\Book Worm\local_folders_to_scan_dictonary.json", "w")
                file.write(json.dumps(local_folders_to_scan_dictionary))
                file.close()  
            app.local_folders_and_files_scan()
            app.add_main_menu_widgets()   

        def remove_folder_from_scan_list(self, app, card, folder):
            app.root.ids.local_folders_to_scan_expansion_panel.content.ids.local_folders_to_scan_expansion_panel_content_box_layout_folders_widget_list.remove_widget(card)
            # resize expansion panel
            app.root.ids.local_folders_to_scan_expansion_panel.content.height = app.root.ids.local_folders_to_scan_expansion_panel.content.minimum_height
            self.remove_folder_from_list_of_folders_json(folder)
            self.remove_folder_files_from_file_dictionary_json(app, folder)
            # what if files has been removed but is still open in album viewer/file deatails/file reader screen?

    navbar_width_max = 50
    list_of_files = []
    currently_open_file = None
    currently_open_album = None 
    screen_currently_in_use :int = 0
    previous_screens_and_tabs_list = ["Main Menu"]
    main_menu_files_widgets_height = None
    main_menu_files_widgets_width = None
    album_track_card_primary_color = (1, 1, 1, 1)
    album_track_card_secondary_color = (0.9, 0.9, 0.9, 1)
    kivy_compatible_image_files = ["jpeg", "jpg", "png", "gif"]
    music_tag_compatible_file_formats = ["wav_album", "ogg_album", "mp3_album", "aac_album", "flac_album", "wv_album", "m4a_album", "opus_album", "dsf_album", "aiff_album"]
    kivy_music_loader = SoundLoader
    track_currently_playing_index = 0
    list_of_audio_files_to_play = [None]
    about_to_play_another_track_bool = None
    kivy_music_loader_position_at_track_paused = None

    def main_menu_file_widget_pressed(self, file, button):
        if button.last_touch.button == "left":
            if file["file_format"] in self.music_tag_compatible_file_formats:
                self.change_screen("Album Inspector Screen", False)
                self.load_album_inspector_screen(file)
            else:
                self.change_screen("Read Currently Open File Screen", False)
                self.load_file_read_screen(file)
        elif button.last_touch.button == "right":
            print("right mouse clicked")
            # in ky create context menu class
            # show the class

            MainMenuFilesContextMenu()
        # self.root.ids.context_menu.show(*app.root_window.mouse_pos)
        
    def change_widget_height(self, widget_id, new_value):
        animation = Animation(height = new_value)
        if widget_id == self.root.ids.toolbar:
            if self.root.ids.toolbar.height != new_value:
                animation.start(self.root.ids.toolbar)
        elif widget_id == self.root.ids.reading_sign_collections_navbar_card:
            if self.root.ids.reading_sign_collections_navbar_card.height != new_value:
                animation.start(self.root.ids.reading_sign_collections_navbar_card)

    def change_widget_width(self, widget_id, new_value):
        animation = Animation(width = new_value)
        try:
            if widget_id == self.root.ids.reading_sign_collections_navbar_card:
                if self.root.ids.reading_sign_collections_navbar_card.width != new_value:
                    animation.start(self.root.ids.reading_sign_collections_navbar_card)
        except AttributeError:
            print("AttributeError, change_widget_width, widget_id")
            if widget_id == self.root.ids.navbar:
                if self.root.ids.navbar.width != new_value:
                    animation.start(self.root.ids.navbar)
                    # for child in self.root.ids.navbar.children:
                    #     child.width = new_value
                    # self.root.ids.navbar.width = new_value

    def change_widget_opacity(self, widget_id, new_value):
        animation = Animation(opacity = new_value)
        if widget_id == self.root.ids.toolbar:
            if self.root.ids.toolbar.opacity != new_value:
                animation.start(self.root.ids.toolbar)

    def on_pause_resume_audio_file_button_pressed(self):
        if self.kivy_music_loader != None:
            if self.kivy_music_loader.state == "stop" and self.kivy_music_loader_position_at_track_paused != None:
                self.kivy_music_loader.play()
                self.kivy_music_loader.seek(self.kivy_music_loader_position_at_track_paused)
            else:
                self.kivy_music_loader_position_at_track_paused = self.kivy_music_loader.get_pos()
                self.kivy_music_loader.stop()

    def on_play_next_audio_file_button_pressed(self):
        if len(self.list_of_audio_files_to_play) - self.track_currently_playing_index > self.track_currently_playing_index + 1:
            self.track_currently_playing_index += 1
            self.about_to_play_another_track_bool = True
            self.set_sound_loader_file()

    def on_play_previous_audio_file_button_pressed(self):
        if self.track_currently_playing_index >= 2:
            self.track_currently_playing_index -= 1
            self.about_to_play_another_track_bool = True
            self.set_sound_loader_file()

    def play_audio_file_list(self, track_or_album_file, play_full_album_bool, play_now_bool):
        # check that there aren't 2 same tracks in a row? check if the new file is the same as the old file
        if play_full_album_bool == True:
            # this is always a play now?
            track_currently_playing_index = self.track_currently_playing_index
            for track in track_or_album_file["album_tracks_dictionary"]:
                track_and_album_dictionary = {
                    "track": track,
                    "album": track_or_album_file
                }
                # self.list_of_audio_files_to_play.insert(track_currently_playing_index + 1, track)
                self.list_of_audio_files_to_play.insert(track_currently_playing_index + 1, track_and_album_dictionary) #updated with dict
                track_currently_playing_index += 1
            self.on_play_next_audio_file_button_pressed()
        else: # what to do here, if the track_or_album_file is just a single track??????
            if play_now_bool == True:
                self.list_of_audio_files_to_play.insert(self.track_currently_playing_index + 1, track_or_album_file)
                self.on_play_next_audio_file_button_pressed()
            else:
                self.list_of_audio_files_to_play.insert(self.track_currently_playing_index + 1, track_or_album_file)

    def set_sound_loader_file(self):
        try:
            self.kivy_music_loader.stop()
        except AttributeError:
            self.kivy_music_loader = None
        try:
            if self.kivy_music_loader == None or self.kivy_music_loader.source == None:
                for child in self.root.ids.audio_player_card.children:
                    child.opacity = 1
                animation = Animation(height = 70, opacity = 1)
                animation.start(self.root.ids.audio_player_card)
        except AttributeError:
            for child in self.root.ids.audio_player_card.children:
                child.opacity = 1
            animation = Animation(height = 70, opacity = 1)
            animation.start(self.root.ids.audio_player_card)
        self.kivy_music_loader = SoundLoader.load(self.list_of_audio_files_to_play[self.track_currently_playing_index]["absolute_file_path"])
        self.kivy_music_loader.play()
        self.kivy_music_loader.bind(on_stop = self.on_kivy_music_loader_stop)
        self.set_audio_player_card_widgets()
    
    def set_audio_player_card_widgets(self):
        file_currently_playing = self.list_of_audio_files_to_play[self.track_currently_playing_index]
        currently_playing_file_title = self.list_of_audio_files_to_play[self.track_currently_playing_index]["track_title"]
        currently_playing_file_author = self.list_of_audio_files_to_play[self.track_currently_playing_index]["track_artist"]
        currently_playing_file_path = self.list_of_audio_files_to_play[self.track_currently_playing_index]["absolute_file_path"]
        currently_playing_file_lenght = self.list_of_audio_files_to_play[self.track_currently_playing_index]["track_lenght"]
        currently_playing_file_cover = audio_file_data_music_tag.get_audio_file_data_music_tag_artwork(currently_playing_file_path)
        if currently_playing_file_cover != None:
            self.root.ids.audio_player_card_cover_image.texture = CoreImage(io.BytesIO(currently_playing_file_cover), ext = "jpg").texture
        self.root.ids.audio_player_card_file_title_label.text = currently_playing_file_title
        self.root.ids.audio_player_card_file_author_label.text = currently_playing_file_author
        self.root.ids.audio_player_card_file_lenght_label.text = currently_playing_file_lenght

        # find which album it is from the track data with:
        # iterate all albums

        # for album in list_of_albums:
        #     if album["file_album_title"] == track["track_album_title"] and album["file_album_artist"] == track["file_album_artist"]:
        #         if album["file_album_total_track_number"] == track["file_album_total_track_number"] and album["file_album_total_disk_number"] == track["file_album_total_disk_number"]:
        #             self.root.ids.audio_player_card_file_viewer_button.bind(on_press = lambda x: self.load_album_inspector_screen(album))  
        # self.root.ids.audio_player_card_file_viewer_button.bind(on_press = lambda x: self.change_screen("Album Inspector Screen", False))

        self.root.ids.audio_player_card_file_viewer_button.bind(on_press = lambda x: self.load_album_inspector_screen(self.list_of_audio_files_to_play[self.track_currently_playing_index]["album"]))  
        self.root.ids.audio_player_card_file_viewer_button.bind(on_press = lambda x: self.change_screen("Album Inspector Screen", False))

    def on_kivy_music_loader_stop(self, dt):
        if self.about_to_play_another_track_bool == True:
            self.about_to_play_another_track_bool = None
        else:
            # should you check if the leghts has been reached?
            if len(self.list_of_audio_files_to_play) > self.track_currently_playing_index + 1:
                self.track_currently_playing_index += 1
                self.set_sound_loader_file()

    def load_album_inspector_screen(self, file):
        if self.currently_open_album != file:
            self.root.ids.album_inspector_box_layout.clear_widgets()
            layout = BoxLayout(
                orientation = "vertical",
                size_hint = (1, None),
                pos_hint = {"left": 1}
                )
            header = BoxLayout(
                size_hint = (1, None),
                orientation = "horizontal"
                )
            file_cover = audio_file_data_music_tag.get_audio_file_data_music_tag_artwork(file["album_tracks_dictionary"][0]["absolute_file_path"])
            if file_cover != None:
                cover_image = CoreImage(io.BytesIO(file_cover), ext = "jpg")
                header_cover = Image(
                    texture = CoreImage(cover_image).texture
                )
                header.add_widget(header_cover)
            header_info_layout = BoxLayout(
                orientation = "vertical"
            )
            header.add_widget(header_info_layout)
            header_album_title = Label(
                text = file["file_name"],
                color = (0, 0, 0, 1)
            )
            header_info_layout.add_widget(header_album_title)
            header_album_author = KivyButton(
                text = file["file_author"]
            )
            header_info_layout.add_widget(header_album_author)
            header_album_release_year = Label(
                text = file["release_date"],
                color = (0, 0, 0, 1)
            )
            header_info_layout.add_widget(header_album_release_year)
            header_genre_layout = BoxLayout(
                orientation = "horizontal"
            )
            header_info_layout.add_widget(header_genre_layout)
            album_genres = file["album_genre"]
            for album_genre in album_genres:
                try:
                    if album_genre[0] == "'":
                        album_genre = album_genre[1:-1]
                except IndexError:
                    pass
                self.Album_Genres(self, album_genre, header_genre_layout)
            header_play_album_button = KivyButton(
                text = "Play Album",
                on_press = lambda x: self.play_audio_file_list(file, True, True)
            )
            header_info_layout.add_widget(header_play_album_button)
            album_track_list = BoxLayout(
                    orientation = "vertical",
                    size_hint = (1, None)
                )
            layout.add_widget(header)
            track_item_number = 0
            for album_track in file["album_tracks_dictionary"]:
                self.Album_Track(self, album_track, track_item_number, album_track_list)
                track_item_number += 1
            layout.add_widget(album_track_list)
            self.root.ids.album_inspector_box_layout.add_widget(layout)
            album_track_list.bind(minimum_height = album_track_list.setter("height"))
            layout.bind(minimum_height = layout.setter("height"))
            self.root.ids.album_inspector_box_layout.bind(minimum_height = self.root.ids.album_inspector_box_layout.setter("height"))
            self.currently_open_album = file
    
    def window_resized(self, *args):
        self.responsive_grid_layout()
        if self.root.ids.screen_manager.current == "Read Currently Open File Screen":
            self.set_file_reader_screen_page_focus_mode_scroll_distance()

    def set_file_reader_screen_page_focus_mode_scroll_distance(self):
        if self.root.ids.file_reader_content_box_layout_grid_layout_focus_mode != None:
            self.root.ids.file_reader_content_box_layout_grid_layout_focus_mode.spacing = Window.size[1]
            if self.root.ids.file_reader_content_box_layout_grid_layout_focus_mode.rows != None:
                scroll_distance = Window.size[1] + (Window.size[1] / self.root.ids.file_reader_content_box_layout_grid_layout_focus_mode.rows)
            else: 
                scroll_distance = Window.size[1] * 2
            self.root.ids.file_reader_content_scroll_view.scroll_distance = scroll_distance
            self.root.ids.file_reader_content_scroll_view.scroll_wheel_distance = scroll_distance
            for child in self.root.ids.file_reader_content_box_layout_grid_layout_focus_mode.children:
                child.height = Window.size[1] 

    def main_menu_file_widget_size(self, id):
        if id == self.root.ids.main_menu_file_widget_size_slider:
            self.main_menu_files_widgets_height = 1000 * id.value
            self.main_menu_files_widgets_width = 600 * id.value
            for child in self.root.ids.main_menu_grid_layout.children:
                child.height = self.main_menu_files_widgets_height
                child.width = self.main_menu_files_widgets_width
            self.responsive_grid_layout()

    def set_file_reader_floating_options_card(self, file_format, file_read_screen_mode):
        self.set_file_reader_floating_options_card_reading_mode_part(file_format, file_read_screen_mode)
        self.set_file_reader_floating_options_card_background_options_part()
        self.set_file_reader_floating_options_card_file_type_part(file_format, file_read_screen_mode) 
        
    def set_file_reader_floating_options_card_reading_mode_part(self, file_format, file_read_screen_mode):
        if file_read_screen_mode == "pageless infinite scroll":
            pass
        elif file_read_screen_mode == "pages and infinite scroll":
            pass
        elif file_read_screen_mode == "pages and focus":
            if file_format == "cbz":

                file_read_screen_mode_horizontal_box_layout = BoxLayout(
                    orientation = "horizontal"
                    )

                # add rows, cols

                self.root.ids.file_reader_floating_options_card_horizontal_box_layout.add_widget(file_read_screen_mode_horizontal_box_layout)

        elif file_read_screen_mode == "book simulator":                                                                                                                            
            pass

    def set_file_reader_floating_options_card_background_options_part(self):
        file_read_screen_background_options_horizontal_box_layout = BoxLayout(
            orientation = "horizontal"
        )

        # background color
        
        self.root.ids.file_reader_floating_options_card_horizontal_box_layout.add_widget(file_read_screen_background_options_horizontal_box_layout)

    def set_file_reader_floating_options_card_file_type_part(self, file_format, file_read_screen_mode):
        pass

    def load_file_read_screen(self, file):
        if self.currently_open_file != file:
            self.file_read_screen_mode(file)

    def file_read_screen_mode(self, file, *args):
        self.root.ids.file_reader_content_box_layout.clear_widgets()
        self.root.ids.file_reader_content_scroll_view.scroll_distance = 20
        self.root.ids.file_reader_content_scroll_view.scroll_wheel_distance = 20
        file_content = self.get_file_contents(file)
        if args == ():
            # there isn't a specified reading mode, so check defaults or previously used modes for this type or just previously used modes for any type
            # file specific?, file type specific mode?
            if file["file_format"] == "txt":
                args_as_list = list(args)
                args_as_list.append("pageless infinite scroll")
                args = tuple(args_as_list)
            elif file["file_format"] == "epub":
                args_as_list = list(args)
                args_as_list.append("pageless infinite scroll")
                args = tuple(args_as_list)
            elif file["file_format"] == "cbz":
                args_as_list = list(args)
                args_as_list.append("pages and focus")
                args = tuple(args_as_list)
        if args:
            if args[0] == "pageless infinite scroll":
                if file["file_format"] == "txt":
                    label = Label(
                            text = file_content,
                            color = [0, 0, 0, 1],
                            size_hint = (None, None),
                            halign = "left",
                            valign = "top",
                            size = self.root.ids.file_reader_content_box_layout.size
                        )
                    label.bind(texture_size = label.setter("size"))
                    self.root.ids.file_reader_content_box_layout.add_widget(label)
                    self.set_file_reader_floating_options_card(file["file_format"], args[0])
                elif file["file_format"] == "epub": 
                    for file in file_content:
                        if file["file_type"] == "html":
                            label = Label(
                                text = file["location_content"],
                                color = [0, 0, 0, 1],
                                size_hint = (None, None),
                                halign = "left",
                                valign = "top",
                                size = self.root.ids.file_reader_content_box_layout.size
                            )
                            label.bind(texture_size = label.setter("size"))
                            self.root.ids.file_reader_content_box_layout.add_widget(label)
                            # should there only be one widget? will that make it better for pages?
                    self.set_file_reader_floating_options_card("epub", args[0])
                elif file["file_format"] == "cbz": 
                    self.file_read_screen_mode(file, "pages and focus")
                    self.set_file_reader_floating_options_card("cbz", args[0])
            elif args[0] == "pages and infinite scroll":
                if file["file_format"] == "cbz": 
                    grid_layout = GridLayout(
                        cols = 1, # save from previous session, do same with rows (if they aren't default)
                        size_hint = (1, 1),
                        pos_hint = {"center_x": 0.5}
                    )
                    self.root.ids.file_reader_content_box_layout.add_widget(grid_layout)
                    for file_item in file_content:
                        if file_item["file_format"] in self.kivy_compatible_image_files:
                            # this part of the code isn't working; sizes, size hints and such are issues
                            image = CoreImage(io.BytesIO(file_item["file"]), ext = "jpg")
                            file_image = Image(
                                texture = CoreImage(image).texture,
                                size_hint = (None, None),
                                # height = 400,
                                # width = 400,
                                pos_hint = {"center_x": 0.5}
                            )
                            grid_layout.add_widget(file_image)
                    grid_layout.size_hint = (1, 1)
                    grid_layout.height = grid_layout.minimum_height
                    grid_layout.size_hint_y = None
                    grid_layout.bind(minimum_height = grid_layout.setter("height"))
                    self.root.ids.file_reader_content_box_layout.size_hint = (None, 1)
                    self.root.ids.file_reader_content_box_layout.bind(minimum_height = self.root.ids.file_reader_content_box_layout.setter("height"))
                    self.root.ids.file_reader_content_box_layout.size_hint_y = None
                    self.set_file_reader_floating_options_card("cbz", args[0])
            elif args[0] == "pages and focus":
                if file["file_format"] == "cbz": 
                    grid_layout = GridLayout(
                        cols = 1, # save from previous session, do same with rows (if they aren't default)?
                        rows = None,
                        size_hint = (1, 1),
                        pos_hint = {"center_x": 0.5},
                        width = self.root.ids.file_reader_content_box_layout.width
                    )
                    self.root.ids["file_reader_content_box_layout_grid_layout_focus_mode"] = grid_layout
                    self.root.ids.file_reader_content_box_layout.add_widget(grid_layout)
                    for file_item in file_content:
                        if file_item["file_format"] in self.kivy_compatible_image_files:
                            container_card = MDCard(
                                orientation = "vertical",
                                size_hint = (1, None),
                                radius = [0, 0, 0, 0],
                                md_bg_color = (0, 0, 0, 0),
                                pos_hint = {"center_x": 0.5, "top": 1},
                                height = Window.size[1]
                            )
                            image = CoreImage(io.BytesIO(file_item["file"]), ext = "jpg")
                            file_image = Image(
                                texture = CoreImage(image).texture,
                                size_hint = (1, 1),
                                pos_hint = {"center_x": 0.5}
                            )
                            container_card.add_widget(file_image)
                            grid_layout.add_widget(container_card)
                    self.set_file_reader_screen_page_focus_mode_scroll_distance()
                    grid_layout.size_hint = (1, 1)
                    grid_layout.height = grid_layout.minimum_height
                    grid_layout.size_hint_y = None
                    grid_layout.bind(minimum_height = grid_layout.setter("height"))
                    self.root.ids.file_reader_content_box_layout.size_hint = (None, 1)
                    self.root.ids.file_reader_content_box_layout.bind(minimum_height = self.root.ids.file_reader_content_box_layout.setter("height"))
                    self.root.ids.file_reader_content_box_layout.size_hint_y = None
                    self.set_file_reader_floating_options_card("cbz", args[0])
            elif args[0] == "book simulator":
                self.set_file_reader_floating_options_card(file["file_format"], args[0])
        self.currently_open_file = file

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
        elif file["file_format"] == "cbr": 
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
            try:
                if list["release_date"] == None:
                    return ""
                else:
                    return list["release_date"]
            except TypeError:
                pass
        def sort_file_format(list):
            try:
                if list["file_format"] == None:
                    return ""
                else:
                    return list["file_format"]
            except TypeError:
                    pass
        def sort_file_name(list):
            try:
                if list["file_name"] == None:
                    return ""
                else:
                    return list["file_name"]
            except TypeError:
                    pass
        def sort_author_name(list):
            try:
                if list["file_author"] == None:
                    return ""
                else:
                    return list["file_author"]
            except TypeError:
                    pass
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
        self.Folder_To_Scan_Card(self, folder_selected)
        self.list_of_files = scan_folders.scan_folders(str(folder_selected), True)
        self.add_main_menu_widgets()
        
    def full_scan(self):
        if exists("Book Worm\Book Worm\local_folders_to_scan.json"):
            file = open("Book Worm\Book Worm\local_folders_to_scan.json", "r")
            json_file_data = file.read()
            file.close()
            if json_file_data != "":
                self.list_of_files = scan_folders.scan_folders(eval(json_file_data), False)
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
        local_folders_to_scan_expansion_panel = MDExpansionPanel(
                content = LocalFoldersExpansionPanelContent(),
                panel_cls = MDExpansionPanelOneLine(
                    text = "Local Folders To Scan",
                    size_hint = (1, None)
                    )
                )   
        self.root.ids["local_folders_to_scan_expansion_panel"] = local_folders_to_scan_expansion_panel
        self.root.ids.settings_scanning_local_folders_tab_box_layout.add_widget(local_folders_to_scan_expansion_panel)
        if exists("Book Worm\Book Worm\local_folders_to_scan.json"):
            file = open("Book Worm\Book Worm\local_folders_to_scan.json", "r")
            json_file_data = file.read()
            file.close()
            if json_file_data != "":
                list_of_folders_to_scan = eval(json_file_data)
                for folder in list_of_folders_to_scan:
                    self.Folder_To_Scan_Card(self, folder)

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
        if Config.get("graphics", "window_state") == "maximized":
            window_state = "maximized"
        else:
            window_state = "visible"
        save_app_data_dictionary = {
            "main_menu_file_sort": self.root.ids.main_menu_files_widget_sort_spinner.text,
            "main_menu_file_sort_order": self.root.ids.main_menu_files_widget_order.text,
            "main_menu_file_widget_height": self.main_menu_files_widgets_height,
            "main_menu_file_widget_width": self.main_menu_files_widgets_width,
            "main_menu_file_widget_size_slider_value": self.root.ids.main_menu_file_widget_size_slider.value,
            "window_size": Window.size,
            "window_state": window_state,
            "main_menu_current_tab": self.root.ids.main_menu_tabbed_panel.current_tab.text,
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
    
    def set_audio_player_card_height(self):
        try:
            if self.kivy_music_loader == None or self.kivy_music_loader.source == None:
                for child in self.root.ids.audio_player_card.children:
                    child.opacity = 0
                animation = Animation(opacity = 0, height = 0, duration = 0)
                animation.start(self.root.ids.audio_player_card)
        except AttributeError:
            for child in self.root.ids.audio_player_card.children:
                child.opacity = 0
            animation = Animation(opacity = 0, height = 0, duration = 0)
            animation.start(self.root.ids.audio_player_card)

    def set_window_size(self, saved_app_data_dictionary):
        if Config.get("graphics", "window_state") != "maximized":
            try:
                Window.size = saved_app_data_dictionary["window_size"]
            except TypeError:
                pass

    def set_main_menu_current_tab(self, saved_app_data_dictionary):
        for tab in self.root.ids.main_menu_tabbed_panel.tab_list:
            if tab.text == saved_app_data_dictionary["main_menu_current_tab"]:
                self.root.ids.main_menu_tabbed_panel.switch_to(tab) # tab will automatically switch to files after this, for some reason
    
    def set_window_state(self, saved_app_data_dictionary):
        Config.set("graphics", "window_state", saved_app_data_dictionary["window_state"])

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
                "main_menu_file_widget_size_slider_value": 0.84,
                "window_size": (800, 800),
                "window_state": "visible",
                "main_menu_current_tab": "Files"
                }
        self.set_main_menu_widget_sizes(saved_app_data_dictionary)
        self.set_main_menu_widget_sort(saved_app_data_dictionary)
        self.set_main_menu_widget_sort_order(saved_app_data_dictionary)
        self.set_audio_player_card_height()
        self.set_window_size(saved_app_data_dictionary)
        self.set_window_state(saved_app_data_dictionary)
        self.set_main_menu_current_tab(saved_app_data_dictionary)
    
    def check_mouse_position_on_navbar(self, mouse_position):
        if self.root.ids.screen_manager.current == "Read Currently Open File Screen":
            if self.root.ids.navbar.width == 0:
        # if current screen has hide-able navbar
        # if navbar is currently hidden
                if mouse_position[0] <= self.root.ids.navbar.pos[0] + self.navbar_width_max:
                    # show nabvar
                    print("XXXX")
                # else, hide navbar

# when exactly should you hide navbar, when exactly should you show it

    def on_mouse_position_changed(self, window_object, mouse_position):
        self.check_mouse_position_on_navbar(mouse_position)

    def build(self):
        self.title = "Book Reader"
        Window.bind(on_resize = self.window_resized)
        Window.bind(on_restore = self.responsive_grid_layout)
        Window.bind(on_maximize = self.responsive_grid_layout)
        Window.bind(on_request_close = self.on_request_close)
        Window.bind(on_key_down = self.on_key_down)
        Window.bind(mouse_pos = self.on_mouse_position_changed)
        return Builder.load_string(Kivy)
    
    def on_start(self):
        self.load_last_used_settings()
        self.responsive_grid_layout()
        self.create_local_folders_to_scan_expansion_panel()
        self.local_folders_and_files_scan()
        # print(Config.get("graphics", "window_state"), Config.get("graphics", "fullscreen"))
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