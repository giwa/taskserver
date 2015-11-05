#! /bin/bash


# they cannot download from requirements.txt directly. Therfore, I made a script.
pip install https://github.com/celery/celery/zipball/master#egg=celery
pip install https://github.com/celery/billiard/zipball/master#egg=billiard
pip install https://github.com/celery/py-amqp/zipball/master#egg=amqp
pip install https://github.com/celery/kombu/zipball/master#egg=kombu
