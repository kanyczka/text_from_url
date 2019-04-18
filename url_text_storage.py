from datetime import datetime
import csv, os
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
                self.upload_time = datetime.now().strftime("%Y-%m-%d %H:%M")
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
        try:
            if not isinstance(number, int) or number < 0:
                raise ValueError('Not a proper number, the number must be an integer or None')
        except ValueError as e:
            print(e)
        else:
            IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.gif'}
            if not number:
                number = len(self.links)
            for i in range(0, int(number)):
                if sf.check_url(self.links[i])['true']:
                    response = sf.check_url(self.links[i])['response']
                    if response:
                        last_link_letters = str(self.links[i])[-4:]
                        if last_link_letters in IMAGE_EXTS:
                            print('The link is an image, not a text, the link was ignored')
                        else:
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
        try:
            if not self.retrieved_from_links:
                raise Exception
        except Exception as a:
            print('The link list is empty')
        else:
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


    def save_csv(self, file_name=None):
        if not file_name:
            name_num = sf.count_files() + 1
            file_name = sf.name_file(name_num)
        with open(file_name, 'w+') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['url', 'text', 'upload time'])
            csv_writer.writerow([self.url, self.text, self.upload_time])
            for el in self.retrieved_from_links:
                csv_writer.writerow([el.get('link'), el.get('text'), el.get('upload_time')])



