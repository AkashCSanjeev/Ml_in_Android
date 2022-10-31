from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from Resource.model import Model

#  For authentication we can use Flask-JWT (pip)

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '1234'
api=Api(app)

# @app.before_first_request
# def create_table():
#     db.create_all()

api.add_resource(Model,'/predict')
# api.add_resource(StoreList,'/stores')



if __name__ == '__main__':
    # from db import db
    # db.init_app(app)
    app.run(debug=True)
