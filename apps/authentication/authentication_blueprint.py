# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from flask_login import (
    current_user,
    login_user,
    logout_user
)
from apps import login_manager
from apps.dbUserModels import dbPerform, dbActionInsertUser, dbActionRetreiveUser
from apps.authentication import blueprint
from apps.home import blueprint as home_blueprint
from apps.authentication.forms import LoginForm, CreateAccountForm
from apps.authentication.models import Users
from flask import Blueprint, redirect, url_for, make_response, g, render_template, request, url_for
from apps.authentication.util import verify_pass

@blueprint.before_request
def set_security_headers():
    g.security_response = make_response()
    g.security_response.headers['X-Frame-Options'] = 'DENY'
    g.security_response.headers['X-Content-Type-Options'] = 'nosniff'
    g.security_response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    g.security_response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self'; frame-src 'none'"
@blueprint.route('/')
def route_default():  
    return redirect(url_for('home_blueprint.cover'))
@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:
        # read form data
        username = request.form['username']
        password = request.form['password']
        # Locate user
        username, password, billingDate, isPremium  = dbPerform(dbActionRetreiveUser(username, password,'2023-07-23', True  ), True)
        #name, password, email, billingDate, isPremium
        # Check the password
        if user and verify_pass(password, user.password):
            login_user(user)
            return redirect(url_for('authentication_blueprint.route_default'))
        # Something (user or pass) is not ok
        return render_template('accounts/login.html',
                               msg='Wrong user or password',
                               form=login_form)
    if not current_user.is_authenticated:
        return render_template('accounts/login.html',
                               form=login_form)
    return redirect(url_for('home_blueprint.route_default'))
@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:
        username = request.form['username']
        email = request.form['email']
        # Check usename exists
        user = Users.query.filter_by(username=username).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Username already registered',
                                   success=False,
                                   form=create_account_form)
        # Check email exists
        user = Users.query.filter_by(email=email).first()
        if user:
            return render_template('accounts/register.html',
                                   msg='Email already registered',
                                   success=False,
                                   form=create_account_form)
        # else we can create the user
        user = Users(**request.form)
        dbPerform(dbActionInsertUser('users',username, email, 0), False)
        #tableName, db, name, password, email, billingDate, isPremium
        # Delete user from session
        logout_user()
        return render_template('accounts/register.html',
                               msg='User created successfully.',
                               success=True,
                               form=create_account_form)
    else:
        return render_template('accounts/register.html', form=create_account_form)
@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('authentication_blueprint.login'))
# Errors
@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('home/page-403.html'), 403
@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403
@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404
@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500
