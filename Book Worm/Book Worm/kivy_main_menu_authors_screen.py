import json
from urllib.request import urlopen
from kivymd.uix.card import MDCard
from kivy.uix.button import Button as KivyButton

class AuthorMainMenuWidget():
    def __init__(self, app, files_of_author):
        author_card = MDCard(
            orientation = "vertical",
            size_hint = (None, None),
            height = app.main_menu_authors_tab_widgets_height,
            width = app.main_menu_authors_tab_widgets_width,
            radius = [0, 0, 0, 0],
            md_bg_color = (0, 0, 0, 0)
        )
        app.root.ids.main_menu_authors_tab_grid_layout.add_widget(author_card)
        # add author image here
        author_button = KivyButton(
            on_press = lambda x: app.change_screen("Author Screen", False),
            text = files_of_author[0]["file_author"],
            color = (0, 0, 0, 1),
            size_hint = (1, None),
            height = 50,
            # width = 300,
        )
        author_button.bind(on_press = lambda button: self.main_menu_author_widget_pressed(button, app, files_of_author))
        app.root.ids.main_menu_authors_tab_grid_layout.add_widget(author_button)
        
    def main_menu_author_widget_pressed(self, button, app, files_of_author):
        if button.last_touch.button == "left":
            AuthorScreen.load_author_screen(app, files_of_author)
        elif button.last_touch.button == "right":
            print("right mouse clicked")
            # in ky create context menu class
            # show the class

class AuthorScreen():
    def load_author_screen(app, files_of_author):
        author = files_of_author[0]["file_author"]
        list_of_author_files = []
        for file in files_of_author:
            list_of_author_files.append(file["file_name"])
        # here get bio, DOD, DOB, and similar, but not photo
            # photo is already needed for the main menu tab, so take it from there


        # first cehck book database, then comic book, then music
        try:
            search_onpenlibrary_author = urlopen("https://openlibrary.org/search/authors.json?q=" + author.replace(" ", "%20"))
            html_bytes_search_onpenlibrary_author = search_onpenlibrary_author.read()
            string_html_search_onpenlibrary_author = html_bytes_search_onpenlibrary_author.decode("utf-8")
            json_search_onpenlibrary_author = json.loads(string_html_search_onpenlibrary_author)
            if json_search_onpenlibrary_author["numFound"] >= 1:
                if json_search_onpenlibrary_author["numFound"] == 1:
                    correct_author_key = json_search_onpenlibrary_author["docs"][0]["key"]
                elif json_search_onpenlibrary_author["numFound"] > 1:
                    list_of_author_keys = []
                    for doc in json_search_onpenlibrary_author["docs"]:
                        list_of_author_keys.append(doc["key"])
                    for author_key in list_of_author_keys:
                        search_onpenlibrary_author_works = urlopen("https://openlibrary.org/authors/" + author_key + "/works.json")
                        html_bytes_search_onpenlibrary_author_works = search_onpenlibrary_author_works.read()
                        string_html_search_onpenlibrary_author_works = html_bytes_search_onpenlibrary_author_works.decode("utf-8")
                        json_search_onpenlibrary_author_works = json.loads(string_html_search_onpenlibrary_author_works)
                        list_of_author_entries = []
                        for entry in json_search_onpenlibrary_author_works["entries"]:
                            list_of_author_entries.append(entry["title"])
                        if list_of_author_files in list_of_author_entries:
                            correct_author_key = author_key
                            break
                        else:
                            for file in list_of_author_files:
                                if file in list_of_author_entries:
                                    correct_author_key = author_key
                                    break
                        break
            if correct_author_key != None:
                onpenlibrary_author = urlopen("https://openlibrary.org/authors/" + correct_author_key + ".json")
                html_bytes_onpenlibrary_author = onpenlibrary_author.read()
                string_html_onpenlibrary_author = html_bytes_onpenlibrary_author.decode("utf-8")
                json_onpenlibrary_author = json.loads(string_html_onpenlibrary_author)

                print("TT", json_onpenlibrary_author)

                # now get some actual data, like bio, and actually show it in app
                
        except Exception as exception:
            print("Exception in load_author_screen", exception)

# main menu files auther name button pressed