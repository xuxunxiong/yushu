from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from flask import jsonify, request
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
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        if isbn_or_key == 'key':
            result = YuShuBook.search_by_key(q, page)

        # return json.dumps(result), 200, {'content-type': 'application/json'}
        return jsonify(result)
    else:
        return jsonify(form.errors)
