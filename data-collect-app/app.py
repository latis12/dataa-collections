from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/collections'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    gender = db.Column(db.String(200))
    age = db.Column(db.Integer)
    comments = db.Column(db.Text())


    def __init__(self, customer, gender, age, comments):
        self.customer = customer
        self.gender = gender
        self.age = age
        self.comments = comments


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        gender = request.form['gender']
        age = request.form['age']
        comments = request.form['comments']

        if customer == '' or gender == '' or comments == '':
            return render_template('index.html', message='Please enter required fields')

        #if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
         #   data = Feedback(customer, dealer, rating, comments)
          #  db.session.add(data)
           # db.session.commit()
        return render_template('success.html')
        #return render_template('index.html', message='You have already submitted feedback')


if __name__ == '__main__':
    app.run()