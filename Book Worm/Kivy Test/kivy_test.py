from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'minimum_width', '700')
Config.set('graphics', 'minimum_height', '400')
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
# from kivy.core.window import Window
# Window.fullscreen = True
# Window.maximize()

# KV = '''
# <ContentNavigationDrawer>:

#     ScrollView:

#         MDList:

#             OneLineListItem:
#                 text: "Screen 1"
#                 on_press:
#                     root.screen_manager.current = "scr 1"

#             OneLineListItem:
#                 text: "Screen 2"
#                 on_press:
#                     root.screen_manager.current = "scr 2"


# Screen:

#     MDTopAppBar:
#         id: toolbar
#         pos_hint: {"top": 1}
#         elevation: 10
#         title: "Book Reader"
        

        
#     MDNavigationLayout:
#         x: toolbar.height

#         ScreenManager:
#             id: screen_manager

#             Screen:
#                 name: "scr 1"

#                 MDLabel:
#                     text: "Screen 1"
#                     halign: "center"
                
#                     Button:
#                         text: "gay"
#                         pos_hint: {"x":50}
#                         size_hint: (0.5, 0.5)
#                         on_press:
#                             root.screen_manager.current = "scr 2"

#             Screen:
#                 name: "scr 2"

#                 MDLabel:
#                     text: "Screen 2"
#                     halign: "center"

#         MDNavigationDrawer:
#             state: "close"
#             status: "closed"
#             enable_swiping: False
#             id: nav_drawer
#             scrim_color: [0, 0, 0, 0]
#             pos: 0,-60
#             close_on_click: False
#             ContentNavigationDrawer:
#                 screen_manager: screen_manager
#                 nav_drawer: nav_drawer


# '''

Kivy = '''

<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Screen 1"
                on_press:
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Screen 2"
                on_press:
                    root.screen_manager.current = "scr 2"


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

            ScrollView:
                do_scroll_x: False
                pos_hint: {"right": 1, "top": 1}
                size_hint: (None, None)
                width: root.width - 70
                height: root.height

                BoxLayout:
                    pos_hint: {"center_x": 0.5}
                    size_hint: (None, None)
                    width: root.width - 70
                    height: root.height - 35
                    orientation: 'vertical'

                    BoxLayout:
                        size_hint: (None, None)
                        orientation: 'horizontal'

                        Button:
                            text: "Files"
                            size_hint: (None, None)
                            width: 70
                            height: 70
                        
                        Button:
                            text: "Series"
                            size_hint: (None, None)
                            width: 70
                            height: 70

                        Button:
                            text: "Authors"
                            size_hint: (None, None)
                            width: 70
                            height: 70
                        
                        MDIconButton:
                            size_hint: (None, None)
                            width: 70
                            height: 70
                            color : [1.0, 1.0, 1.0, 1.0]             

                    BoxLayout:
                        orientation: 'horizontal'
                        pos_hint: {"y": 0}

                        Button:
                            text: "Sort"
                            size_hint: (None, None)
                            width: 70
                            height: 20

                        Button:
                            text: "Filter"
                            size_hint: (None, None)
                            width: 70
                            height: 20

                    MDLabel:
                        text: "Main Menu"
                        halign: "center"
                    
                    BoxLayout:
                        pos_hint: {"right": 1}
                        size_hint: (None, None)
                        width: root.width - 70
                        height: root.height - 35
                        orientation: 'vertical'

                        Button:
                            text: "Files"
                            size_hint: (None, None)
                            width: 70
                            height: 700
                        
                        Button:
                            text: "Files"
                            size_hint: (None, None)
                            width: 70
                            height: 700      

        Screen:
            name: "Read Currently Open File Screen"
            MDLabel:
                text: "Read Currently Open File Screen"
                halign: "center"
        
        Screen:
            name: "Settings Screen"

            ScrollView:
                do_scroll_x: False
                pos_hint: {"right": 1}
                size_hint: (None, None)
                width: root.width - 70
                height: root.height - 70
                
                BoxLayout:
                    pos_hint: {"right": 0}

                    size_hint: (None, None)
                    orientation: 'horizontal'                

                    Button:
                        text: "Themes & Preferences"
                        size_hint: (None, None)
                        width: 200

                    
                    Button:
                        text: "Scanning Folders"
                        size_hint: (None, None)
                        width: 200


                    Button:
                        text: "About"
                        size_hint: (None, None)
                        width: 100
                        height: 40




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


#  fix scrollview position
#  box layouts should be outside of the scrollview, similar in settings
#  setup main menu, get it to add elements for every book, add sort and filter buttons, books, series, authors, 
#  see if you can get the location of the mouse and hide the navbar in the currently reading frame and only show it if mouse is in position
#  get the box layout to change position
#  you'll have to redo the return func somehow
#  filter by file format


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class FileReaderApp(MDApp):
    def build(self):
        self.title = "Book Reader"
        return Builder.load_string(Kivy)


FileReaderApp().run()