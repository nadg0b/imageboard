from flask import render_template
from app.admin import bp


@bp.route('/admin')
def admin():
    return "Admin page"