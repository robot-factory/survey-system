from flask import Blueprint

analysis = Blueprint(
    'analysis',
    __name__,
    template_folder='templates/analysis',
    static_folder='static/analysis',
    url_prefix='/analysis',
)


from . import main