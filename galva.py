from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Definējam datubāzes modeļus
class Tabula1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vards = db.Column(db.String(50), nullable=False)
    uzvards = db.Column(db.String(50), nullable=False)
    vecums = db.Column(db.Integer, nullable=False)

class Tabula2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    veids = db.Column(db.String(50), nullable=False)
    datums1 = db.Column(db.DateTime, default=datetime.utcnow)
    skaits = db.Column(db.Integer, nullable=False)

# Izveidojam datubāzi
db.create_all()

# Dekorācija uz uzdevuma izveidi Tabulā1
def create_entry(data):
    new_entry = Tabula1(vards=data['vards'], uzvards=data['uzvards'], vecums=data['vecums'])

    try:
        db.session.add(new_entry)
        db.session.commit()
        return 'Ieraksts pievienots veiksmīgi.'
    except:
        return 'Kaut kas nogāja greizi.'

# Dekorācija uz datu izgūšanu no Tabulas2 ar nosacījumu
def fetch_data_conditionally():
    data = Tabula2.query.filter(Tabula2.skaits > 4).all()
    return data

@app.route('/')
def index():
    data_tabula2 = fetch_data_conditionally()
    return render_template('index.html', data_tabula2=data_tabula2)

@app.route('/add', methods=['POST'])
def add():
    content = request.form['content']
    new_task = Task(content=content)

    try:
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')
    except:
        return 'Kaut kas nogāja greizi'

if __name__ == '__main__':
    app.run(debug=True)