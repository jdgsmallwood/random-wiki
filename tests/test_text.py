from random_wiki import random_wiki_text


class TestText:
    def test_format(self):
        text_pieces = [random_wiki_text.introduction, random_wiki_text.article_delivery]
        for text in text_pieces:
            assert isinstance(text, str)
