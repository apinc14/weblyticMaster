# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps.actions import DatabaseLoad
#@login_required
@blueprint.route('/entry')
def entry():

    return render_template('home/entry.html', segment='entry')
@blueprint.route('/index')
def index():
    return render_template('home/index.html', segment='index')
@blueprint.route('/cover')
def cover():
    return render_template('home/cover.html', segment='cover')
@blueprint.route('/table')
def table():
    resultsPosts, resultsTotals = DatabaseLoad.getFromDb()
    print("totals",resultsTotals)
    print("posts",resultsPosts)
    print(len(resultsPosts), "lensP",)
    print(len(resultsTotals), "lensT",)


    return render_template('home/table.html', segment='table', resultsPosts=resultsPosts, resultsTotals=resultsTotals )
@blueprint.route('/<template>')
#@login_required
def route_template(template):
    try:
        if not template.endswith('.html'):
            template += '.html'
        # Detect the current page
        segment = get_segment(request)
        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404
    except:
        return render_template('home/page-500.html'), 500
# Helper - Extract current page name from request
def get_segment(request):
    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index'
        return segment
    except:
        return None
