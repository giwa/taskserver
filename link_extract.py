import glob
import hashlib
from urllib.parse import urlparse



from bs4 import BeautifulSoup



def read_all_uri():
    with open("/Users/ken/west/master/task_server/data/unq_uri.txt") as f:
        for uri in f:
            yield uri.strip()

def read_htmls():
    htmls = glob.glob("/Users/ken/west/master/task_server/data/html/*")
    for html in htmls:
        yield html

def hash_uri_dict():
    uris = read_all_uri()
    return dict((hashlib.md5(uri.encode()).hexdigest(), uri) for uri in uris)

def extract_href(html_file):
    hash_uri = hash_uri_dict()
    hashed_uri = html_file.split("/")[-1]
    with open(html_file) as f:
        bs = BeautifulSoup("".join(f.readlines()), "lxml")
        for link in bs.find_all('a', href=True):
            # Convert relative path to absolute path
            if not link['href'].startswith("http"):
                uri = hash_uri.get(hashed_uri, None)
                if uri is None:
                    continue
                o = urlparse(uri)
                yield o.scheme + "://" + o.netloc + "/" + link['href']
            else:
                yield link['href']

def extract_link():
    r = []
    for html in read_htmls():
        link = []
        hashed_uri = html.split("/")[-1]
        link.append(hashed_uri)
        hrefs = [hashlib.md5(href.strip().encode()).hexdigest() for href in extract_href(html)]
        if hrefs:
            link.extend(hrefs)
        r.append(link)
    with open("./data/link_rel.txt", "w") as f:
        for result in r:
            f.write(",".join(result))
            f.write("\n")

if __name__ == "__main__":
    extract_link()
