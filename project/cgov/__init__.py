from flask import Blueprint


cgov_blueprint = Blueprint('cgov', __name__, template_folder='templates')

from . import routes # noqa
