from flask_bootstrap import Blueprint

auth=Blueprint('auth',__name__,'auth',url_prefix='/auth')
from . import views