from flask import render_template

from . import cgov_blueprint


# ------
# Routes
# ------

@cgov_blueprint.route('/')
def index():
    return render_template('cgov/index.html')
