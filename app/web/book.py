from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from flask import jsonify, request, flash, render_template

from app.view_models.book import BookViewModel
from . import web


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
    result = dict()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
            result = BookViewModel.package_single(result, q)
        if isbn_or_key == 'key':
            result = YuShuBook.search_by_key(q, page)
            result = BookViewModel.package_collection(result, q)

        # return json.dumps(result), 200, {'content-type': 'application/json'}

    else:
        flash('there is no result')

    return render_template('search_result.html', books=result)


@web.route('/book/<isbn>/')
def book_detail(isbn):
    pass
