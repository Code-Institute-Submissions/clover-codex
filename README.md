# Milestone 3 : Black clover codex

Overview:
 
For my milestone project the goal was to Build a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain and also implememts the CRUD functionality (Create ,Read ,Update ,Delete). 
For my project i decided to create a character dictionary which contained info about characters from a type of japanese animation known as anime. I'm a big fan of anime and so the goal here is to find and share infomation about these characters and as a community add to the database. 

# UX

#### User stories :

As a user i would like to be able to login/logout for security purposes.

As a user I would to be able to search for Character definitions by typing into a search bar a name or a word associated with the character card . 

As a user I would like to be able to edit/update or delete information if it were to be incorrect or additonal info needed to be added. 

As user I would like to be able, to create new Character cards and definitions. 

As a user i would like to easily navigate through the site. 


#### Wireframes:

I hand drew my wireframes and linked them below:

* [Homepage/welcome-page](https://www.google.com)
* [Character-page](https://www.google.com)
*  [Full-character-card](https://www.google.com)
* [Add/Edit](https://www.google.com)
* [Login-page](https://www.google.com)


# Features

#### Existing features: 

Navigation bar

* Allows user to traverse through the two main pages. 

Text-logo 

* This will take you back to the homepage whne clicked. 

Login 

* In order to start Creating, Editing ect the user must log in first. a flash message will prompt the user if they attempt to click the characters link without logining in first.

Logout 

* The user can logout of the database by returnoing to the homepage and clicking the "logout" button.

Search bar

* The user can search for text by typing in a character name or word associated with character description. This will filter out character cards tha match the search input. 

Add character button (Create) 

* This takes user to another page which contains various inputs that allow the user to create a new character card. 

Full card button  (Read)
* This will enable user to view the full extent of the character card. 

Edit character button  (update)

* This will take user to another page and display the previous information stored in each input moreover it will update any changes made to the input values and display them into the new character cards when the "done button" is clicked. 

Delete character button (Delete)

* This will enable user to delete a character card. 

Refresh button 
* This will refresh the displayed results from a user search. 




#### Features left to implement:

Create your own account 

* I think would be a step up from what i currently have, it would make it more personal to the user. 

 Add more content such as Terminologies , timeline ect

* This isnt a user requirment but i think this would be a great additon to the app so that fans can learn/understand more about the anime.

Timestamps 

* This would be great to add to see how up to date some content is and when it was last edited. Not a requirement but i think it would make the app better. 


 Rating system
 
 * This would be good to have as on the character cards and if implemented the terminologies as it would communicate a sense of accurate data and satisfaction with that data to the community. 

* discussion forum 

* I think this would be a great feature becuase it would bring the community of people editing and creating on this app together.

# Technologies used: 

Bootstrap CDN 

* This was used to structure the page and make it responsive.  

HTML

* Used this in conjuction to flask for my templates 

CSS 
 
* This was used to create custom styles in my project. 

Javascript 

* This was used to add a back to top button. 

Fontawesome

* This was used for the social media icons located in the footer of the page. 

Google Fonts 

* This was used to style the font in my project.

Python 

* I used this to create the backend part of my app 

Mongodb 

* I used this in conjuction with flask to link my database to my app. 

Flask
* I used this framework to display my templates and flash messages from my apps.

# TESTING 

#### User testing: 

As a user I would like to be able to login/logout for security purposes. My project does this as it has a login page furthermore if a user tries to click on e.g "characters" link in the nav bar they will be redirected to the login page to login.

As a user I would to be able to search for Character definitions by typing into a search bar a name or a word associated with the character card. When the user types in a word e.g "captain" it will filter the list of cards will a set of cards associated with that word or name. 

As a user I would like to be able to edit/update or delete information if it were to be incorrect or additonal info needed to be added. when you click on "full character card" on a card in the characters page you are taken to a seperate page that reveals more information on the character card if you click the edit button you are taken to a form that will display all the previous inputs moreover if you change and input e.g the name and click the "done" button then this will update the database and the card furthermore on the full characters card if you click the "delete" button this will remove the card from the app and database.   

As user I would like to be able, to create new Character cards and definitions. On the characters page when you click the "add characters" button you are taken to a form with empty inputs. When you fill in those inputs and click "done" this will create a new character card into the database. 

As a user i would like to easily navigate through the site. My site contains a simple responsive Nav bar with two links moreover on the home page and welcome page theres are call to action links that directs the user to the characters page and login page. 


#### Manual testing: 

Login required function: 

* When on the welcome page try to click on the "characters" link in the navbar user will be redirected to the login page. A flash message will notify the user at the bottom of the page that a login is required. 
for testing purposes the username and password is specified in the flash message.

* Type in the wrong credentials into the form, the user will be redirected to the login page again and a flash message will notify the user that they've entered wrong credentials. 

Navigation bar : 

* When logged in click the Nav links and see if they take you to the respective pages. 
* When the Navigation bar is collapsed click the menu button to see if a dropdown menu is displayed.   

Welcome page : 

* click the link in the jumbotron and see of it takes you to the login page. 

Homepage : 

* click the link in the jumbotron and see if it takes you to the characters page. 

Characters page : 

* Type in a character name into the search bar, click the "Search button" and see if the specifed character comes up. Type in a word associated with character description and see what characters with that specified word in there character description comes up e.g "black bulls ". 
* type in a character name to filter out the rest of the cards and then click the "refresh button" to see if all other cards reappear. 
* click  "add character button" to see if you are redirected to a new page with an empty form. type in some/select values into these form inputs find an image url to put in the url input. CLick "add character" check to see if youo are redirected to "character page " and also Check to see if your newly created card is displayed with the rest on the page.
* click "edit" on the full characters card see if you are redirected to a form that displays the inputs from the selected character card. Change an input e.g the character name or age then click "done" to see if the changes take effect. 
* On the add characters page and edit characters page click the "Back to characters page" to see if you are returned to the " characters page " 
 character. 
* when on full character card, do this test for "edit" and "add character". Delete the following inputs : Character name, img url and character description. see if a message pops up saying "field required". Next input text into two of the listed inputs leaving one empty then try to submit form and see if a message pops up do this for each of the listed inputs. 
* On a card in the characters page click on " full card" to see if you are taken to a full page with more information about that card. 
* On the "Full characters page" click the "delete" button to see if hte character card is removed from the database.
* Start at the top of the page, keep scrolling down till you see the back to top button appear. Click that button to see if it takes you to the top of the page. 


 Validation: 

 HTML - I used [W3.orgvalidator](https://validator.w3.org/nu/) to validate my html, however because the validator can't read the jinja templating language it will come up with errors pertaining to the templating language syntax. 

 CSS - I used [W3CCSSvalidation](https://jigsaw.w3.org/css-validator) to validate my CSS "Congratulations! No Error Found.".

Python - 

```
E501	91	80	line too long (121 > 79 characters)
E501	118	80	line too long (174 > 79 characters)
```
Javascript - I used [Esprima](https://esprima.org/demo/validate.html) to validate my JS "Code is syntactically valid."


* Issues:

I found when testing the search bar that it could be improved alot by adding different search inputs for example atm mine is only a "text search input" so it only searches the database for text however i think adding a catagory search would make the search bar more user friendly and efficient e.g one of the inputs on the character card is "squad" the user can select from a list of inputs, in light of this is i think adding a tick box that enables the user to select a card with this catagory would be the next step.  


# DEPLOYMENT

I used Heroku, 

# CREDITS


#### Content : 

Images : 

* I don't own any of the images used in this project they came from google. 

Character Content: 

* I used information from  this [wiki](http://blackclover.fandom.com/wiki/) page to create the charcter cards
 
 Flash Messages:


 * I used this [Doc](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/) to help me implement Flash messages. 

Login code :

* I used this page from [Stacks-overflow](https://stackoverflow.com/questions/20503183/python-flask-working-with-wraps) to implemtent the login required feature.
* I used this video to [create the login page with view functions in flask](https://www.youtube.com/watch?v=bLA6eBGN-_0) for my app.

#### Acknowledgements : 

Anna_ci , Micheal_ci , Tim_ci :

* These tutors really helped me out in this project. Particularly creating the search bar and adding an img url to my character card.  