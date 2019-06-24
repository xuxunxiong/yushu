from httper import Httper


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/book/isbn/{}'
    key_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = Httper.get(url)
        return result

    @classmethod
    def search_by_key(cls, key, count=15, start=0):
        url = cls.key_url.format(key, count, start)
        result = Httper.get(url)
        return result
