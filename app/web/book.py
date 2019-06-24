from helper import is_isbn_or_key
from yushu_book import YuShuBook
from flask import jsonify
from . import web


# 蓝图


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """

    :param q: key_word or isbn
    :param page:
    :return:  result
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    if isbn_or_key == 'key':
        result = YuShuBook.search_by_key(q)

    # return json.dumps(result), 200, {'content-type': 'application/json'}
    return jsonify(result)
