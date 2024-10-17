from flask import Blueprint, render_template, request, redirect, url_for


bp = Blueprint('comparative', __name__)


@bp.route('/comparative')
def index():
    return render_template('comparative.html')
