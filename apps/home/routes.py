# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from itertools import count
from apps.home import blueprint
from flask import render_template, request, Flask
from flask_login import login_required
from jinja2 import TemplateNotFound
from apps.actions import DatabaseLoad
from flask.blueprints import Blueprint
from pymysql import DATE


print("did start call")




#@login_required
@blueprint.route('/Entry')
def entry():

    return render_template('home/entry.html', segment='entry')
@blueprint.route('/Index')
def index():
    return render_template('home/index.html', segment='index')
@blueprint.route('/Cover')
def cover():
    return render_template('home/cover.html', segment='cover')

@blueprint.route('/Totals Table')
def totalsTable():
    data = DatabaseLoad.getFromDbTotals()
    return render_template('home/totalsTable.html', segment='totalsTable', resultsTotals= data )
@blueprint.route('/Post Table')
def postTable():
    data = DatabaseLoad.getFromDbPosts()
    return render_template('home/postTable.html', segment='Post Table' ,resultsPosts = data)




@blueprint.route('/<template>')
#@login_required
def route_template(template):
    print("template")
    routes = [
        ("", "route1_function", "Entities"),
        ("", "route2_function", "Posts"),
    ]
    data = {}  # Use a dictionary to store data for each route separately
    count = 1

    
    EndSegment(data)
   
    
   
def EndSegment(data):
        try:
                if not template.endswith('.html'):
                    template += '.html'
        
                # Detect the current page
                segment = get_segment(request)
                if data != None:
                    return render_template("home/" + template, segment=segment, data=data)
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

