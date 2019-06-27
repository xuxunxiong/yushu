from . import web
#
#
@web.route('/pending')
def pending():
    pass

#
# @web.route('/drift/<int:did>/reject')
# @login_required
# def reject_drift(did):
#     """
#         拒绝请求，只有书籍赠送者才能拒绝请求
#         注意需要验证超权
#     """
#     with db.auto_commit():
#         drift = Drift.query.filter(Gift.uid == current_user.id,
#                                    Drift.id == did).first_or_404()
#         drift.pending = PendingStatus.reject
#         # 当收到一个请求时，书籍不会处于锁定状态, 也就是说一个礼物可以收到多个请求
#         # gift = Gift.query.filter_by(id=drift.gift_id, status=1).first_or_404()
#         # gift.launched = False
#     return redirect(url_for('web.pending'))
#
#
# @web.route('/drift/<int:did>/redraw')
# @login_required
# def redraw_drift(did):
#     """
#         撤销请求，只有书籍请求者才可以撤销请求
#         注意需要验证超权
#     """
#     with db.auto_commit():
#         # requester_id = current_user.id 这个条件可以防止超权
#         # 如果不加入这个条件，那么drift_id可能被修改
#         drift = Drift.query.filter_by(
#             requester_id=current_user.id, id=did).first_or_404()
#         drift.pending = PendingStatus.redraw
#         current_user.beans += current_app.config['BEANS_EVERY_DRIFT']
#         # gift = Gift.query.filter_by(id=drift.gift_id).first_or_404()
#         # gift.launched = False
#     return redirect(url_for('web.pending'))
#
#
# @web.route('/drift/<int:did>/mailed')
# @login_required
# def mailed_drift(did):
#     """
#         确认邮寄，只有书籍赠送者才可以确认邮寄
#         注意需要验证超权
#     """
#     with db.auto_commit():
#         # requester_id = current_user.id 这个条件可以防止超权
#         drift = Drift.query.filter_by(
#             gifter_id=current_user.id, id=did).first_or_404()
#         drift.pending = PendingStatus.success
#         current_user.beans += current_app.config['BEANS_EVERY_DRIFT']
#         gift = Gift.query.filter_by(id=drift.gift_id).first_or_404()
#         gift.launched = True
#         # 不查询直接更新;这一步可以异步来操作
#         Wish.query.filter_by(isbn=drift.isbn, uid=drift.requester_id,
#                              launched=False).update({Wish.launched: True})
#     return redirect(url_for('web.pending'))
