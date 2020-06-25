# coding=utf-8
from . import reglogin_view
from ..models import User, db
import hashlib
import random
from flask import render_template, redirect, request, flash, url_for
from flask_login import login_user, logout_user, login_required
from .form import LoginForm, RegisterForm, SearchForm, PersonForm
from messageboard.models import Message, db
from flask_login import current_user
import datetime


# 登录页
@reglogin_view.route('/login/', methods={'get', 'post'})
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            # 密码正确验证
            m = hashlib.md5()
            m.update((form.password.data + user.salt).encode("utf-8"))
            print
            if m.hexdigest() != user.password:
                flash('密码输入错误')
                return redirect('/login')
            login_user(user)
            flash('登录成功')
            return redirect('/')
        else:
            flash('用户或密码错误')
    return render_template('login.html', form=form)


# 注册页
@reglogin_view.route('/register/', methods={'get', 'post'})
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            # 查看用户是否存在数据库中
            user = User.query.filter_by(username=form.username.data).first()
            if user is not None:
                flash('用户名已经存在')
                return redirect('/register')
            # 用户名不存在注册
            # 密码加md5+盐
            salt = ''.join(random.sample('0123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 10))
            m = hashlib.md5()
            m.update((form.password.data + salt).encode("utf-8"))
            password = m.hexdigest()
            # 新用户提交入库
            user = User(form.username.data, password, salt)
            # 数据库提交
            db.session.add(user)
            db.session.commit()
            flash('注册成功')
            return redirect(url_for('reglogin_view.login'))

    return render_template('register.html', form=form)


# 登出页
@reglogin_view.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('你已退出登录')
    return redirect(url_for('reglogin_view.login'))


# 查询页
@reglogin_view.route('/search/', methods={'get', 'post'})
def search():
    form = SearchForm(request.form)
    if form.validate_on_submit():

        messages = Message.query.filter(
            Message.msg.like("%" + form.username.data + "%")if form.username.data is not None else "").all()
        return render_template('search.html', form=form, messages=messages)
    else:
        messages = Message.query.order_by(Message.timestamp.desc()).all()
        return render_template('search.html', form=form, messages=messages)


# 个人页
@reglogin_view.route('/person/', methods={'get', 'post'})
def person():
    form = PersonForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            messages = Message.query.filter_by(author_id=current_user.id).all()
            return render_template('person.html', form=form,messages=messages)
        else:
            flash('请登录账号后进行查询')
            redirect('/person')

    return render_template('person.html', form=form)
