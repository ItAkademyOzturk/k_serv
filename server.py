from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from api.model.signboard import Signboard

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./data/test.db' # TODO mettre env variable & update makefile
db = SQLAlchemy(app)

s = Signboard(signboard_code='board1', customer_code='customer1', author='me', signboard_status='verified', url='test.fr', deleteed=True)
db.session.add(s)
db.session.commit()

from api.controller import index
from api.model import signboard
