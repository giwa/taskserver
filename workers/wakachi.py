import re
import os

import MeCab


sep = '[!-/:-@[-`{-~、◞⤴○▿゚д◟。♡٩ωو°！？（）〈〉【】『』／≦＜＼≧＞≪≫《》∀〔〕━──\n¥〜∵∴́ ❤⇒→⇔\│←↑↓┃★☆「」・♪～〓◆◇■□▽△▲●〇▼◎．”“※♥́́́]'
pat_sep = re.compile(sep)


class Wakachi:
    def __init__(self):
        pkg_dir = os.path.dirname(os.path.realpath(__file__))
        mecab_mode = 'mecabrc -u %s/mcdict/wikipedia.dic' % pkg_dir
        self._tagger = MeCab.Tagger(mecab_mode)

    def parse(self, text):
        """

        :rtype list[str]
        :param text:
        :return:
        """
        words = [word for word, word_type in self._parse2word(text) if word_type == '名詞']
        # filter for removing one charactor
        filtered_words = filter(lambda word: len(word[0]) > 1, words)
        for w in filtered_words:
            yield w

    def _clean_up_text(self, text):
        removed_sep = [re.sub(pat_sep, ' ', e) for e in text]
        return removed_sep

    def _parse2word(self, text):
        """
            Return generator of word
        """
        clean_text = "".join(self._clean_up_text(text))
        for mecab in self._tagger.parse(clean_text).splitlines():
            wakati = mecab.split("\t")
            if len(wakati) == 2:
                word = wakati[0]
                word_type = wakati[1].split(',')[0]
                yield word, word_type
