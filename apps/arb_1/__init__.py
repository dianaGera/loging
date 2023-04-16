from flask import Blueprint

blueprint = Blueprint(
    import_name=__name__,
    url_prefix='/',
    name='home_blueprint'
)
