from bs4 import BeautifulSoup
import requests
import re, os


def check_url(url):
    try:
        requests.get(url)
        return {'true': True, 'response': requests.get(url)}
    except:
        return False


def upload_text(html_data):
    soup = BeautifulSoup(html_data, 'lxml')
    for s in soup(['script', 'style']):
        s.decompose()
    text = ' '.join(soup.stripped_strings)
    clean_text = re.sub("{{.*?}}", '', text)
    return clean_text



def upload_links(html_data, url):
    url_links = []
    soup = BeautifulSoup(html_data, 'lxml')
    a_tags = soup.find_all('a', attrs={'href': re.compile("^http")})
    if a_tags:
        for link in a_tags:
            url_links.append(link.get('href'))
    if url in url_links:
        url_links.remove(url)
    links_set = set(url_links)
    return list(links_set)



def make_one_line(content):
    text_list = []
    if isinstance(content, str):
        content = content.split('\n')
    if not isinstance(content, list):
        raise ValueError('Must be a string or a list of strings')
    for line in content:
        text_list.append(line.strip())
    one_line_text = ' '.join(text_list)
    return one_line_text


def count_files(dir, file_type=".txt"):
    count = 0
    for file in os.listdir(dir):
        if file.endswith(file_type):
            count += 1
    return count
