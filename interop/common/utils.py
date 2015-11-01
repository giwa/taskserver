import json
from datetime import datetime, timedelta, date
from itertools import tee


datetime_str_format = "%Y-%m-%d %H:%M:%S"


def parse_timestamp(timestamp):
    """
        Parse timestamp
        >>> parse_timestamp('2015-4-30 18:59:34')
        datetime.datetime(2015, 4, 30, 18, 59, 34)
    """
    return datetime.strptime(timestamp, datetime_str_format)


def round_datetime_by_minute(dt):
    rounded_dt = dt - timedelta(minutes=dt.minute % 10,
                                seconds=dt.second,
                                microseconds=dt.microsecond)
    return rounded_dt


def pairwise(iterable):
    """
        s -> (s0, s1), (s1, s2), ...
    """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime(datetime_str_format)
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
