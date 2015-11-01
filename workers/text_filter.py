#! encoding=utf-8

import re
import codecs
import sys
import os

if sys.version_info >= (3, 0):
    unicode = str


def is_japanese(text):
    """
    Return True if text is Japanese

    >>> is_japanese(u"daf")
    False
    """
    m = re.match(u'[ぁ-んァ-ヴ一-龠]', text)
    if m:
        return True
    else:
        return False


def is_english(text):
    """
    Return True if text is English

    >>> TextFilter.english_filter(u"adcg")
    True
    >>> TextFilter.english_filter(u"ほがおｐが")
    False
    """
    m = re.match(u'[a-zA-z]', text)
    if m:
        return True
    else:
        return False

class TextFilter(object):

    def __init__(self):
        pkg_dir = os.path.dirname(os.path.realpath(__file__))
        stopword_dir = "%s/stopword" % pkg_dir
        self._html_tags = list(self._read_stoplist("%s/html.stop" % stopword_dir))
        self._css_tags = list(self._read_stoplist("%s/css.stop" % stopword_dir))
        self._niconico_stop = list(self._read_stoplist("%s/niconico.stop" % stopword_dir))
        self._japanese_stop = list(self._read_stoplist("%s/japanese.stop" % stopword_dir))
        self._english_stop = list(self._read_stoplist("%s/english.stop" % stopword_dir))

    def _read_stoplist(self, filename):
        with codecs.open(filename, "r", "utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    if line[0] == u"#":
                        continue
                yield line

    def html_filter(self, text):
        if unicode(text) in self._html_tags:
            return True
        else:
            return False

    def css_filter(self, text):
        if unicode(text) in self._css_tags:
            return True
        else:
            return False

    def niconico_filter(self, text):
        if unicode(text) in self._niconico_stop:
            return True
        else:
            return False

    def japanese_stop_filter(self, text):
        if unicode(text) in self._japanese_stop:
            return True
        else:
            return False

    def english_stop_filter(self, text):
        if unicode(text) in self._english_stop:
            return True
        else:
            return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
