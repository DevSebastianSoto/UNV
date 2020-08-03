import json
from flask import Blueprint, redirect, render_template

r_base = Blueprint('r_base', __name__, static_folder='static')

@r_base.route('/')
def index():
    vp = 'videos.json'
    with open(vp, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    return render_template('views/base/index.html', videos=data)
