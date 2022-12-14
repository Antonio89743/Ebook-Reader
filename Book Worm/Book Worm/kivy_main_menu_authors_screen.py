import json
from urllib.request import urlopen
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
        author_button.bind(on_press = lambda button: self.main_menu_author_widget_pressed(button, app, author))
        app.root.ids.main_menu_authors_grid_layout.add_widget(author_button)
        
    def main_menu_author_widget_pressed(self, button, app, author):
        if button.last_touch.button == "left":
            AuthorScreen.load_author_screen(app, author)
        elif button.last_touch.button == "right":
            print("right mouse clicked")
            # in ky create context menu class
            # show the class

class AuthorScreen():

    def load_author_screen(app, author):

        # here get bio, DOD, DOB, and similar, but not photo
            # photo is already needed for the main menu tab, so take it from there


        # first cehck book database, then comic book, then music
        try:
            search_onpenlibrary_author = urlopen("https://openlibrary.org/search/authors.json?q=" + author.replace(" ", "%20"))
        except Exception:
            print(Exception)
        html_bytes_search_onpenlibrary_author = search_onpenlibrary_author.read()
        string_html_search_onpenlibrary_author = html_bytes_search_onpenlibrary_author.decode("utf-8")



        # get docs in that json, check if is empty
            # if not empty and num found is one

            # that will be the author to check
            # go to docs, take key element

        json_object = json.loads(string_html_search_onpenlibrary_author)

        if json_object["numFound"] >= 1:
            if json_object["numFound"] == 1:
                author_key = json_object["docs"][0]["key"]
                print(author_key)
            elif json_object["numFound"] > 1:
                # compare works from author on site and works from author in app
                # create a list of works created by that author
                # get key of author needed
                pass

                
        print(json_object, type(json_object))