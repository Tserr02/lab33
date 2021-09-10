from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Column, Date, TEXT

app = Flask(__name__, static_url_path='/static')
app.debug = True
app.config['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Result(db.Model):
    __tablename__ = 'result'
    id = Column(Integer(), primary_key=True)
    image_path = Column(TEXT, nullable=False)
    x = Column(Integer(), nullable=False)
    y = Column(Integer(), nullable=False)
    text = Column(TEXT, nullable=False)

