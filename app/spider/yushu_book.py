from app.libs.httper import Httper
from flask import current_app


class YuShuBook:
    per_page = 15
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    key_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = Httper.get(url)
        self.__fill_single(result)

    def __fill_single(self, result):
        self.total = 1
        self.books.append(result)

    def search_by_key(self, key, page=1):
        url = self.key_url.format(key, self.per_page, (page - 1) * self.per_page)
        result = Httper.get(url)
        self.__fill_collection(result)

    def __fill_collection(self, result):
        self.total = result['total']
        self.books = result['books']

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
