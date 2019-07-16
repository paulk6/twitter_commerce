from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__)


# initialize config variables for application
app.config.from_object(Config)

# Bootstrap requires app instance, always comes after app is declared
bootstrap = Bootstrap(app)



from app import routes
