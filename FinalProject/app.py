import os

import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from helpers import login_required

#Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# make sure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# be sure that API-KEY is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# to use SQLite database
conn = sqlite3.connect('life.db' , check_same_thread=False)
cursor = conn.cursor()


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def mainpage():
    return render_template("home.html")

@app.route("/info", methods=["GET", "POST"])
@login_required
def info():
    if request.method == "POST":
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        country = request.form.get("country")
        city = request.form.get("city")
        qualities = request.form.get("qualities")
        age = request.form.get("age")
        working =  request.form.get("working")
        studying = request.form.get("studying")
        field = request.form.get("field")
        activities = request.form.get("activities")
        skills = request.form.get("skills")
        experience = request.form.get("experience")



        # check if the table has a data for the user, if not , it shows him an error if he doesn't fill all the fields
        # but if he has already typed it before, he can see directly his information;
        cursor.execute("SELECT * FROM info WHERE user_id = ?", (session["user_id"],))
        data = cursor.fetchall()
        if ((firstname == "" or lastname == "" or country == "" or city == "" or qualities =="" or age == "" or field == "" or activities == "" or skills ==""
        or working == "" or studying == "" or experience == "") and len(data) == 0 ):
            flash("No data provided")
            return render_template("error.html")
        else:

            cursor.execute("INSERT OR REPLACE INTO info (user_id,firstname,lastname,country,city,qualities,age,working,studying,field,activities,skills, experience) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (session["user_id"],firstname,lastname,country,city,qualities,age,working,studying,field,activities,skills,experience))
            conn.commit()

            # if the user submits the form without typing anything and he has data, he will get the data that he entered in the past
            # I made that so we don't get an empty form if the users doesn't fill any of the fields
            cursor.execute("DELETE FROM info WHERE firstname = ? OR lastname = ? OR country = ? OR city = ? OR qualities = ? OR age = ?  OR activities = ? OR skills = ? OR experience = ?", ("","","","","","","","","",))
            conn.commit()

            # i selected the number of rows to show the latest data that the user had provided
            # count begins from zero, so to arrive to the final number, we have to add 1 so we accessed with for loop the number and added 1.
            cursor.execute("SELECT COUNT(id) from info")
            count = cursor.fetchone()
            for x in count:
                value = x
            cursor.execute("SELECT * FROM info WHERE id = ? ", (value,))
            info = cursor.fetchall()
            return render_template("allinfo.html", info = info)

    else:
        return render_template("Info.html")


@app.route("/todo" , methods=["GET", "POST"])
@login_required
def todo():
    if request.method == "POST":
        birthday = request.form.get("birthday")
        task = request.form.get("task")
        importance = request.form.get("importance")

        cursor.execute("INSERT OR REPLACE INTO TODO(user_id,task,date,importance) VALUES(?,?,?,?)", (session["user_id"],task,birthday,importance))
        conn.commit()
        cursor.execute("SELECT * FROM todo WHERE user_id = ?", (session["user_id"],))
        todo = cursor.fetchall()
        return render_template("todo.html", todo = todo)

    else:
        cursor.execute("SELECT * FROM todo WHERE user_id = ?", (session["user_id"],))
        todo = cursor.fetchall()
        return render_template("todo.html", todo = todo)

@app.route("/searchtodobyname", methods=["GET", "POST"])
@login_required
def searchtodo():
    if request.method == "POST":
        task = request.form.get("searchtask")
        cursor.execute("SELECT * FROM todo WHERE user_id = ? AND task = ?", (session["user_id"],task))
        searchname = cursor.fetchall()
        cursor.execute("SELECT * FROM todo WHERE user_id = ?", (session["user_id"],))
        todo = cursor.fetchall()

        return render_template("todo.html", searchname = searchname, todo = todo)
    else:
        return render_template("todo.html")

@app.route("/searchtodobydate", methods=["GET", "POST"])
@login_required
def searchtodobydate():
    if request.method == "POST":
        date = request.form.get("searchbydate")
        cursor.execute("SELECT * FROM todo WHERE user_id = ? AND date = ?", (session["user_id"],date))
        searchname = cursor.fetchall()
        cursor.execute("SELECT * FROM todo WHERE user_id = ?", (session["user_id"],))
        todo = cursor.fetchall()

        return render_template("todo.html", searchname = searchname, todo = todo)
    else:
        return render_template("todo.html")

@app.route("/searchtodobypriority", methods=["GET", "POST"])
@login_required
def searchtodobypriority():
    if request.method == "POST":
        priority = request.form.get("searchbypriority")
        cursor.execute("SELECT * FROM todo WHERE user_id = ? AND importance = ?", (session["user_id"],priority))
        searchname = cursor.fetchall()
        cursor.execute("SELECT * FROM todo WHERE user_id = ?", (session["user_id"],))
        todo = cursor.fetchall()

        return render_template("todo.html", searchname = searchname, todo = todo)
    else:
        return render_template("todo.html")


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
        cursor.execute("DELETE FROM todo WHERE id = ?", (todo_id,))
        conn.commit()
        cursor.execute("SELECT * FROM todo WHERE user_id = ?", (session["user_id"],))
        todo = cursor.fetchall()
        return render_template("todo.html", todo = todo)


@app.route("/expenses" , methods=["GET", "POST"])
@login_required
def expenses():
    if request.method == "POST":
        return render_template("error.html")

    else:
        return render_template("Expenses.html")

@app.route("/budget", methods=["GET", "POST"])
@login_required
def budget():
    if request.method == "POST":
        paycheck = float(request.form.get("paycheck"))
        otherincome = float(request.form.get("otherincome"))
        totalincome = paycheck + otherincome
        rent = float(request.form.get("rent"))
        grocery = float(request.form.get("grocery"))
        gas = float(request.form.get("gas"))
        carloan = float(request.form.get("carloan"))
        houseloan = float(request.form.get("houseloan"))
        creditcard = float(request.form.get("creditcard"))
        otherspending = float(request.form.get("otherspending"))
        month = request.form.get("month")
        year = request.form.get("year")
        totalspending = rent + grocery + gas + carloan + houseloan + creditcard + otherspending
        savings = totalincome - totalspending

        cursor.execute("SELECT * FROM budget WHERE user_id = ? AND month = ? AND year = ?", (session["user_id"],month,year))
        infointable = cursor.fetchall()
        if(len(infointable) != 0):
            flash("Information has been filled for this month")
            return render_template("error.html")
        else:
            cursor.execute("INSERT INTO budget(user_id,paycheck,otherincome,rent,grocery,gas,carloan,houseloan,creditcard,otherspending,totalincome,totalspending,savings,month,year) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (session["user_id"],paycheck,otherincome,rent,grocery,gas,carloan,houseloan,creditcard,otherspending,totalincome,totalspending,savings,month,year))
            conn.commit()

            return render_template("budget.html",
            totalincome =  totalincome, totalspending = totalspending, savings = savings)
    else:
        return render_template("budget.html")


@app.route("/searchbudget", methods = ["GET", "POST"])
@login_required
def searchbudget():
    if request.method == "POST":
        searchmonth = request.form.get("searchmonth")
        searchyear = request.form.get("searchyear")
        cursor.execute("SELECT * FROM budget WHERE user_id = ? AND month = ? AND year = ?", (session["user_id"],searchmonth,searchyear))
        budgetsearch = cursor.fetchall()
        return render_template("budget.html", budgetsearch = budgetsearch)

    else:
        return render_template("budget.html")



@app.route("/investement", methods=["GET", "POST"])
@login_required
def investement():
    if request.method == "POST":
        investement = float(request.form.get("investement"))
        years = float(request.form.get("years"))
        current = float(request.form.get("current"))
        possiblereturn = float(request.form.get("possiblereturn"))/100 + 0.02
        numerator = float(current * possiblereturn)
        denominator = float((1+possiblereturn)**years)
        pmt = round(numerator / denominator)
        firsthalfofphrase = "So your monthly contribution of $"
        secondhalfofphrase = "will bring you each time a step closer to achieving your financial freedom."

        return render_template("investement.html", pmt = pmt, firsthalfofphrase = firsthalfofphrase, secondhalfofphrase = secondhalfofphrase)

    else:
        return render_template("investement.html")


@app.route("/iqtest" , methods=["GET", "POST"])
@login_required
def iqtest():
    if request.method == "POST":
        return render_template("iqtest.html")
    else:
        return render_template("iqtest.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Ensure username was submitted
        if not username:
            flash("Missing username")
            return render_template("error.html")

        # Ensure password was submitted
        elif not password:
            flash("Missing password")
            return render_template("error.html")

        # Query database for username
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        rows = cursor.fetchall()

        # Ensure username exists and password is correct
        if len(rows) != 1:
            flash("Invalid username and password.")
            return render_template("error.html")
        else:
            if  password != rows[0][2]:
                flash("Invalid password")
                return render_template("error.html")

            else:
                # Remember which user has logged in
                session["user_id"] = rows[0][0]

                # Redirect user to home page
                return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return render_template("login.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        usernamee = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        cursor.execute("SELECT username from users WHERE username = ?", (usernamee,))
        names = cursor.fetchone()

        # check if the username is already used
        if names is not None:
            flash(" Username already taken. Please use another username")
            return render_template("error.html")

            # check if the confirm password field corresponds with the password
        elif password != confirmation:
            flash(" Confirmation doesn't match password")
            return render_template("error.html")

        else:
            cursor.execute("INSERT OR REPLACE INTO users (username, hashpass) Values(?,?)", (usernamee, password))
            conn.commit()
            return render_template("login.html")
    else:
        return render_template("register.html")