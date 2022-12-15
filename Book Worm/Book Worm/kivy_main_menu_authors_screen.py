import io
import json
from kivy.uix.image import Image
from urllib.request import urlopen
from kivymd.uix.card import MDCard
from kivy.uix.button import Button as KivyButton
from kivy.core.image import Image as CoreImage

class AuthorMainMenuWidget(object):
    def __init__(self, app, files_of_author):
        author_card = MDCard(
            orientation = "vertical",
            size_hint = (None, None),
            height = app.main_menu_authors_tab_widgets_height,
            width = app.main_menu_authors_tab_widgets_width,
            radius = [0, 0, 0, 0],
            md_bg_color = (0, 0, 0, 0)
        )
        author_image = AuthorMainMenuWidget.get_author_image(files_of_author)
        if author_image != None:
            cover_image = CoreImage(io.BytesIO(author_image), ext = "jpg")
            author_image_button = KivyButton( 
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
            author_image_button.bind(size = file_cover_image.setter("size"))
            author_image_button.bind(pos = file_cover_image.setter("pos"))
            author_image_button.add_widget(file_cover_image)
        else:
            author_image_button = KivyButton(
                text = "Author Image Not Found",
                color = (0, 0, 0, 1),
                size_hint = (1, None),
                height = 50,
                # width = 300,
            )
        author_image_button.bind(on_press = lambda x: app.change_screen("Author Screen", False))
        author_image_button.bind(on_press = lambda button: self.main_menu_author_widget_pressed(button, app, files_of_author))
        author_card.add_widget(author_image_button)   
        author_button = KivyButton(
            on_press = lambda x: app.change_screen("Author Screen", False),
            text = files_of_author[0]["file_author"],
            color = (0, 0, 0, 1),
            size_hint = (1, None),
            height = 50,
            # width = 300,
        )
        author_button.bind(on_press = lambda button: self.main_menu_author_widget_pressed(button, app, files_of_author))
        author_card.add_widget(author_button)  
        app.root.ids.main_menu_authors_tab_grid_layout.add_widget(author_card)
        # when going to authro screen, should you also send in that func author image?
        
    def main_menu_author_widget_pressed(self, button, app, files_of_author):
        if button.last_touch.button == "left":
            AuthorScreen.get_author_screen_data(AuthorScreen, app, files_of_author)
        elif button.last_touch.button == "right":
            print("right mouse clicked")
            # in ky create context menu class
            # show the class
    
    def get_author_image(files_of_author):
        author = files_of_author[0]["file_author"]
        list_of_author_files = []     
        author_image = None
        for file in files_of_author:
            list_of_author_files.append(file["file_name"])
            
        # get image from somewhere

        
        # else, search comic book database, then search music database
        return author_image

class AuthorScreen():
    def openlibrary_get_correct_author_key(author, list_of_author_files):
        correct_author_key = None
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
                            return correct_author_key
                        else:
                            for file in list_of_author_files:
                                if file in list_of_author_entries:
                                    correct_author_key = author_key
                                    return correct_author_key
                        break
        except Exception as exception:
            print("Exception in load_author_screen", exception)
        return correct_author_key

    def get_author_screen_data(self, app, files_of_author):
        author = files_of_author[0]["file_author"]
        list_of_author_files = []
        
        for file in files_of_author:
            list_of_author_files.append(file["file_name"])
        # here get bio, DOD, DOB, and similar, but not photo, get wiki link get official page link, get openlibrary link and show it on screen
            # photo is already needed for the main menu tab, so take it from there
        openlibrary_author_data_dictionary = self.search_openlibrary_database(self, author, list_of_author_files)
        if openlibrary_author_data_dictionary:
            self.load_author_screen(self, app, openlibrary_author_data_dictionary)
        else:
            # search another database
            pass
            print("Dictionary is empty!")

    def search_openlibrary_database(self, author, list_of_author_files):
        correct_author_key = self.openlibrary_get_correct_author_key(author, list_of_author_files)
        openlibrary_author_data_dictionary = {}
        if correct_author_key != None:
            onpenlibrary_author = urlopen("https://openlibrary.org/authors/" + correct_author_key + ".json")
            html_bytes_onpenlibrary_author = onpenlibrary_author.read()
            string_html_onpenlibrary_author = html_bytes_onpenlibrary_author.decode("utf-8")
            json_onpenlibrary_author = json.loads(string_html_onpenlibrary_author)

            print("search_openlibrary_database(), json_onpenlibrary_author", json_onpenlibrary_author)

            if "birth_date" in json_onpenlibrary_author:
                openlibrary_author_data_dictionary["author_birth_date"] = json_onpenlibrary_author["birth_date"]
            if "death_date" in json_onpenlibrary_author:
                openlibrary_author_data_dictionary["author_death_date"] = json_onpenlibrary_author["death_date"]
                # author_age_at_death = 
            # else:
                # author_age = 
            if "bio" in json_onpenlibrary_author:
                openlibrary_author_data_dictionary["author_bio"] = json_onpenlibrary_author["bio"]


            # try:
            #     author_official_website_link = json_onpenlibrary_author["links"]
            # except Exception as exception: 
                # print("Exception in load_author_screen", exception)

            # get some links (amazon, wiki, goodreads, official website)
            # get pseudonyms, alternate anad pesonal names along with 'name'
            # get list of works 
        
        return openlibrary_author_data_dictionary

    def load_author_screen(self, app, openlibrary_author_data_dictionary):
        pass