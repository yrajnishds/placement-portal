from flask import Blueprint


company = Blueprint('company', __name__)


from app.company import routes  # noqa: F401, E402