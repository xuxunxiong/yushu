from . import web
#
#
# def limit_key_prefix():
#     isbn = request.args['isbn']
#     uid = current_user.id
#     return f"satisfy_wish/{isbn}/{uid}"
#
@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    pass
#
#
# @web.route('/satisfy/wish/<int:wid>')
# @login_required
# @limiter.limit(key_func=limit_key_prefix)
# def satisfy_wish(wid):
#     """
#         向想要这本书的人发送一封邮件
#         注意，这个接口需要做一定的频率限制
#         这接口比较适合写成一个ajax接口
#     """
#     wish = Wish.query.get_or_404(wid)
#     gift = Gift.query.filter_by(uid=current_user.id, isbn=wish.isbn).first()
#     if not gift:
#         flash('你还没有上传此书，请点击“加入到赠送清单”添加此书。添加前，请确保自己可以赠送此书')
#     else:
#         send_email(wish.user.email, '有人想送你一本书', 'email/satisify_wish', wish=wish,
#                    gift=gift)
#         flash('已向他/她发送了一封邮件，如果他/她愿意接受你的赠送，你将收到一个鱼漂')
#     return redirect(url_for('web.book_detail', isbn=wish.isbn))
#
#
# @web.route('/wish/book/<isbn>/redraw')
# @login_required
# def redraw_from_wish(isbn):
#     wish = Wish.query.filter_by(isbn=isbn).first()
#     if not wish:
#         flash('该心愿不存在，删除失败')
#     else:
#         with db.auto_commit():
#             wish.status = 0
#     return redirect(url_for('web.my_wish'))
#
