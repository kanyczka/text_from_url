from url_text_storage import TextFromUrl


url = 'https://google.com'
print('\n============= Class TextFromUrl(url) =========================================\n')
url_text = TextFromUrl(url)
print()
print('\n============= Class attributes: text, url, uppload_time ======================\n')
print(url_text.text)
print(url_text.url)
print(url_text.upload_time)
print()
print('\n============= Method: show_text() ============================================\n')
url_text.show_text()
print()
print('\n============= Method: show_text_lenght() =====================================\n')
url_text.show_text_lenght()
print()
print('\n============= Method: show_links() ===========================================\n')
url_text.show_links()
print()
print('\n============= Method: retrieve_from_links() ==================================\n')
url_text.retrieve_from_links(0)
print()
print('\n============= Method: show_text_from_links() =================================\n')
url_text.show_tex_from_links()
print()
print(
    '\n============= Property: all_text - list of all retrieved texts including texts from links =====================\n')
print(url_text.all_text)
print()
print(
    '\n============ Class attribute: retrieved_from_links - list of dictionaries with link, upload time and text =====\n')
print(url_text.retrieved_from_links)
print()
print('\n============= Method: save_csv() =================================\n')
url_text.save_csv()
print()

