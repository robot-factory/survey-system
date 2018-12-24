from ..utils import logger
from . import analysis
from flask import (
    request,
    render_template,
    url_for,
    jsonify,
    current_app,
    session,
    redirect,
    make_response,
)
from ..models import qadb
from hashlib import sha1
import json

@analysis.route('/')
def index():
    return render_template('analysis/analysis.html')