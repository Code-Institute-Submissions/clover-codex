import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'clover_codex'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/characters')
def characters_page():
    return render_template('characters.html', characters=mongo.db.characters.find())


@app.route('/add_characters')
def add_characters():
    return render_template('add_characters.html', affinity=mongo.db.affinity.find())

@app.route('/full_character_card/<character_id>')
def full_character_page(character_id):
    the_characters=mongo.db.characters.find_one({"_id": ObjectId(character_id)}),
    character_name: request.form.getValues('character_name')
    the_affinity=affinity=mongo.db.affinity.find()
    
    return render_template('full_character_card.html', characters=the_characters , affinity=the_affinity)

@app.route('/insert_character', methods=['POST'])
def insert_character():
    characters = mongo.db.characters
    characters.insert_one(request.form.to_dict())
    return redirect(url_for('characters_page')) 

@app.route('/edit_character_card/<character_id>')
def edit_character(character_id):
    the_character = mongo.db.characters.find_one({"_id": ObjectId(character_id)})
    the_affinity = mongo.db.affinity.find()
    return render_template('edit_character.html', character=the_character,
                           affinity=the_affinity)


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
