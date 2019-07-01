from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from flask import jsonify, request, flash, render_template

from app.view_models.book import BookViewModel, BookCollection
from . import web
import json


# 蓝图


@web.route('/book/search/')
def search():
    """

    :param q: key_word or isbn
    :param page:
    :return:  result
    """
    #
    # q = request.args['q']
    # page = request.args['page']

    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
            books.fill(yushu_book, q)
            # result = BookViewModel.package_single(result, q)
        if isbn_or_key == 'key':
            yushu_book.search_by_key(q, page)
            books.fill(yushu_book, q)

        # return json.dumps(result), 200, {'content-type': 'application/json'}

    else:
        flash('there is no result')

    return render_template('search_result.html', books=books)
    # return json.dumps(books, default=lambda obj: obj.__dict__)


@web.route('/book/<isbn>/')
def book_detail(isbn):
    pass
