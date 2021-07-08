# Books4Devs
Books4Devs is an online platform that allows for the recommendation and review of IT related (in particular programming/development) books. Users are able to see the books that have been posted by other users; these posted books are have a front cover image, description, rating and comments from the person who posted it and also a link to an external site for purchasing of the book. In addition, users are able to post their own book suggestions, update their book suggestions or even delete only their own book suggestions

## USER EXPERIENCE

**PLEASE NOTE: These User Experience scenarios are what were used for the testing of the site features so please refer to them for testing outcome**

**Please Note – Regarding Side Nave bar:**
In all the user scenarios, for smaller devices and smaller screens the nav items a condensed into a hamburger icon which when clicked on brings up the ‘side-nav’ bar for the user to make their selections.

#### USER SCENARIOS

* **User A is looking for a book**
A first time user lands on the [homepage](http://books-4-devs.herokuapp.com/) and is greeted with the website introduction passage and asked to Log in or Register if they want to add their own book reviews (Login and register at top in navbar as well).

Below that is a search bar section which allows a use to search for a book via the name of it or by the author(s) names. So if user knows the name of the book or authors name they could type this into the search box.

User A could just scroll down on the all books section of the home page and scroll though the lists of books available. Each book’s more detailed information is available by clicking on the plus icon floating between the image and the book information. Clicking on the plus icon takes the user to the book’s personal page.

* **User B wants to register in order to add reviews of their own**
While on the homepage, user B can click on the ‘Register’ in the navbar or the ‘Register’ link in the introductory text. Which then takes them onto the Register page which displays the register card with the username and password inputs.

User B can then create a username and password using the placeholder text as a guidance on the restrictions allowed. If username is not in use then the user account is created and user is logged in and shown a flash message saying ‘registration successful!’ and brought back on to the home page with all the books but this time the nav items available are ‘All Book, My Books, Add a Book and Log Out.’

If User B goes into the ‘My Books’ section they are shown a text that they currently have no books in their profile and to click on the ‘add a book’ button in order to add their book.

If Username already exists then the user can try another name. If they remembered they are already registered then they can go to the Log In page via the button at the bottom of the register panel.

* **User C is already registered and so logs in with authentication.**
While on the homepage, user C can click on the ‘Log In’ item in the navbar or the ‘LogIn’ link in the introductory text. Which then takes them onto the ‘Log In’ page which displays the Log In panel with the username and password inputs fields.

If the User attempts to log in and is successful then they get a flash message saying ‘Log In Successful’ and they are brought onto their ‘My Books’ page which is their profile of all their books they have added (note: this is different to a new user who has just registered as a new user is taken to the homepage as they will not have any books in their profile). From here the user is able to view their book and edit/delete or add a books.

* **User D wants to post their own book (Add a Book)**
Once user is logged into their account they can add/post a book review using either the ‘Add a Book’ nav item at the top or while in their profile in the ‘My Books’ section they can click on the Add a Book button. User D is then presented with an ‘Add Book’ Form which has all the various fields required to complete adding a valid book review. All fields are mandatory and have to be done as directed. On completion User D clicks the add book button at the bottom of the form which if filled out correctly gives the user a flash message to say book has been successfully added. This book card is then visible on User Ds all books page as well as in the ‘My Books’ section which is where they are returned to on completing the book addition.

* **User E wants to delete a book they have posted**
User E can see a delete button only on books they have added. Even in the all books sections, the books that have been added by User E have the delete button on them as well as the list of books in their ‘My Books’ section. On clicking this delete button the user is shown a confirm alert box done using JavaScript which confirms if the user is sure they want to delete this book. On clicking OK the book is deleted and a flash message is given confirming successful deletion however on clicking cancel the user is returned to the page they were on with no action.

* **User F wants to amend/update a book they have made.**
Like User E in the deletion action, User F is able to do this via the list of books in All Books where only books they have added will have the Edit button on it. Or also via there My Books section which will show only their books. Clicking on the Edit Button takes the user to Edit Book which is prefilled with all the books current information from the previous posting. User F is then able to manually go to each field and amend information as they so please. Then at the bottom of the form the user can click the cancel button which takes them back to their ‘my books’ section and they will get a flash message that book was successfully updated even if they did not make any changes. On clicking ‘confirm edit’ they are returned to the My Books page with the same flash message book successfully updated.

* **User G wants to get a book they have an interest in**
User G likes the review they have read on a particular book and so click on the ‘Get this Book’ button. This opens a new tab for the user which is the purchasing site of the book e.g. amazon. The user remains having the page for their Books4Devs site open so able to continue browsing.


## FEATURES
### Existing Features

* **Site Navigation**
On top of screen there is the fixed Nav Bar which is always visible on scrolling down the page:
* Large Screens
    * When not Logged In - shows to left Book4 Devs Logo which is clickable  and on clicking returns you to home page on all pages, then to the right the nav icons ‘All Books’, ‘Log In’, ‘Register’
    * When logged In  - Books4Devs Logo  to the left and ‘All Books’, ‘My Books’, ‘Add a Book’, ‘Log Out’

*  Screens sizes 992px or less
    * Books4Devs Logo goes centre of screen
    * Other Nav Icons go into a 3 bar “hamburger” icon to the left of screen which on clicking brings up the side-nav with the same options as the large screens details above.

* **Not Logged In**
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

* **Logged In Users**
* Add a Book
    * User can add a book(s) using the add book nav item or while in their ‘my books’ section can click on the Add a Book button which take them to the same add a book form. User fills the form out as directed which creates the new book entry and if done correct creates the new book
* Edit a Book
    * User can only update a book they have added. Edit makes changes to the posted book information and this is then saved to the database.
* Delete a Book
    * User is able to delete only a book(s) they have created. Once deleted the book is deleted from the database permanently.

* **Footer Section**
User is able to go see the Social Media links of Books4Devs (Facebook, Twitter & Pinterest) – currently due to not having any social media accounts set up, these icons only take the user to the homepages these platforms


### Future Features
* **Wider Search Filter**
User can find books in a wider range of categories and not just by name and author search. For example, categorise books on specific languages (python, C, JavaScript, C++, C# etc.). Another good search category will be other’s usernames. Users may like a particular user’s reviews and recommendations and so will be able to search for this user by username and be able to see only posts from this user.

* **A user wants to leave a review/comment on a book they did not post**

* **Users will be able to review/comment on a book added by another user.** 
The feature will also allow users to string comment on another users review if they do not fully agree with certain aspects of that review however this would have to have strict rules to prevent any unclean verbal exchanges however debates on a book are encouraged.

* **Average rating system for books**
Add a feature where the books rating is based on not just the person that added it to the books list but an average of all people who have reviewed the book and given it a rating.


* **Prevent Reposting of the same book**
Make it so that users cannot post a book that someone else has already posted. This will have to be added in line with users being able to add a review and rating on any book.

* **A user wants to delete their own account**
Add this option so that if a user wants to remove their account they can do and so have their credentials taken off the database.

* **Increase User account profile**
User accounts have more information rather than just the username name password. The users profile will show how many postings they have made and the average ratings they give books. Users will be able to share their line of work in this enhanced user profile so as to appear more credible on their reviews in a certain subject matter.

* **A user wants to make contact with a query or make a complaint**
A contact us section will be created that allows users to post a query or even make a complaint report what they deem harmful or unjust comments or reviews from other users.

* **Affiliate Links**
Have affiliate links for the site for when a user goes on to purchase a book through the site, Books4Devs makes money from it.

* **Social Media Platforms**
Social media accounts for Books4Devs will be added which will allow for users to follow and network better with Books4Devs on several platforms.

## TECHNOLOGIES USED

## TESTING

## DEPLOYMENT

## CREDITS