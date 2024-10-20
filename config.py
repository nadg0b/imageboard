import os


basedir = os.path.abspath(os.path.dirname(__file__))
print("1111"+basedir)

class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or\
                              "sqlite:///" + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
