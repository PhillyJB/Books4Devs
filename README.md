# Books4Devs
Books4Devs is an online platform that allows for the recommendation and review of IT related (in particular programming/development) books. Users are able to see the books that have been posted by other users; these posted books are have a front cover image, description, rating and comments from the person who posted it and also a link to an external site for purchasing of the book. In addition, users are able to post their own book suggestions, update their book suggestions or even delete only their own book suggestions

## USER EXPERIENCE

**PLEASE NOTE: These User Experience scenarios are what were used for the testing of the site features so please refer to them for testing outcome**

**Please Note – Regarding Side Nave bar:**
In all the user scenarios, for smaller devices and smaller screens the nav items a condensed into a hamburger icon which when clicked on brings up the ‘side-nav’ bar for the user to make their selections.

#### USER SCENARIOS

* **User A is looking for a book**
    * A first time user lands on the [homepage](http://books-4-devs.herokuapp.com/) and is greeted with the website introduction passage and asked to Log in or Register if they want to add their own book reviews (Login and register at top in navbar as well).

    Below that is a search bar section which allows a use to search for a book via the name of it or by the author(s) names. So if user knows the name of the book or authors name they could type this into the search box.

    User A could just scroll down on the all books section of the home page and scroll though the lists of books available. Each book’s more detailed information is available by clicking on the plus icon floating between the image and the book information. Clicking on the plus icon takes the user to the book’s personal page.

* **User B wants to register in order to add reviews of their own**
    * While on the homepage, user B can click on the ‘Register’ in the navbar or the ‘Register’ link in the introductory text. Which then takes them onto the Register page which displays the register card with the username and password inputs.

    User B can then create a username and password using the placeholder text as a guidance on the restrictions allowed. If username is not in use then the user account is created and user is logged in and shown a flash message saying ‘registration successful!’ and brought back on to the home page with all the books but this time the nav items available are ‘All Book, My Books, Add a Book and Log Out.’

    If User B goes into the ‘My Books’ section they are shown a text that they currently have no books in their profile and to click on the ‘add a book’ button in order to add their book.

    If Username already exists then the user can try another name. If they remembered they are already registered then they can go to the Log In page via the button at the bottom of the register panel.

* **User C is already registered and so logs in with authentication.**
    * While on the homepage, user C can click on the ‘Log In’ item in the navbar or the ‘LogIn’ link in the introductory text. Which then takes them onto the ‘Log In’ page which displays the Log In panel with the username and password inputs fields.

    If the User attempts to log in and is successful then they get a flash message saying ‘Log In Successful’ and they are brought onto their ‘My Books’ page which is their profile of all their books they have added (note: this is different to a new user who has just registered as a new user is taken to the homepage as they will not have any books in their profile). From here the user is able to view their book and edit/delete or add a books.

* **User D wants to post their own book (Add a Book)**
    * Once user is logged into their account they can add/post a book review using either the ‘Add a Book’ nav item at the top or while in their profile in the ‘My Books’ section they can click on the Add a Book button. User D is then presented with an ‘Add Book’ Form which has all the various fields required to complete adding a valid book review. All fields are mandatory and have to be done as directed. On completion User D clicks the add book button at the bottom of the form which if filled out correctly gives the user a flash message to say book has been successfully added. This book card is then visible on User Ds all books page as well as in the ‘My Books’ section which is where they are returned to on completing the book addition.

* **User E wants to delete a book they have posted**
    * User E can see a delete button only on books they have added. Even in the all books sections, the books that have been added by User E have the delete button on them as well as the list of books in their ‘My Books’ section. On clicking this delete button the user is shown a confirm alert box done using JavaScript which confirms if the user is sure they want to delete this book. On clicking OK the book is deleted and a flash message is given confirming successful deletion however on clicking cancel the user is returned to the page they were on with no action.

* **User F wants to amend/update a book they have made.**
    * Like User E in the deletion action, User F is able to do this via the list of books in All Books where only books they have added will have the Edit button on it. Or also via there My Books section which will show only their books. Clicking on the Edit Button takes the user to Edit Book which is prefilled with all the books current information from the previous posting. User F is then able to manually go to each field and amend information as they so please. Then at the bottom of the form the user can click the cancel button which takes them back to their ‘my books’ section and they will get a flash message that book was successfully updated even if they did not make any changes. On clicking ‘confirm edit’ they are returned to the My Books page with the same flash message book successfully updated.

* **User G wants to get a book they have an interest in**
    * User G likes the review they have read on a particular book and so click on the ‘Get this Book’ button. This opens a new tab for the user which is the purchasing site of the book e.g. amazon. The user remains having the page for their Books4Devs site open so able to continue browsing.


## FEATURES
### Existing Features

#### Site Navigation

 On top of screen there is the fixed Nav Bar which is always visible on scrolling down the page:

* Large Screens
    * When not Logged In - shows to left Book4 Devs Logo which is clickable  and on clicking returns you to home page on all pages, then to the right the nav icons ‘All Books’, ‘Log In’, ‘Register’
    * When logged In  - Books4Devs Logo  to the left and ‘All Books’, ‘My Books’, ‘Add a Book’, ‘Log Out’

*  Screens sizes 992px or less
    * Books4Devs Logo goes centre of screen
    * Other Nav Icons go into a 3 bar “hamburger” icon to the left of screen which on clicking brings up the side-nav with the same options as the large screens details above.

#### Not Logged In
* User can views all the books on the homepage under all books and is free to scroll through all of them
* User can expand each book by clicking the ‘plus’ icon which will take them to the more details page of the book
* User can click on the ‘get this book’ icon to take them to an external site link where they can buy the book – this opens the page for the external site in a new tab thus keeping the user on the Books4Devs site.
* Search
    * Users can use the search feature to filter books by book Name or particular part of the book name or even Author name.
    * Clear search – clears the current search criteria and takes user back to seeing all the books in ‘All books’.
* Register
    * New Users are able to register and create an account via entering a valid username and password
* Log In
    * Users are able to Log In to their account using a previously created username and password.

#### Logged In Users
* Add a Book
    * User can add a book(s) using the add book nav item or while in their ‘my books’ section can click on the Add a Book button which take them to the same add a book form. User fills the form out as directed which creates the new book entry and if done correct creates the new book
* Edit a Book
    * User can only update a book they have added. Edit makes changes to the posted book information and this is then saved to the database.
* Delete a Book
    * User is able to delete only a book(s) they have created. Once deleted the book is deleted from the database permanently.

#### Footer Section
User is able to go see the Social Media links of Books4Devs (Facebook, Twitter & Pinterest) – currently due to not having any social media accounts set up, these icons only take the user to the homepages these platforms


### Future Features
#### Wider Search Filter
User can find books in a wider range of categories and not just by name and author search. For example, categorise books on specific languages (python, C, JavaScript, C++, C# etc.). Another good search category will be other’s usernames. Users may like a particular user’s reviews and recommendations and so will be able to search for this user by username and be able to see only posts from this user.

#### A user wants to leave a review/comment on a book they did not post
Users will be able to review/comment on a book added by another user. The feature will also allow users to string comment on another users review if they do not fully agree with certain aspects of that review however this would have to have strict rules to prevent any unclean verbal exchanges however debates on a book are encouraged.

#### Users will be able to review/comment on a book added by another user 
The feature will also allow users to string comment on another users review if they do not fully agree with certain aspects of that review however this would have to have strict rules to prevent any unclean verbal exchanges however debates on a book are encouraged.

#### Average rating system for books
Add a feature where the books rating is based on not just the person that added it to the books list but an average of all people who have reviewed the book and given it a rating.


#### Prevent Reposting of the same book
Make it so that users cannot post a book that someone else has already posted. This will have to be added in line with users being able to add a review and rating on any book.

#### A user wants to delete their own account
Add this option so that if a user wants to remove their account they can do and so have their credentials taken off the database.

#### Increase User account profile
User accounts have more information rather than just the username name password. The users profile will show how many postings they have made and the average ratings they give books. Users will be able to share their line of work in this enhanced user profile so as to appear more credible on their reviews in a certain subject matter.

#### A user wants to make contact with a query or make a complaint
A contact us section will be created that allows users to post a query or even make a complaint report what they deem harmful or unjust comments or reviews from other users.

#### Affiliate Links
Have affiliate links for the site for when a user goes on to purchase a book through the site, Books4Devs makes money from it.

#### Social Media Platform
Social media accounts for Books4Devs will be added which will allow for users to follow and network better with Books4Devs on several platforms.

#### Improve Logo
Take the time to design and execute a beautiful standout logo for the site. At the moment it is just the simple wording of the site name.

## TECHNOLOGIES USED
### Languages
* HTML5
* CSS3
* JavaScript
* Python

### Frameworks and Libraries
* [Flask](https://flask.palletsprojects.com/en/2.0.x) - Python
* [JQuery](http://code.jquery.com) - Javascript
* [Materialize](https://materializecss.com) - HTML and CSS and JS

### Database Management System
* [MongoDB](https://www.mongodb.com) - Non SQL database


## TESTING
### Testing Scenarios
**The User scenarios under User Experience above were used to describe the testing approach implemented and below are the bug fixes that caused the main problems.**

### Bug Fixes
* **1 - Problem**
    * A persistent problem I was having was that my
data from mongodb was not rendering onto the template. The error in terminal whenever I try to run my app with `python3 app.py` was:

```
from bson.errors import InvalidId
ModuleNotFoundError: No module named 'bson.errors'

```
* **1 - Solution**
    * I initially tried to install bson using pip3 and this did install a bson package to my environment however on still running my app the above error was still showing up. So I uninstalled the bson package as to not have unnecessary packages. Instead I then had to install, using pip3, pymongo on top of the Flask-pymongo I had already installed. This fixed the issue as when I now run my app the bson method was now working and no error was present. In conclusion it seems the Flask-pymongo version of pymongo is not properly associated with the bson module for some reason.

* **2 - Problem**
    * rendering only the books the user has added in their ‘My Books’ section and if no book added by them then to just show a message saying “no books currently in your profile”
* **2 - Solution**
    * It took a while to get my head around the best way to solve this issue. On several attempts what was happening is that on a user ‘My Books’ section I was getting all the books from the site when I would try to iterate through the list of books while using a if session[user] “if statement”, I was getting  Flask errors when I tried to run my app. The solution to this problem layed in the logic of my model and how the information coming back from the model was being filtered. I altered the get information coming back from my database collection to only return information on the session[“user”] who could be found on the database by the “added_by” key on each book. This meant that in the ‘My Books’ section a user will only be able to see the books they added as this key matched the session[“user”]:

    ```
        if session["user"]:
        developer_books = list(mongo.db.developerBooks.find(
            {"added_by": session["user"]}))
        return render_template(
            "profile.html", developer_books=developer_books, username=username)
    ```
    As the code above shows, the find() method for the mongo.db is only looking the  “added_by key”

* **3 - Problem**
    * problem highlighting the active page link in the nav bar using the flask template.
Initially used an if statement in side each <li> element but for my profile page (My Books page) this was not working as the profile page takes another parameter which is the actual user. For some reason despite trying all different ways of entering the username so that the jinja template could read it depending on the user it would just not work. It followed this format:

    ```
      {% if request.path == '/profile/' %} class="active"{% endif %}  
    ```
    This jinja if else statement worked to highlight all active pages except the profile page one and I eneded up trying to add several different options in front of the ‘profile/’ bit. Like “session.user, session[user], username, <username>, <session.user>.” these all failed. I then tried to see if I typed in the username manually in front of the ‘profile/’ which I did with the user account I created and it worked as it matched the required if statement. So this definitely confirmed that I needed another parameter. 

* **3 - Solution**
    * In the end I gave up on the if statement using jinja as I had stumbled across another method on stack overflow. I found a link through the data-centric slack group which led me to a [stack overflow](https://stackoverflow.com/questions/55895502/dynamically-setting-active-class-with-flask-and-jinja2/55895621#55895621) solution. The idea  used is on the base.html  above the  **li** links to be highlighted to set the following variable (please note I donot think it realle matters where you this in the base.html:

    ```
    {% set active_page = active_page|default('index') %}
    ```
    Or even as if you do not want a default page:

    ```
    {% set active_page = active_page %}
    ```
    Then at the top of each template you put the following jinja tag:

    ```
    {% set active_page = "index" %}
    ```
    With “index” replaced by which ever template route/function u want active. Then in each **li** tags in the base.html we put:

    ```
    class="{{ 'active' if active_page == 'index' }}"
    ```
    This solved the issue the issue perfectly. I had seen a similar answer in the Flask documentation but I found this was not very clear and so could not implement correctly. However seeing it explained clearer in stackoverflow really helped
* **4 - Problem**
    * getting book cards to fully align in  a neat centre on all screen sizes. Remains slightly offset from the content like the search bar and the headings above them. They seem to have an extra bit of margin/padding to the right which cannot be made smaller.
* **4 - Solution**
    * after trying several methods and suggestions. I decided to revisit all the CSS I had made and inspect the DevTools a bit closer in the browser. Had tried several solutions for this and look at several resources to try fix.  It turned out I had some redundant code I wrote earlier on in the development process that was adding some extra margin (of 30px) to the right of the book card **div** tags. I removed this redundant code and just relied on the materialize grid system which placed 3 cards in a line on large screen sizes, two on medium and one on small screens. I also used display 
    flex and justify content to have the columns centred in rows and well as columns on small screens

    ```
    <div class="row book-section-row">
    {% for book in developer_books %}
    <!--Each Individual Card-->
    <div class="col s12 m6 l4 colum-for-cards">
    ```
    CSS for larger screens:

    ```
    .book-section-row {
        display: flex;
        flex-wrap: wrap;
        flex-direction: row;
        justify-content: center;
    }
    ```
    CSS for smaller screens less than 768px:

    ```
        @media (max-width: 767.98px) {
        .book-section-row {
        display: flex;
        flex-wrap: wrap;
        flex-direction: column;
        justify-content: center;
        text-align: center;
    }

    ```
    Also then ha to remove alot of redundant CSS which was there from when tried to resolvethe issue to refactorthe CSS code
* **5 - Problem**
    * registration entry format was allowing any type of entry into the fields with disallowed symbols as well. This was meaning users could register a username and password with any symbols from the keyboard.
* **5 - Solution**
    * – I thought I had entered my “pattern” attribute information correctly but on checking the [w3cschools](https://www.w3schools.com/tags/att_input_pattern.asp) guidance on this I notice the format I had put the entry in would not allow for the system to recognise that the entry items were incorrect format. The Correct format is:

    ```
    pattern="^[a-zA-Z0-9]{5,15}$"
    ```
    which will allow only letters and numbers between 5 to 15 characters. I had written it as which shows that the numbers should be put inside the curly brackets.

    ```
    pattern="^[a-zA-Z0-9]{ }5,15$"
    ```

### Validation of Code

* HTML Code - [W3C Validator](https://validator.w3.org/)
    * All HTML validation checks came back with no errors apart from the reoccurring “bad Value” error which was every time I used the jinja syntax to input code where the html validator could not recognise this. It is ok to ignore this as all the code base works and serves its function.
    * The only other noticeable error was with the input type which I had as a number and the validator was recognising as not allowed a ‘maxlength’ attribute for this type as shown below. However this type input is working just fine and not causing any bugs and getting and posting the rating value to the database absolutely fine so I will ignore it. The error said :


    > Attribute maxlength is only allowed when the input type 
    >is email, password, search, tel, text, or url.
    >From line 57, column 25; to line 59, column 37

And the code section is as follows:

```
<input type="number" name="rating" class="form-control" id="rating" min="1" max="10"↩ maxlength="2" value="{{ book.rating }}" placeholder="only enter a number from 1 to 10"↩ required>
```

* CSS Code  - [W3C](https://jigsaw.w3.org/css-validator/)
    * No errors found with the style.css
* JavaScript Code- [jshint](https://jshint.com/)
    * No errors found with the script.js
* Python Code - [PEP8online](http://pep8online.com/)
    * Returned an "all right" message on check.
#### Lighthouse Site Check – within google DevTools
On carrying out a lighthouse check on the website, It generated a very informative report for me on the performance of the site which it gave it scored that were all above 70/100 with the performance itself at 87. These could be improved. For the current use of the site its performance is fine and I will look at improving its performance based on the suggestions at a later time. This report is available in the github repository of the site in the static files folder

## DEPLOYMENT
### Project Development
This project was all developed using the GitPod IDE with regular commits being to git and pushed up to the github repository for saving.

#### Work on a the app in Gitpod:
1. Be sure to have a GiHub account set up  
2. Ideally use a Chrome Browser
3. Install the Gitpod browser extensions for chrome
4. Restart the browser after installation
5. Log in into Gitpod with account details
6. Follow this link to [Books4Devs repository](https://github.com/PhillyJB/milestone-project3-books4devs)
7. Go to the repository and you should see a green Gitpod button in the top right corner so click on it. This will start a new workspace with the code to allow you to work locally

#### Work on the app within a local IDE like Pycharm or Visual Code:
1. Under the repository name on GitHub you have the option to click on 'Go to file' and select a specific file in there by doing a search or click the 'Code' Icon which should then have a drop down menu and from there you can clone or download a zip of the files or 'Open with Github Desktop'
2. You can clone the repository which would mean copying the clone URL from the clone HTTPS section:

> https://github.com/PhillyJB/milestone-project3-books4devs.git
3. 4-	In your IDE open the terminal and in a directory to where the cloned directory of the project will go type in the terminal:

```
git clone https://github.com/PhillyJB/milestone-project3-books4devs.git

```
4. After pressing enter your local clone should be created ready for you to work on.

### DEPLOYMENT TO HEROKU
Deployment of the active site is done via [heroku](https://www.heroku.com/) and the following steps were taken:

1. To begin with we need to create files that Heroku needs to run the app and so the applications and dependencies required to run the app.
2. create a requirements.txt file using the command in your CLI:

 ```
 pip3 freeze --local > requirements.txt
 
 ```
This lists all the installed dependencies that are needed to run the app and lists them in the txt file.

3. We then create a **Procfile** which is what Heroku looks for to know which file runs the app and how to run it. We create this by using the following command in your CLI:

```
echo web: python app.py > Procfile
```

4. This thus puts the information `web: python app.py` into the Profile. So Heroku knows app.py runs the app. Note that the Procfile has no file extensions. Remember to then ‘git commit’ and ‘git push’ these files to github.

5. On the Heroku website you should have already created an account following the ‘sign up’ directions.
6. On the above tab, we click on ‘New’ Button, then select ‘create new app’
7. Give the app a name – try sticking to using a dashes  instead of spaces and lowercase letters
8. Select Region closest to you (Europe for us) then click create app
9. Select deployment method as  GitHub (other options are heroku CLI or Container but we use the GitHub option.
10. Select you Git Hub name and the repository name in your repositories for the app
11. Once it finds the repo click to connect to this app
12. **NOTE** – do not yet click ‘Enable automatic Deploys’ until we complete the next steps
13. Click on **‘settings’** tab at the top for your app
14. Then click on **‘reveal config Vars’** – which stands for configuration variables
15. We use this section to securely tell Heroku which variables are required so fill in the fields as follows:

KEY | VALUE
----|------
IP	|				0.0.0.0
MONGO_DBNAME	|		books4Devs
MONGO_URI		|		mongodb+srv://<username>:<password>@<cluster_name>.xli3y.mongodb.net/<database_name>?retryWrites=true&w=majority
PORT			|		5000
SECRET_KEY	    |	"your secret key"

**NOTE** - YOu can generate your SECRET_KEY from any random key generating site like [randomkeygen](https://randomkeygen.com/).

These keys and values are in our env.py file which we told git to ignore and so does not ever get pushed up to the GitHub repo. Make sure to not put quotes when entering the KEYs or the VALUEs.

16. Once that is done and you have double checked you pushed the Procfile and the requirement.txt files up to GitHub. You can now click on **‘Enable Automatic Deploys’**.
17. Deploy the correct branch of the GitHub Repo (in this case the main branch)
18. Click ‘Deploy Branch’ - App successfully deployed should be shown. The app is viewable via:

>https://books-4-devs.herokuapp.com/

19. One Key thing to remember before deploying the site it to set Debug=False in the app.py file. This is very important.

## CREDITS
* [www.W3schools.com](https://www.w3schools.com/) - for pattern attribute for passwords and usernames and footer fixing to bottom of page as well as how to keep NavBar fixed.

* [Materialize](https://materializecss.com/navbar.html) - for the side-nav-bar effect and the Javascript code to initialise it.

* [Code institute](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopment) -Mini Project – Putting it all Together  (backend Development) – significant guidance on how to implement code especially for the back end app and routes and use of Flask framework was gained from here to help implement CRUD functions flash messages and view and template parameters.

* [Stackoverflow](https://stackoverflow.com/)

#### Book Images and Descriptions
**Books which were manually added to the database have images addresses and descriptions taken from select sites as follows but please note that during the testing phase descriptions and reviews may have been altered to  check feature capability so be aware of this**

Some descriptive information on the books taken from:
-https://www.serverless.com/blog/software-engineering-resources
-https://thesmartcoder.dev/10-must-read-books-for-software-engineers/#clean-code

* [C programming language](https://images-na.ssl-images-amazon.com/images/I/51TGEPRTDNL.jpg) book image and the 
Description is from - 
https://en.wikipedia.org/wiki/The_C_Programming_Language

* [Clean code](https://images-na.ssl-images-amazon.com/images/I/41yafGMO+rL._SX376_BO1,204,203,200_.jpg) book image and
Description from - https://thesmartcoder.dev/10-must-read-books-for-software-engineers/#clean-code

* [The Clean Coder](https://cdn.waterstones.com/bookjackets/large/9780/1370/9780137081073.jpg) book image and
Description from - 
https://thesmartcoder.dev/10-must-read-books-for-software-engineers/#clean-code

*  [Introduction to algorithms](https://images-na.ssl-images-amazon.com/images/I/41T0iBxY8FL._SX440_BO1,204,203,200_.jpg) book image and Description from - https://thesmartcoder.dev/10-must-read-books-for-software-engineers/#clean-code

* [C# 9 and .NET 5](https://images-eu.ssl-images-amazon.com/images/I/41h2pcTHC7L._SX218_BO1,204,203,200_QL40_ML2_.jpg) book image and the
description from – 
https://www.amazon.co.uk/NET-Cross-Platform-Development-intelligent-Framework/dp/180056810X/ref=sr_1_1_sspa?crid=2G7FUBJDV3VX1&dchild=1&keywords=c%23+programming&qid=1625057256&s=books&sprefix=c%23%2Cstripbooks%2C459&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExVFFPQTVNTks1MTExJmVuY3J5cHRlZElkPUEwNDk4MzY5MVdVSEkxUERYNFU0MiZlbmNyeXB0ZWRBZElkPUEwOTY4MzgxM1I3WEo5S0pFSFhWRiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=

* [Modern C++ Programming Cookbook](https://images-na.ssl-images-amazon.com/images/I/41uAPmFd9dL._SX404_BO1,204,203,200_.jpg)
* [Beginning Programming with Java For Dummies](https://images-na.ssl-images-amazon.com/images/I/51JIsH2gjsL._SX397_BO1,204,203,200_.jpg) book image ans description from - https://www.amazon.co.uk/Beginning-Programming-Java-Dummies-Computers/dp/1119235537/ref=sr_1_3?crid=392BIWA0C59X7&dchild=1&keywords=java+programming&qid=1625413830&s=books&sprefix=java%2Cstripbooks%2C196&sr=1-3
* [JAVA PROGRAMMING FOR BEGINNERS](https://images-na.ssl-images-amazon.com/images/I/41BnH9+t0rL._SX331_BO1,204,203,200_.jpg) book image and description from - https://www.amazon.co.uk/dp/B08KH3T7J7/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B08KH3T7J7&pd_rd_w=yYGNG&pf_rd_p=8d6f1b33-e9e1-48a7-9bf6-fb23b68a35eb&pd_rd_wg=6rcT2&pf_rd_r=ATKADNJF992FMVCB2PQ8&pd_rd_r=c0de7ba2-6e82-4602-a882-3f7b64a1870b&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMVhRTERMTkpERlZOJmVuY3J5cHRlZElkPUEwMzA3NzE1MUFRS1pFWUxIVlpaMiZlbmNyeXB0ZWRBZElkPUEwNzQ2MDk5TjE5R0Y5Qkk0NU9FJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==
* [The Algorithm Design Manual](https://images-na.ssl-images-amazon.com/images/I/41v28WnETpS._SX377_BO1,204,203,200_.jpg) book image and description from - https://www.amazon.co.uk/Algorithm-Design-Manual-Computer-Science/dp/3030542556/ref=sr_1_1?crid=1DQB66E01N0DA&dchild=1&keywords=algorithm+design+manual&qid=1625415514&s=books&sprefix=algo%2Cstripbooks%2C230&sr=1-1
* [Computer Programming: The Bible](https://images-eu.ssl-images-amazon.com/images/I/51KElbJ7EqL._SY291_BO1,204,203,200_QL40_ML2_.jpg) book image and description from - https://www.amazon.co.uk/Computer-Programming-Bible-Advanced-Raspberry/dp/1661846289
* [Learning RSLogix 5000 Programming](https://images-na.ssl-images-amazon.com/images/I/41wg93-gMNL._SX404_BO1,204,203,200_.jpg) book image and description from - https://www.amazon.co.uk/dp/1789532469/ref=sspa_dk_detail_1?psc=1&pd_rd_i=1789532469&pd_rd_w=30Glz&pf_rd_p=8d6f1b33-e9e1-48a7-9bf6-fb23b68a35eb&pd_rd_wg=IwhMc&pf_rd_r=TQV182STSFVYDVNXQCXN&pd_rd_r=a96bc0f8-1e96-497e-a4bd-64cac5d4afe0&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTENEMEFNRFgxNFBHJmVuY3J5cHRlZElkPUEwNzUxNjgyMU00MjRGN0M5SzlFMSZlbmNyeXB0ZWRBZElkPUEwNDgyODgxMUoxNTU1OFJXQ0U2VCZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=
* [Learn Python Quickly](https://images-na.ssl-images-amazon.com/images/I/41fijTjJWZL._SX348_BO1,204,203,200_.jpg) book image and description from - https://www.amazon.co.uk/dp/1951791274/ref=sspa_dk_detail_4?psc=1&pd_rd_i=1951791274p13NParams&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTFA0TDRWNlMyT09NJmVuY3J5cHRlZElkPUEwMTAzOTI5M0ZFV0lBNklDQjJTWiZlbmNyeXB0ZWRBZElkPUEwNjQ3MDc0MllMNFpaVU9CVEhMWSZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU


