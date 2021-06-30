import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    developer_books = list(mongo.db.developerBooks.find())
    #this developer_books is technically not a list but a mongo
    #cursor object, we turn it into a proper list
    return render_template("index.html", developer_books=developer_books)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("book_search")
    developer_books = list(mongo.db.developerBooks.find({"$text": {"$search": book_search}}))
    return render_template("index.html", developer_books=developer_books)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # we then need to check if the username already exists 
        # in the db - we use the get method
        # on our form to check if the key value matches #anything in our db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        # this acts as the else statement which creates the 
        # dictionary to be inserted
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        #this then inserts the dictionary abive into our mongodb 
        #collection for users
        mongo.db.users.insert_one(register)

        #put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        #if registration successful we want the user to go to their profile page
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #we will check to see if the username already exists in our db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
       
        if existing_user:
            #we need to make sure the existing hash password matches the input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    #if log in successful we want the user to go to their profile page
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                #if the password is invalid/does not match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template('login.html')


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # this username variable we create is for the user we find in the db so
    #so we are grabbing the sessions user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    #remove the iser from the session cookie
    #this can be done in couple ways
    #1-session.clear() - which would remove all session cookies on the app
    #2-session.pop("user")
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        # we want to add this posted form to the developerBooks collection
        # in our books4Devs db
        # we create a new dict (called book) to store all the values
        # we get from the form
        # ready to be inserted into our colleciton via the mongo.db method.
        book = {
            "title": request.form.get("title"),
            "imgURL": request.form.get("imgURL"),
            "author": request.form.get("author"),
            "desc": request.form.get("desc"),
            "rating": int(request.form.get("rating")),
            "comments": request.form.get("comments"),
            "get_book": request.form.get("get_book"),
            "added_by": session["user"]
        }

        mongo.db.developerBooks.insert_one(book)
        flash("Your book was successfully added")
        return redirect(url_for(
            "profile", username=session["user"]))

    return render_template("add_book.html")


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        # we want to post this edited form to the developerBooks collection
        # in our books4Devs db
        # we create a new dict (called book_edits) to store all the values we get from the edit_book form
        # ready to be inserted into our colleciton modification in the mongo.db method.
        book_edits = {
            "title": request.form.get("title"),
            "imgURL": request.form.get("imgURL"),
            "author": request.form.get("author"),
            "desc": request.form.get("desc"),
            "rating": int(request.form.get("rating")),
            "comments": request.form.get("comments"),
            "get_book": request.form.get("get_book"),
            "added_by": session["user"]
        }

        # this time in our mongo.db update we use .update()
        # this takes two parameters which are both dicts.
        mongo.db.developerBooks.update({"_id": ObjectId(book_id)}, book_edits)
        flash("Your book was successfully Updated")
        return redirect(url_for(
            "profile", username=session["user"]))
    # we need to get the correct book(document) from the db
    # so we target the objectid of the book variable using the import bson
    # the bson format is what is accepted readable by mongodb
    book = mongo.db.developerBooks.find_one({"_id": ObjectId(book_id)})
    return render_template("edit_book.html", book=book)


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    mongo.db.developerBooks.remove({"_id": ObjectId(book_id)})
    flash("Book successfully deleted")
    return redirect(url_for(
                        "profile", username=session["user"]))

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)