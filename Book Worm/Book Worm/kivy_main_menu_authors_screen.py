from kivymd.uix.card import MDCard
from kivy.uix.button import Button as KivyButton

class AuthorMainMenuWidget():
    def __init__(self, app, author):
        author_card = MDCard(
            orientation = "vertical",
            size_hint = (None, None),
            height = app.main_menu_files_widgets_height,
            width = app.main_menu_files_widgets_width,
            radius = [0, 0, 0, 0],
            md_bg_color = (0, 0, 0, 0)
        )
        app.root.ids.main_menu_authors_grid_layout.add_widget(author_card)
        # add author image here
        author_button = KivyButton(
            on_press = lambda x: app.change_screen("Author Screen", False),
            text = author,
            color = (0, 0, 0, 1),
            size_hint = (1, None),
            height = 50,
            # width = 300,
        )
        # author_button.bind(on_press = lambda button: app.main_menu_file_widget_pressed(file, button)) # make a func that will handle loading author screen
        app.root.ids.main_menu_authors_grid_layout.add_widget(author_button)

        
        
