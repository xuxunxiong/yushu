import json

class Spider:
    def __init__(self):
        self.books = [{'author': ['阿里巴巴集团双11技术团队'], 'binding': '平装', 'category': '编程', 'id': 898,
                       'image': 'https://img3.doubanio.com/lpic/s29402674.jpg',
                       'images': {'large': 'https://img3.doubanio.com/lpic/s29402674.jpg'},
                       'isbn': '9787121309175', 'pages': '240', 'price': '79', 'pubdate': '2017-4',
                       'publisher': '电子工业出版社', 'subtitle': '',
                       'summary': '“双 11”，诞生于杭州，成长于阿里',
                       'title': '尽在双11：阿里巴巴技术演进与超越', 'translator': []}
                      ]
        self.total = 0


class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.pages = book['pages'] or ''
        self.price = book['price']
        self.summary = book['summary'] or ''
        self.image = book['image']


class BookCollection:
    def __init__(self):
        self.books = []
        self.total = 0
        self.keyword = None

    def fill(self, yushu_book, keyword='hello'):
        self.books = [BookViewModel(book) for book in yushu_book.books]
        print(json.dumps(self.books, default=lambda obj: obj.__dict__))
        self.total = yushu_book.total
        self.keyword = keyword


if __name__ == '__main__':
    yushu_book = Spider()
    print(yushu_book.books)
    book = BookCollection().fill(yushu_book)
    print(book)
