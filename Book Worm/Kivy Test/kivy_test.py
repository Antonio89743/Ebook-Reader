from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'minimum_width', '700')
Config.set('graphics', 'minimum_height', '400')
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
# from kivy.core.window import Window
# Window.fullscreen = True
# Window.maximize()
from os.path import sep, expanduser, isdir, dirname
import sys

Kivy = '''

#:import Factory kivy.factory.Factory

<LocalFolderPopUp@Popup>

    auto_dismiss: False
    title: "Choose Folder"
    size_hint: (0.8, 0.8)
    pos_hint: {"center_x": 0.5}

    BoxLayout:
        size: root.size
        pos: root.pos
        orientation: "horizontal"

        BoxLayout:
            id: folder_chooser_box_layout_vertical
            size: root.size
            pos: root.pos
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
                        height: root.height - 70

                        BoxLayout:
                            id: box
                            pos_hint: {"top": 1}
                            size_hint: (None, None)
                            width: scroll_view.width 
                            height: self.minimum_height 
                            orientation: 'vertical'

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
                        height: root.height - 70

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

#  setup main menu, get it to add elements for every book, add sort and filter buttons, books, series, authors, 
#  see if you can get the location of the mouse and hide the navbar in the currently reading frame and only show it if mouse is in position
#  get the box layout to change position
#  redo the return func
#  filter by file format

class AddLocalFolderToScanDialog():
    '''AddLocalFolderToScanDialog'''

class LocalFoldersExpansionPanelContent(BoxLayout):
    '''LocalFoldersExpansionPanelContent'''

class FileReaderApp(MDApp):

        # add panel on the end of grid with button to remove and label that shows folder directory

    def add_folder_to_scan_folder_selected(self, folder_selected):
        print(folder_selected)

    def build(self):
        self.title = "Book Reader"
        return Builder.load_string(Kivy)
    
    def on_start(self):
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
        import os, string
        available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
        print(available_drives)
    
FileReaderApp().run()

# on navbar add a searchbar iconbutton
#   on press expand it to a full searchbar
# main menu: