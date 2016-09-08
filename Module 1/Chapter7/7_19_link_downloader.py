from collections import Iterable

def get_pages(links):
    if not isinstance(links, Iterable) or isinstance(
            links, (bytes, str)):
        links = [links]
    for link in links:
        #download the link with urllib
        print(link)

