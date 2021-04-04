from flask import Blueprint, url_for, render_template, g
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    print(g.user)
    return render_template('main/main_desktop.html')
