import tempfile


import requests
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

"""
Download html document using requests. If requests resulsts errors, store it as http status 600, 
my error definition because Python run time error cannot be mapped to http statu code.
Parse all a tag and store as a link file. Remove html by using beautiful soup 4. Then wakachiwake by mecab. 

This file create following files:
    raw html
    link file
    text file
    wakachied file
"""



try:
    r = requests.get(url)
except Exception as e:
    logger.info(e)


