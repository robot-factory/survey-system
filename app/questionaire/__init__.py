from flask import Blueprint


questionaire_blueprint = Blueprint(
    'questionaire',
    __name__,
    template_folder='templates/questionaire',
    static_folder='static/questionaire',
    url_prefix='/questionaire',
)

from . import view
