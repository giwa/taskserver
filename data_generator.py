#! /usr/bin/env python

# Generate data from sqlite which created by negi(sqlite storage version)
# dump the result with json format in data directory

import os
from glob import glob
import json
from multiprocessing import Process

from interop.browsing_hitstory import BrowsingHistory
from interop.http_result import HTTPResult


def get_sqlites(day=None):
    """
    Extract all record from sqlite

    :rtype str
    """
    sqlite_path = '/Users/ken/west/master/sqlite/'
    sqlite_dirs = os.listdir(sqlite_path)
    if day is not None:
        sqlite_dirs = filter(lambda x: x == day)
    for sqlite_dir in sqlite_dirs:
        sqlites = glob(os.path.join(sqlite_path, sqlite_dir, "*.sqlite"))
        for sqlite_db in sqlites:
            yield sqlite_db


def record_generator(day=None):
    """
    Convert sqlite record to HTTPResult

    :rtype HTTPResult
    """
    for sqlite_db in get_sqlites(day):
        http_results = HTTPResult(sqlite_db)
        for r in http_results.get_result():
            yield r


def filtered_main():
    with open("./data/http_record.json", 'w') as f:
        def callback(http_comm):
            f.write(http_comm.to_json())
            f.write("\n")

        browsing_history = BrowsingHistory(callback)
        for r in record_generator():
            browsing_history.add_http_result(r)


def non_filtered_main():
    with open("./data/non_filter_http_record.json", 'w') as f:
        def callback(http_comm):
            f.write(http_comm.to_json())
            f.write("\n")

        browsing_history = BrowsingHistory(callback)
        for r in record_generator():
            browsing_history.add_http_result_without_filter(r)


def count_get():
    """
    List up all record which has GET as condition
    """
    with open("./data/get_http_record.json", 'w') as f:
        for r in record_generator():
            if r.pattern == "GET":
                f.write(r.to_json())
                f.write("\n")


def get_all():
    """
    Dump all record in a file
    """
    with open("./data/get_all_record.json", 'w') as f:
        for r in record_generator():
            f.write(r.to_json())
            f.write("\n")


def get_uniq_url():
    """
    Count uqniue URL
    """
    records = []
    with open("./data/http_record.json") as f:
        for l in f:
            r = json.loads(l)
            records.append(r)

    uniq_urls = set(map(lambda x: x['url'], records))
    with open("./data/unq_uri.json", 'w') as u:
        for uri in uniq_urls:
            u.write(uri)
            u.write("\n")


if __name__ == '__main__':
    ps = list()
    ps.append(Process(target=non_filtered_main))
    ps.append(Process(target=filtered_main))
    ps.append(Process(target=get_all))
    ps.append(Process(target=count_get))
    for p in ps:
        p.start()

    for p in ps:
        p.join()

    get_uniq_url()
