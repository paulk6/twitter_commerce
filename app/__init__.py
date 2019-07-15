from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__)

# Bootstrap requires app instance, always comes after app is declared
bootstrap = Bootstrap(app)


from app import routes
