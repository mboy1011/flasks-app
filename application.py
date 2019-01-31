import os

from flask import Flask,render_template,request,session,request,redirect,url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
@app.route("/home")
def index():
    query = db.execute("SELECT * FROM tbl_employee").fetchall()
    return render_template('index.html',query=query)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/insert", methods=['POST'])
def insert():
    fn = request.form.get("ifn")
    ln = request.form.get("iln")
    mn = request.form.get("imn")
    query = db.execute("INSERT INTO tbl_employee (f_name,l_name,m_name) VALUES (:fn, :ln, :mn)",{"fn":fn,"ln":ln,"mn":mn})
    db.commit()
    return redirect(url_for('index'))