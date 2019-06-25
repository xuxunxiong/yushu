from app.libs.httper import Httper
from flask import current_app


class YuShuBook:
    # per_page = 15
    isbn_url = 'http://t.yushu.im/v2/book/book/isbn/{}'
    key_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = Httper.get(url)
        return result

    @classmethod
    def search_by_key(cls, key, page=1):
        url = cls.key_url.format(key, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = Httper.get(url)
        return result

    @classmethod
    def calculate_start(cls, page):
        return (page - 1) * current_app.config['PER_PAGE']
