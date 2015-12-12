import requests
import hashlib
import time
import os
from multiprocessing import Pool
import json

DATA_DIR = "/Users/ken/west/master/task_server/data"

def download_and_save_html(url):
    hashed_url = hashlib.md5(url.encode()).hexdigest()
    file_path = DATA_DIR + "/html/" + hashed_url
    if os.path.isfile(file_path):
        return

    r = None
    try:
        r = requests.get(url.strip())
    except Exception as e:
        pass
    if r:
        if r.status_code< 400:
            with open(file_path, "w") as f:
                f.write(r.text)

def html_download():
    pool = Pool(8)
    with open(DATA_DIR + "/unq_uri.txt") as f:
        pool.map(download_and_save_html, f.readlines())


def split_data_per_day():
    http_records = []
    with open(DATA_DIR + "/http_record.json") as f:
        for l in f:
            http_records.append(json.loads(l))




if __name__ == "__main__":
    html_download()
