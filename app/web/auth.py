from app.forms.auth import RegisterForm
from . import web
from flask import render_template, request
from app.models.user import User
from app.models.base import db


@web.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
    return render_template('auth/register.html', form=form)


@web.route('/login')
def login():
    return render_template('auth/login.html', form={'data': {}})
