import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bootstrap = Bootstrap(app)

#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/jobdescription.sqlite"
db = SQLAlchemy(app)



# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
# NOTATION: Table = Base.classes.table

Data_engineer = Base.classes.Data_engineer

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/")
def analysis():
    """Return the analysis page."""
    return render_template("analysis.html")

    @app.route("/")

def about():
    """Return the about page."""
    return render_template("about.html")

@app.route("/engineer")
def names():
    """Return a list of jb descriptions."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(Data_engineer).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names
    return jsonify(list(df.columns)[2:])


@app.route("/engineer/<data>")
def Data_engineer(data):
 
    sel = [
        Data_engineer.id,
        Data_engineer.jobTitle,
        Data_engineer.companyName,
        Data_engineer.location,
        Data_engineer.rating
    ]

    results = db.session.query(*sel).filter(Data_engineer.id == id).all()

    # Create a dictionary entry for each row of metadata information
    Data_eng = {}
    for result in results:
        Data_engineer ["id"] = result[0]
        Data_engineer ["jobTitle"] = result[1]
        Data_engineer ["companyName"] = result[2]
        Data_engineer ["location"] = result[3]
        Data_engineer ["rating"] = result[4]


    print(Data_engineer)
    return jsonify(Data_eng)



class CV(db.Model):
    __tablename__ = 'resumes'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(5000))

    def __repr__(self):
        return '<CV %r>' % (self.text)

@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()

# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        text = request.form["resumeText"]
        
        resume = CV(text=text)
        db.session.add(resume)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("index.html")

@app.route("/api/cv")
def resumes():
    results = db.session.query(CV.text).all()
    print(results)
    all_CVs = list(np.ravel(results))
    return jsonify(all_CVs)


if __name__ == "__main__":
    app.run()