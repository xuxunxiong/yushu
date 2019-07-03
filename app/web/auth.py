from app.forms.auth import RegisterForm, LoginForm
from . import web
from flask import render_template, request, redirect, url_for, flash
from app.models.user import User
from app.models.base import db
from flask_login import login_user


@web.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            # 写入身份票据cookie
            login_user(user, remember=True)
            next = request.args.get('next')
            if not next or not next.startwith('/'):
                return redirect(url_for('web.index'))
            print(next)
            return redirect(next)
        else:
            flash('请先登录或注册')
    return render_template('auth/login.html', form=form)


@web.route('/forget_password_request', methods=['POST', 'GET'])
def forget_password_request():
    pass
