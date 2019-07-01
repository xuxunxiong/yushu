class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.pages = book['pages'] or ''
        self.price = book['price']
        self.summary = book['summary'] or ''
        self.image = book['image']
        self.isbn = book['isbn']


class BookCollection:
    def __init__(self):
        self.books = []
        self.total = 0
        self.keyword = None

    def fill(self, yushu_book, keyword):
        self.books = [BookViewModel(book) for book in yushu_book.books]
        self.total = yushu_book.total
        self.keyword = keyword


class _BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'book': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['book'] = cls._cut_book_data(data)
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls._cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def _cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'author': '、'.join(data['author']),
            'pages': data['pages'] or '',
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']

        }
        return book
