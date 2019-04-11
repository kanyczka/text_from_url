# url_text_storage

Python scraping module for extracting text from internet sites. 

Python version: 3.7


### Prerequisites


To have the module running BeautifulSoup, Requests and lxml parser must be installed.

```
$ apt-get install python3-bs4 (for Python 3)
$ pip install requests
$ pip install lxml

```

### Description

Class <b>TexFromUrl</b> allows you to grab text from websites.
Url is an argument of the class. After checking if the url is correct, 
the text will be retrieved form the site and saved as a dictionary object 
with upload date/time.

```
url = 'https://github.com/'
url_content = TextFromUrl(url)
```
Attributes of the class:

```
url_content.text
url_content.url
url_content.upload_time
url_contetn.retrieved_from_links   # list of dictionaries with link, upload time and text

```
The class has following methods:

```
show_text()
get_links()
show_links()
show_text_lenght()
retrieve_from_links(number)
show_tex_from_links()
all_text - returns a list of all texts retrieved from url and its links
```

Method <b>retrieve_from_links</b> gets the text from all links found on the site.
The argument of this method is the number of links you want to retrieve text from.
If none is given, the method goes through all the links.
If the link is an image ('.png', '.jpg', '.jpeg', '.gif'), the link will be ignored.


```
url_text.retrieve_from_links(4)
```

#### -----------------

The module is still under construction, so it may still have some bugs :)
