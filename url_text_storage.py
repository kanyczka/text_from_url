from datetime import datetime
import scraping_func as sf


class TextFromUrl():
    """
      This class allows you to grab text from websites.
      You pass a url as an argument of the class.
      After checking if the url is correct, the text will be retrieved form the site and saved as a dictionary object
      with upload_time.

    """

    def __init__(self, url):
        self.url = url
        if sf.check_url(self.url)['true']:
            self.response = sf.check_url(self.url)['response']
            self.links = sf.upload_links(self.response.text, self.url)
            self.retrieved_from_links = []
            # self.links_text_list = []
            if self.response:
                self.upload_time = datetime.now()
                text_retrieved = sf.upload_text(self.response.text)
                self.text = sf.make_one_line(text_retrieved)
                print(f'Text retrieved from - {self.url}')
            else:
                print(f'Error code: {self.response.status_code}')
        else:
            print('Bad url')
            del self.url

    def __str__(self):
        return "url: " + self.url

    def show_text(self):
        print(self.text)

    def get_links(self):
        return self.links

    def show_links(self):
        for n, link in enumerate(self.links):
            print(n, link)

    def show_text_lenght(self):
        print(f'Length of the text string: {len(self.text)}')

    def retrieve_from_links(self, number=None):

        """
        The argument of this method is the number of links you want to retrieve text from
        If none is given, the method goes through all the links
        """

        if not isinstance(number, int) or number < 0:
            raise ValueError('The number must be integer or None')
        else:
            if not number:
                number = len(self.links)
            for i in range(0, int(number)):
                if sf.check_url(self.links[i])['true']:
                    response = sf.check_url(self.links[i])['response']
                    if response:
                        text_retrieved = sf.upload_text(response.text)
                        new_text = {
                            'link': self.links[i],
                            'upload_time': datetime.now().strftime("%Y-%m-%d %H:%M"),
                            'text': sf.make_one_line(text_retrieved)
                        }
                        self.retrieved_from_links.append(new_text)
                        print(f'Text retrieved from - {self.links[i]}')
                    else:
                        print(f'{response.status_code}')
                else:
                    print('Bad url')

    def show_tex_from_links(self):
        for link in self.retrieved_from_links:
            text_length = len(link.get('text'))
            print(f"{link.get('link')}\n Text: {link.get('text')}\n Text string length: {text_length}\n"
                  f" Upload date/time: {link.get('upload_time')}")

    @property
    def all_text(self):
        text_list = [self.text]
        for el in self.retrieved_from_links:
            text_list.append(el['text'])
        return text_list


url = 'https://www.plus.pl/'
print('\n============= Class TextFromUrl(url) =========================================\n')
url_text = TextFromUrl(url)
print('\n============= Class attributes: text, url, uppload_time ======================\n')
print(url_text.text)
print(url_text.url)
print(url_text.upload_time)
print('\n============= Method: show_text() ============================================\n')
url_text.show_text()
print('\n============= Method: show_text_lenght() =====================================\n')
url_text.show_text_lenght()
print('\n============= Method: show_links() ===========================================\n')
url_text.show_links()
print('\n============= Method: retrieve_from_links() ==================================\n')
url_text.retrieve_from_links(-1)
print('\n============= Method: show_text_from_links() =================================\n')
url_text.show_tex_from_links()
print(
    '\n============= Property: all_text - list of all retrieved texts including texts from links =====================\n')
print(url_text.all_text)
print(
    '\n============ Class attribute: retrieved_from_links - list of dictionaries with link, upload time and text =====\n')
print(url_text.retrieved_from_links)

# url1 = TextFromUrl("https://onet.pl")
# url2 = TextFromUrl('https://onet.com')
# url3 = TextFromUrl('https://tvn24.pl')
#
# print(url1.show_text())
#
# print('=============')
#
# print(url1.__dict__)
# print(url2.__dict__)
# print(url3.__dict__)
#
# print('======================')
#
# info = TextStorage('Teksty info')
# info.add_new(url1, url2, url3)
# print('=============================')
# print(f'info.__dict__: {info.__dict__}')
#
# # print(info)
#
# for nr, url in enumerate(TextStorage.stored):
#     print(nr, url)
