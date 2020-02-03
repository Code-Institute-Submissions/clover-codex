# Milestone 3 : Black clover codex

Overview:
 
For my milestone project the goal was to Build a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain and also implememts the CRUD functionality (Create ,Read ,Update ,Delete). 
For my project i decided to create a character dictionary which contained info about characters from a type of japanese animation known as anime. I'm a big fan of anime and so the goal here is to find and share infomation about these characters and as a community add to the database. 

# UX

#### User stories :

A a user i would like to be able to login/logout.

As a user I would to be able to search for Character definitions by typing into a search bar a name or a word associated with the character card. 

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

* User testing:

* Manual testing:

* Validation:

* Issues:


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