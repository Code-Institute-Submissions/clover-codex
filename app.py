import os
from flask import (Flask, render_template, redirect, request,
                   url_for, request, session, flash)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from functools import wraps


from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'clover_codex'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')

mongo = PyMongo(app)

# login required. user has to log in before accessing other pages.
# :https://stackoverflow.com/questions/20503183/python-flask-working-with-wraps


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('login required. Hint: username = admin password = admin')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')


@app.route('/home')
@login_required
def home_page():
    return render_template('home.html')

# Enables user to log in and creates session.
# Got code from this video https://www.youtube.com/watch?v=bLA6eBGN-_0


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin'\
           or request.form['password'] != 'admin':
            error = ':  Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('logged in :)')
            return redirect(url_for('home_page'))
    return render_template('login.html', error=error)


# Enables user to logout and expires session.
# https://www.youtube.com/watch?v=BnBjhmspw4c


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('logged out :)')
    resp = app.make_response(render_template('welcome.html'))
    resp.set_cookie('logged_in', expires=0)

    return resp


@app.route('/characters')
@login_required
def characters_page():
    return render_template('characters.html',
                           characters=mongo.db.characters.find())

@login_required
@app.route('/add_characters')
def add_characters():
        return render_template('add_characters.html',
                               affinity=mongo.db.affinity.find(),
                               squad=mongo.db.squad.find(),
                               status=mongo.db.status.find(),
                               gender=mongo.db.gender.find(),
                               country=mongo.db.country.find())


@app.route('/full_card/<character_id>')
def full_page(character_id):
    the_characters = mongo.db.characters.find_one(
        {"_id": ObjectId(character_id)})

    return render_template('full_card.html', character=the_characters)


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
    the_country = mongo.db.country.find()
    return render_template('edit_character.html', character=the_character,
                           affinity=the_affinity, squad=the_squad,
                           status=the_status, gender=the_gender,
                           country=the_country)


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


@app.route("/search_results/", methods=["POST"])
def search_results():  # received help from Micheal_ci with this part of code.
    search_text = request.form.get('search_text')
    mongo.db.characters.create_index([("character_name", "text"),
                                      ("character_description", "text")])
    characters = (mongo.db.characters.find(
                  {"$text": {"$search": search_text}}).limit(10))
    return render_template("results.html", characters=characters)


@app.route('/delete_characters/<character_id>')
def delete_character(character_id):
    mongo.db.characters.remove({'_id': ObjectId(character_id)})
    return redirect(url_for('characters_page'))


if __name__ == "__main__":
    app.run(host=os.environ.get('IP' , '0.0.0.0'),
            port=int(os.environ.get('PORT', '8080' )),
            debug=True)
