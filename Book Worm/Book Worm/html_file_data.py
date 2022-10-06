from html.parser import HTMLParser

class HTMLFilter(HTMLParser):
    text = ""
    def handle_data(self, data):
        self.text += data

def get_html_text(html_string):
    html_filter = HTMLFilter()
    html_filter.feed(html_string)
    return html_filter.text