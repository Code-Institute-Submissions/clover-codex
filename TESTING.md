# TESTING 

Validation: 

 HTML - I used [W3.orgvalidator](https://validator.w3.org/nu/) to validate my html, however because the validator can't read the jinja templating language it will come up with errors pertaining to the templating language syntax. 

 CSS - I used [W3CCSSvalidation](https://jigsaw.w3.org/css-validator) to validate my CSS. result: "Congratulations! No Error Found.".

Python - I used [PEP8validator](http://pep8online.com/) to validate my python code. result: "all right !"

Javascript - I used [Esprima](https://esprima.org/demo/validate.html) to validate my JS. result: "Code is syntactically valid."


##  User testing: 
***

As a user I would like to be able to login/logout for security purposes. My project does this as it has a login page furthermore if a user tries to click on e.g "characters" link in the nav bar they will be redirected to the login page to login.

As a user I would to be able to search for Character definitions by typing into a search bar a name or a word associated with the character card. When the user types in a word e.g "captain" it will filter the list of cards will a set of cards associated with that word or name. 

As a user I would like to be able to edit/update or delete information if it were to be incorrect or additonal info needed to be added. when you click on "full character card" on a card in the characters page you are taken to a seperate page that reveals more information on the character card if you click the edit button you are taken to a form that will display all the previous inputs moreover if you change and input e.g the name and click the "done" button then this will update the database and the card furthermore on the full characters card if you click the "delete" button this will remove the card from the app and database.   

As user I would like to be able, to create new Character cards and definitions. On the characters page when you click the "add characters" button you are taken to a form with empty inputs. When you fill in those inputs and click "done" this will create a new character card into the database. 

As a user i would like to easily navigate through the site. My site contains a simple responsive Nav bar with two links moreover on the home page and welcome page theres are call to action links that directs the user to the characters page and login page. 


## Manual testing:
*** 

 login feature: 

When testing login feature or viewing page I used these credentials to access page.

* Username : admin


* password : admin


 Login required function: 

1) When on the welcome page try to click on the "characters" link in the navbar user will be redirected to the login page. A flash message will notify the user at the bottom of the page that a login is required. 
for testing purposes the username and password is specified in the flash message.

2) Type in the wrong credentials into the form, the user will be redirected to the login page again and a flash message will notify the user that they've entered wrong credentials. 

Navigation bar : 

1) When logged in click the Nav links and see if they take you to the respective pages. 
2) When the Navigation bar is collapsed click the menu button to see if a dropdown menu is displayed.   
3)  When on characters page click on the text logo button on the far left hand siode of the nav bar and see if it takes you back to the homepage.
Welcome page : 

4) click the link in the jumbotron and see of it takes you to the login page. 

Homepage : 

1) click the link in the jumbotron and see if it takes you to the characters page. 

Characters page : 

1) Type in a character name into the search bar, click the "Search button" and see if the specifed character comes up. Type in a word associated with character description and see what characters with that specified word in there character description comes up e.g "black bulls ". 

2) type in a character name to filter out the rest of the cards and then click the "refresh button" to see if all other cards reappear. 
3) click  "add character button" to see if you are redirected to a new page with an empty form. type in some/select values into these form inputs find an image url to put in the url input. CLick "add character" check to see if youo are redirected to "character page " and also Check to see if your newly created card is displayed with the rest on the page.
4) click "edit" on the full characters card see if you are redirected to a form that displays the inputs from the selected character card. Change an input e.g the character name or age then click "done" to see if the changes take effect. 
5) On the add characters page and edit characters page click the "Back to characters page" to see if you are returned to the " characters page " 
 character. 
6) when on full character card, do this test for "edit" and "add character". Delete the following inputs : Character name, img url and character description. see if a message pops up saying "field required". Next input text into two of the listed inputs leaving one empty then try to submit form and see if a message pops up do this for each of the listed inputs. 
7) On a card in the characters page click on " full card" to see if you are taken to a full page with more information about that card. 
8) On the "Full characters page" click the "delete" button to see if hte character card is removed from the database.
9) Start at the top of the page, keep scrolling down till you see the back to top button appear. Click that button to see if it takes you to the top of the page. 

**Responsive tests** 
1) check how the app looks on various screen sizes do this through " dev tools". ( I tested the app on the screen sizes listed below.)
2) make sure theres no horzontal scrolling. 
3) Check that the back to top button still appears on smaller screen sizes. 
4) Check the text displays clearly and doesnt go off the screen. 
5) Check that the layout changes on mobile view. 
6) Check the charaters cards are in single file stacked on top of each other when in mobile view.

**Screen sizes** 

* Galaxy 5 | 360x640   
* Pixel 2  | 411 x 731
* Iphone 5/SE | 320 x 568 
* IPhone 6/7/8 | 375 x 667
* IPhone 6/7/8 plus. | 414 x 736
* IPad | 768 x 1024
* IPad pro | 1024 x 1366

**Responsive test Results:**

The app passed all the responsive tests.

##  Browser testing 
***
I tested this app on several browsers such as :
* Internet explorer | couldnt load unsupported CSS property.
* Google chrome  | Everything Good.
* Google Chrome (Mobile) | Everything Good. 
* Firefox (mobile) | Everything Good
* Samsung mobile internet | Everything Good

 

 ## Bugs/Issues found:
***

* I found when testing the search bar that it could be improved alot by adding different search inputs for example atm mine is only a "text search input" so it only searches the database for text however i think adding a catagory search would make the search bar more user friendly and efficient e.g one of the inputs on the character card is "squad" the user can select from a list of inputs, in light of this is i think adding a tick box that enables the user to select a card with this catagory would be the next step.  
* I am not able to impliment this due to time. 