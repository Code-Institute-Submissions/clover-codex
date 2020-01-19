import os
from flask  import Flask , render_template, redirect, request, url_for , request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'clover_codex'
app.config["MONGO_URI"] = os.getenv('MONGO_URI' )

mongo = PyMongo(app)

@app.route('/')

@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/characters')
def characters_page():
    return render_template('characters.html', characters=mongo.db.characters.find())


if __name__ == "__main__": 
       app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
