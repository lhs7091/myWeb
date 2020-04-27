from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '893d436cf34e7116fb0e7ee6e5f10e7d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


from myWeb import route


'''if __name__ == '__main__':
    app.run(debug=True)
'''

