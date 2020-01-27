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
    return render_template('add_characters.html', affinity=mongo.db.affinity.find() , squad=mongo.db.squad.find() , status=mongo.db.status.find(), gender=mongo.db.gender.find() , country=mongo.db.country.find()  )

@app.route('/full_card/<character_id>') 
def full_page(character_id): 
    the_characters=mongo.db.characters.find_one({"_id": ObjectId(character_id)}),
    character_name: request.form.getValues('character_name')
    the_affinity = affinity = mongo.db.affinity.find()
    return render_template('full_card.html', characters=the_characters, affinity=the_affinity )


@app.route('/insert_character', methods=['POST'])
def insert_character():
    characters = mongo.db.characters
    characters.insert_one(request.form.to_dict())
    return redirect(url_for('characters_page'))


@app.route('/edit_character_card/<character_id>')
def edit_character(character_id):
    the_character = mongo.db.characters.find_one(
        {"_id": ObjectId(character_id)})
    the_affinity = mongo.db.affinity.find()
    the_squad = mongo.db.squad.find() 
    the_status = mongo.db.status.find()
    the_gender = mongo.db.gender.find()
    the_country  =mongo.db.country.find() 
    return render_template('edit_character.html', character=the_character,
                           affinity=the_affinity , squad=the_squad 
                           , status=the_status , gender=the_gender, country=the_country )


@app.route('/update_character/<character_id>', methods=["POST"])
def update_character(character_id):
    characters = mongo.db.characters
    characters.update({'_id': ObjectId(character_id)},
                      {
        'img_src': request.form.get('img_src'),
        'character_name': request.form.get('character_name'),
        'affinity_name': request.form.get('affinity_name'),
        'character_age': request.form.get('character_age'),
        'gender_name': request.form.get('gender_name'),
        'status_name': request.form.get('status_name'),
        'character_species': request.form.get('character_species'),
        'squad_name': request.form.get('squad_name'),
        'country_name': request.form.get('country_name'),
        'character_description': request.form.get('character_description'),

    })
    return redirect(url_for('characters_page'))


@app.route('/delete_characters/<character_id>')
def delete_character(character_id):
    mongo.db.characters.remove({'_id': ObjectId(character_id)})
    return redirect(url_for('characters_page'))


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
