from . import web
from flask_login import login_required


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'my gift'
