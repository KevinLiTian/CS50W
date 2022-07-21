# SQL

Previously, we have learned languages such as HTML, CSS and Python, as well as the Django framework, which allow us to build dynamic web apps. As web app grows, there are data we need to store somewhere, this is where SQL comes in handy. SQL is a programming language that allows us to update and query databases

## SQLite

There are several SQL database management systems that are commonly used to store information:

- [MySQL](https://www.mysql.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLite](https://www.sqlite.org/index.html)
- ...

The first two, MySQL and PostgreSQL, are heavier-duty database management systems that are typically run on their own servers separate from those running a website. SQLite on the other hand, is a light-weight system that can store all the data in a single file. Django's default system is SQLite

#### Database

Before getting into the details of SQL, let's first discuss what is a database. A database consists of relational tables, which are just normal tables with a certain number of columns and a flexible number of rows. Relational tables stand for tables with relations between each other

#### Column Types

Just like variable types in any programming language, SQL also provides types of data:

- `TEXT`: For strings of text
- `INTEGER`: Any non-decimal number
- `REAL`: Any real number
- `NUMERIC`: A more general form a numbers, such as boolean value
- `BLOB`(Binary Large Object): Any other binary data, such as images

#### Tables

Now, to actually get started with using SQL to interact with a database, let’s begin by creating a new table. The [command to create a new table](https://www.w3schools.com/sql/sql_create_table.asp) looks something like this:

```SQL
CREATE TABLE flights(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);
```

In the above SQL command, the table created is called `flights`, which has four columns:

- `id`: `INTEGER` type data, has attributes [`PRIMARY KEY`](https://www.w3schools.com/sql/sql_primarykey.ASP), and `AUTOINCREMENT` which means that `id` is the primary way to distinguish between different rows and `id` will be automatically filled and incremented by SQL everytime we enter a new data
- `origin`, `destination`: `TEXT` type data, has attribute `NOT NULL`, which means the SQL will not accept a data without `origin` or `destination`
- `duration`: `INTEGER` type data, has attribute `NOT NULL`, SQL will not accept a data without duration

We just saw the `NOT NULL` and `PRIMARY KEY` constraint when making a column, but there are several other [constraints](https://www.tutorialspoint.com/sqlite/sqlite_constraints.htm) available to us:

- `CHECK`: Makes sure certain constraints are met before allowing a row to be added/modified
- `DEFAULT`: Provides a default value if no value is given
- `UNIQUE`: Ensures that no two rows have the same value in that column
- ...

Now that we’ve seen how to create a table, let’s look at how we can add rows to it. In SQL, we do this using the `INSERT` command:

```SQL
INSERT INTO flights
    (origin, destination, duration)
    VALUES ("New York", "London", 415);
```

In the `INSERT` command, we have to specify which table to `INSERT INTO` and for each column, provide `VALUES`. Notice we don't have to provide value for the `id` column since we specified that it should be `AUTOINCREMENT` during the creation of the table

#### SELECT

Once a table has been created and populated with data, we would want a way to retrieve the data from the database. The [`SELECT`](https://www.w3schools.com/sql/sql_select.asp) keyword allows us to extract specific information from the database:

```SQL
SELECT * FROM flights;
```

<img src="https://user-images.githubusercontent.com/99038613/179120199-d6665ca6-8b8b-4824-a047-68f4849de494.jpg" width=60%>

The `FROM` keyword specifies which table we are retrieving data from. The `*` is a wildcard select which means everything will be selected. Commonly, we don't have to retrieve all the data from the table, maybe just certain columns:

```SQL
SELECT origin, destination FROM flights;
```

<img src="https://user-images.githubusercontent.com/99038613/179120214-d6cbc214-cc39-421f-9bfe-82c24999aec3.jpg" width=60%>

As the table gets larger, we might not want to retrieve all the data from a column, but only a single row of data:

```SQL
SELECT * FROM flights WHERE id = 3;
```

The [`WHERE`](https://www.w3schools.com/sql/sql_where.asp) keyword allows us to specify a condition and the data that satisfies the condition will be selected and in this case, the row with `id = 3` will be selected

<img src="https://user-images.githubusercontent.com/99038613/179120223-210ec8d9-28db-4520-a662-46b73d40ff86.jpg" width=60%>

`WHERE` can also filter by any column, not just by `id`:

```SQL
SELECT * FROM flights WHERE origin = "New York";
```

<img src="https://user-images.githubusercontent.com/99038613/179120229-4baa62e3-a05d-46c6-8a2c-d3fd7e12e822.jpg" width=60%>

#### Working with SQL in the Terminal

Now that we learned that basic SQL commands, let's test them out in the terminal! In order to work with SQLite, first download it from [HERE](https://www.sqlite.org/download.html)(Specifically the sqlite-tools one in Precompiled Binaries). An alternative is to download the [DB Browser](https://sqlitebrowser.org/dl/) which provides a more user-friendly way to use SQL. Don't forget to add to environment after downloading it

After setting up SQLite, in the terminal, use the command `sqlite3 mydb.sql` to create a new database. You will not find the .sql file in your directory, if you would like to see it, use the command `.databases`. Some common SQLite commands are:

- `sqlite3 dbname.sqlite3`: Create new database
- `.quit`: Exit the SQLite command line
- `.databases`: List all databases, show them in directories they are in
- `.tables`: List all tables

The following code is an example of utilizing SQLite from command line:

```SQL
-- "--" is the comment in SQL language

-- Entering into the SQLite Prompt
% sqlite3 flights.sql
SQLite version 3.26.0 2018-12-01 12:34:55
Enter ".help" for usage hints.

-- Creating a new Table
sqlite> CREATE TABLE flights(
   ...>     id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...>     origin TEXT NOT NULL,
   ...>     destination TEXT NOT NULL,
   ...>     duration INTEGER NOT NULL
   ...> );

-- Listing all current tables (Just flights for now)
sqlite> .tables
flights

-- Querying for everything within flights (Which is now empty)
sqlite> SELECT * FROM flights;

-- Adding one flight
sqlite> INSERT INTO flights
   ...>     (origin, destination, duration)
   ...>     VALUES ("New York", "London", 415);

-- Checking for new information, which we can now see
sqlite> SELECT * FROM flights;
1|New York|London|415

-- Adding some more flights
sqlite> INSERT INTO flights (origin, destination, duration) VALUES ("Shanghai", "Paris", 760);
sqlite> INSERT INTO flights (origin, destination, duration) VALUES ("Istanbul", "Tokyo", 700);
sqlite> INSERT INTO flights (origin, destination, duration) VALUES ("New York", "Paris", 435);
sqlite> INSERT INTO flights (origin, destination, duration) VALUES ("Moscow", "Paris", 245);
sqlite> INSERT INTO flights (origin, destination, duration) VALUES ("Lima", "New York", 455);

-- Querying this new information
sqlite> SELECT * FROM flights;
1|New York|London|415
2|Shanghai|Paris|760
3|Istanbul|Tokyo|700
4|New York|Paris|435
5|Moscow|Paris|245
6|Lima|New York|455

-- Changing the settings to make output more readable
sqlite> .mode columns
sqlite> .headers yes

-- Querying all information again
sqlite> SELECT * FROM flights;
id          origin      destination  duration
----------  ----------  -----------  ----------
1           New York    London       415
2           Shanghai    Paris        760
3           Istanbul    Tokyo        700
4           New York    Paris        435
5           Moscow      Paris        245
6           Lima        New York     455

-- Searching for just those flights originating in New York
sqlite> SELECT * FROM flights WHERE origin = "New York";
id          origin      destination  duration
----------  ----------  -----------  ----------
1           New York    London       415
4           New York    Paris        435
```

We can use more than just equality to filtering, for numeric values, we can use greater than or less than:

```SQL
SELECT * FROM flights WHERE duration > 500;
```

<img src="https://user-images.githubusercontent.com/99038613/179120274-3fc97e28-d7ae-40a4-a50c-aebc77242544.jpg" width=60%>

We can use other logics (AND, OR) in SQL commands:

```SQL
SELECT * FROM flights WHERE duration > 500 AND destination = "Paris";
```

<img src="https://user-images.githubusercontent.com/99038613/179120280-d246d3ab-14bf-40cc-aaae-728e1c4adae8.jpg" width=60%>

```SQL
SELECT * FROM flights WHERE duration > 500 OR destination = "Paris";
```

<img src="https://user-images.githubusercontent.com/99038613/179120287-3f1015bc-c396-47ff-8660-4d60ed0e49ae.jpg" width=60%>

Just like in Python, we can use the keyword [`IN`](https://www.w3schools.com/sql/sql_in.asp) to check if a data is one of the several options:

```SQL
SELECT * FROM flights WHERE origin IN ("New York", "Lima");
```

<img src="https://user-images.githubusercontent.com/99038613/179123498-7ae149b0-2203-4f8f-be89-19fb19fd54ea.jpg" width=60%>

We can use regular expressoins to search for data more broadly using the [`LIKE`](https://www.w3schools.com/sql/sql_like.asp) keyword. For example, we can find the data with an "a" in its `origin`:

```SQL
-- "a" can be anywhere in the origin string
SELECT * FROM flights WHERE origin LIKE "%a%";

-- "a" must be the first character in the origin string
SELECT * FROM flights WHERE origin LIKE "a%";

-- "a" must be the ending character in the origin string
SELECT * FROM flights WHERE origin LIKE "%a";
```

The `%` means 0 or more characters

<img src="https://user-images.githubusercontent.com/99038613/179123503-4bebbb69-e0e5-4431-a57e-aa2b3d21280d.jpg" width=60%>

#### Functions

There are also a number of SQL functions we can apply to the results of a query. These can be useful if we don’t need all of the data returned by a query, but just some summary statistics of the data

- [`AVERAGE`](https://www.w3schools.com/sql/sql_count_avg_sum.asp)
- [`COUNT`](https://www.w3schools.com/sql/sql_count_avg_sum.asp)
- [`MAX`](https://www.w3schools.com/sql/sql_min_max.asp)
- [`MIN`](https://www.w3schools.com/sql/sql_min_max.asp)
- [`SUM`](https://www.w3schools.com/sql/sql_count_avg_sum.asp)
- ...

#### UPDATE

We now have the ability to `CREATE` a table, `INSERT` data into a table, and `SELECT` data to retrive them. Now imagine a case where an airline might upgrade their airplane and the duration will thus decrease. In this case, we might want a way to update the data for that airline. We can [`DELETE`](https://www.w3schools.com/sql/sql_delete.asp) that data then `INSERT` an updated one:

```SQL
DELETE FROM flights
WHERE origin = "Shanghai" AND destination = "Paris";
INSERT INTO flights (origin, destination, duration) VALUES ("Shanghai", "Paris", 700);
```

But this is not the best way to do it, in fact, there is an `UPDATE` that just do this work in SQL:

```SQL
UPDATE flights
    SET duration = 700
    WHERE origin = "Shanghai"
    AND destination = "Paris";
```

However, if for instance an airline is canceled permanently, `DELETE` is the one to use. Choose the suitable SQL command to do corresponding work

#### Other Clauses

There are a number of additional clauses we can use to control queries coming back to us:

- [`LIMIT`](https://www.w3schools.com/sql/sql_top.asp): Limits the number of results returned by a query
- [`ORDER BY`](https://www.w3schools.com/sql/sql_orderby.asp): Orders the results based on a specified column
- [`GROUP BY`](https://www.w3schools.com/sql/sql_groupby.asp): Groups results by a specified column
- [`HAVING`](https://www.w3schools.com/sql/sql_having.asp): Allows for additional constraints based on the number of results

#### Joining Tables

So far, we have been working on only one table, instead of the relational tables we mentioned in the beginning about databases. It turns out that many databases in practice are popuated by number of tables tha all relate to each other in some way. In the airlines example, what if we want to add the airport code to the origin and destination? Such as JFK for New York, or PVG for Shanghai. For sure we can add more columns to store the additional information, but that will make the table too large and slow down the performance when quering or storing data. Instead, we can create another `code` table that relates the cities with their airport codes:

<img src="https://user-images.githubusercontent.com/99038613/179130207-ee87618a-f23d-4810-801a-4190f04a01fa.jpg" width=60%>

Now we have the cities with their corresponding codes, we can modify the original `flights` table to store these instead of only cities. The way to do this is by using [Foreign Keys](https://www.w3schools.com/sql/sql_foreignkey.asp) in SQL:

<img src="https://user-images.githubusercontent.com/99038613/179130216-d347ff2e-6755-4b82-8fc5-6338f7da9084.jpg" width=60%>

Notice that the data in the flights table is some numeric numbers instead of `TEXT` data of city names. These numbers themselves are meaningless, but they serve as foreign keys that connects the `flights` table to the `code` table since they are the `id` of the `code` table

In addition to airport codes, airlines might want to store the data about the passengers and what airlines did they book. Therefore, we can create another table, storing the passengers with their booked airline where the `flight_id` is also a foreign key as they are the `id` of `flights` table:

<img src="https://user-images.githubusercontent.com/99038613/179130220-de6d8456-8dd5-4061-bbae-912adb7d5860.jpg" width=60%>

We can do even better, since one passenger could book more than one flights, we can make another `people` table that only contains the information of every person and the passenger table will have a foreign key from `people` and another foreign key from `flights`:

<img src="https://user-images.githubusercontent.com/99038613/179130224-a8bf0422-9baa-471b-8b74-bcd70c1e8e4a.jpg" width=60%>

<img src="https://user-images.githubusercontent.com/99038613/179130227-6357c9f1-b337-473a-ba02-e26f07f6220e.jpg" width=60%>

This creates a "Many to Many" relationship where a passenger could book more than one airline and an airline could have more than one passenger

#### JOIN Query

Although our data are stored more efficiently by now, it seems like it may be harder to query the data since they are spreaded across several tables. SQL makes it convenient by introducing the [`JOIN`](https://www.w3schools.com/sql/sql_join.asp) query where we can combine tables for data retrieval

For example, if we want to find the origin, destination and the first names of the passengers of an airline. Just to demonstrate what the `JOIN` key do, we will use the unoptimized `passengers` table with `flight_id` being one of its columns:

```SQL
SELECT first, origin, destination
FROM ...
```

This part seems familiar since we are querying about the first names of the passengers, origin and destination of an airline. But we run into a problem since `first` is stored in another table, we cannot only specify one table, `flights`, after the `FROM` keyword. Therefore we will use the `JOIN` keyword, and specify which are the foreign keys by using the `ON` keyword:

```SQL
SELECT first, origin, destination
FROM flights JOIN passengers
ON passengers.flight_id = flights.id;
```

The result will be:

```
first         origin    destination
----------  ----------  -----------
Harry        New York     London
Ron          Shanghai     Paris
Hermione     Istanbul     Tokyo
Draco        New York     Paris
Luna          Moscow      Paris
Ginny          Lima      New York
```

We’ve just used something called an [INNER JOIN](https://www.w3schools.com/sql/sql_join_inner.asp), which means we are ignoring rows that have no matches between the tables, but there are other types of joins, including [LEFT JOIN](https://www.w3schools.com/sql/sql_join_left.asp), [RIGHT JOIN](https://www.w3schools.com/sql/sql_join_right.asp), and [FULL OUTER JOIN](https://www.w3schools.com/sql/sql_join_right.asp), which we won’t discuss here in detail

#### Indexing

Indexing is an optimization technique when querying frequently and regarding specific columns. This works as if the index page of a dictionary, which will let us find contents quicker than flipping page by page. For instance, if we know that we will frequently look up passengers by their last names, we can:

```SQL
CREATE INDEX name_index ON passengers (last);
```

#### SQL Vulnerabilities

Now that we know the basics of using SQL to work with data, it's important to know the vulnerabilities associated with using SQL. Start with [SQL Injection](https://www.w3schools.com/sql/sql_injection.asp)

SQL Injection is a malicious attack using the syntax of SQL. For example, nowadays most websites have authentification systems that need users to login to check their personal information. The SQL command to check if username and password are valid is:

```SQL
SELECT * FROM users
WHERE username = username AND password = password;
```

For instance, a user Harry might enter `harrypotter` for username and `12345` for password, then the specific SQL command will be:

```SQL
SELECT * FROM users
WHERE username = "harrypotter" AND password = "12345";
```

If the data exists in the database, then the website will log Harry in. A hacker, on the other hand, might set a username `harrypotter"--` as a username and an arbitrary password which does not exist in the database. The hacker should not be allowed to log onto Harry's account but in fact he will. This is because `--` in SQL syntax is comment, so the SQL command will become:

```SQL
SELECT * FROM users
WHERE username = "harrypotter"--" AND password = "66666";
```

As the code illustrated, the SQL command after `harrypotter` is commented out, so that if there exists a username `harrypotter` in the database, the hacker will be able to log onto that account without knowing the password

To solve this problem, we can use:

- Explicitly specifying characters to make sure SQL treats the input as plain string and not as SQL code
- An abstraction layer on top of SQL which includes its own escape sequence, so we don’t have to write SQL queries ourselves, such as using Django as the abstraction layer

Another main vulnerability when it comes to SQL is known as a [Race Condition](https://searchstorage.techtarget.com/definition/race-condition#:~:text=A%20race%20condition%20is%20an,sequence%20to%20be%20done%20correctly.)

A race condition is a situation that occurs when multiple queries to a database occur simultaneously. When these are not adequately handled, problems can arise in the precise times that databases are updated. For example, let’s say I have $150 in my bank account. A race condition could occur if I log into my bank account on both my phone and my laptop, and attempt to withdraw $100 on each device. If the bank’s software developers did not deal with race conditions correctly, then I may be able to withdraw $200 from an account with only $150 in it. One potential solution for this problem would be locking the database. We could not allow any other interaction with the database until one transaction has been completed. In the bank example, after clicking navigating to the “Make a Withdrawl” page on my computer, the bank might not allow me to navigate to that page on my phone

## Django Models

[Django Models](https://docs.djangoproject.com/en/4.0/topics/db/models/) are a level of abstraction on top of SQL that allow us to work with databases using Python classes and objects rather than direct SQL queries

Let’s get started on using models by creating a django project for our airline, and creating an app within that project:

```shell
django-admin startproject airline
cd airline
python manage.py startapp flights
```

Now we’ll have to go through the process of adding an app as usual:

1. Add `flights` to the `INSTALLED_APPS` list in `settings.py`
2. Add a route for `flights` in `urls.py`:
   `path("flights/", include(flights.urls))`
3. Create a `urls.py` file within the `flights` app

Now we will take a look at the `models.py` file. In this file, we will outline what data we want to store in our application. Then Django will determine the SQL syntax necessary to store information on each of our models

```Python
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()
```

- In the first line, we create a new model that extends Django’s model class
- Below, we add fields for origin, destination, and duration. The first two are [Character Fields](https://docs.djangoproject.com/en/4.0/ref/forms/fields/#charfield), meaning they store strings, and the third is an [Integer Field](https://docs.djangoproject.com/en/4.0/ref/forms/fields/#integerfield). These are just two of many [built-in Django Field classes](https://docs.djangoproject.com/en/4.0/ref/forms/fields/#built-in-field-classes)
- We specify maximum lengths of 64 for the two Character Fields. you can check the specifications available for a given field by checking the [documentation](https://docs.djangoproject.com/en/4.0/ref/forms/fields/#built-in-field-classes)

#### Migration

Now that we've created a Django model class, we don't yet have a database setup. In order to create a database from the models, we navigate to the main directory of the Django project and run the command:

`python manage.py makemigrations`

This command will create some Python files that allow us to create and query the database. Next, to actually create the database itself, we run the following command:

`python manage.py migrate`

Which will create a `db.sqlite3` file as the database

#### Shell

After setting up a database, we need a way to interact with it, for example insert data or retrieve data. We can enter Django's shell to achieve this:

`python manage.py shell`

```shell
Python 3.7.2 (default, Dec 29 2018, 00:00:04)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.5.0 -- An enhanced Interactive Python. Type '?' for help.
```

```shell
# Import our flight model
In [1]: from flights.models import Flight

# Create a new flight
In [2]: f = Flight(origin="New York", destination="London", duration=415)

# Instert that flight into our database
In [3]: f.save()

# Query for all flights stored in the database
In [4]: Flight.objects.all()
Out[4]: <QuerySet [<Flight: Flight object (1)>]>
```

When we query the database using `Flight.objects.all()`, we see an output that says `Flight object (1)` which isn't that helpful. We can create a `__str__` function within the `Flight` class to define what should the output of the query be:

```Python
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
```

Not if we go back to the shell and query again, the output will be more readable:

```shell
# Create a variable called flights to store the results of a query
In [7]: flights = Flight.objects.all()

# Displaying all flights
In [8]: flights
Out[8]: <QuerySet [<Flight: 1: New York to London>]>

# Isolating just the first flight
In [9]: flight = flights.first()

# Printing flight information
In [10]: flight
Out[10]: <Flight: 1: New York to London>

# Display flight id
In [11]: flight.id
Out[11]: 1

# Display flight origin
In [12]: flight.origin
Out[12]: 'New York'

# Display flight destination
In [13]: flight.destination
Out[13]: 'London'

# Display flight duration
In [14]: flight.duration
Out[14]: 415
```

Now that we've learned how to work with Django models, let's think back to the design earlier where cities and their airport codes are stored as a separate table:

```Python
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
```

- Notice that the `origin` and `destination` are changed from `CharField` to [`ForeignKey`](https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/)
- `on_delete=models.CASCADE` means that if an airport is deleted for whatever reason in the `airports` table, since some airlines in `flights` table will no longer have an airport to reference to via foreign key, they will also be deleted automatically
- We also provide a [`related name`](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ForeignKey.related_name) which gives us a way to search for all airlines with a given airport as their origin or destination

Every time we make changes to `models.py`, we'll have to repeat the two migration commands in order to let the change take effect in the database

```shell
# Create New Migrations
python manage.py makemigration

# Migrate
python manage.py migrate
```

Now we can try to use the new models in the Django shell:

```shell
# Open up the Django shell
python manage.py shell

# Import all models
In [1]: from flights.models import *

# Create some new airports
In [2]: jfk = Airport(code="JFK", city="New York")
In [4]: lhr = Airport(code="LHR", city="London")
In [6]: cdg = Airport(code="CDG", city="Paris")
In [9]: nrt = Airport(code="NRT", city="Tokyo")

# Save the airports to the database
In [3]: jfk.save()
In [5]: lhr.save()
In [8]: cdg.save()
In [10]: nrt.save()

# Add a flight and save it to the database
f = Flight(origin=jfk, destination=lhr, duration=414)
f.save()

# Display some info about the flight
In [14]: f
Out[14]: <Flight: 1: New York (JFK) to London (LHR)>
In [15]: f.origin
Out[15]: <Airport: New York (JFK)>

# Using the related name to query by airport of arrival:
In [17]: lhr.arrivals.all()
Out[17]: <QuerySet [<Flight: 1: New York (JFK) to London (LHR)>]>
```

#### Starting the Application

We can now build an application with the skills of working with Django models to create and interact with a database. First create a `urls.py` file in the airline application:

```Python
urlpatterns = [
    path('', views.index, name="index")
]
```

And inside `views.py`

```Python
from django.shortcuts import render
from .models import Flight, Airport

# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })
```

Also create a `layout.html` and a `index.html` file

- `layout.html`

  ```HTML
  <!DOCTYPE html>
  <html lang="en">
      <head>
          <title>Flights</title>
      </head>
      <body>
          {% block body %}
          {% endblock %}
      </body>
  </html>
  ```

- `index.html`

  ```HTML
  {% extends "flights/layout.html" %}

  {% block body %}
    <h1>Flights:</h1>
    <ul>
        {% for flight in flights %}
            <li>Flight {{ flight.id }}: {{ flight.origin }} to {{ flight.destination }}</li>
        {% endfor %}
    </ul>
  {% endblock %}
  ```

Now our webpage is able to display all the flights information stored in our database

![1](https://user-images.githubusercontent.com/99038613/179260206-21f201d3-8ccc-4dc8-b8e1-8387caf65218.jpg)

#### Django Admin

Instead of interacting with the database in the Django shell, Django provides a more convenient way which is the Django Admin. We start by creating an administrative userL

```shell
python manage.py createsuperuser
Username: superuser
Email address: superuser@gmail.com
Password:
Password (again):
Superuser created successfully.
```

Next, navigate to `admin.py` and register our models:

```Python
from django.contrib import admin
from .models import Flight, Airport

# Register your models here.
admin.site.register(Flight)
admin.site.register(Airport)
```

Now, when we visit our site and add /admin to the url, we can log into a page that looks like this

<img src="https://user-images.githubusercontent.com/99038613/179260272-2e79a9ac-c2fb-4308-a305-343d48850eb9.jpg" width=60%>

<img src="https://user-images.githubusercontent.com/99038613/179260284-f4df1557-af35-4a2e-a4ed-cac6dfe5369f.jpg" width=60%>

#### Many to Many Relationship

Think back to the relationship where a passenger could book more than one flight and a flight could have booked by more than one passenger. We can achieve this by using the `ManytoManyField` in Django:

```Python
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
```

- `blank=true` means that a passenger could have no flights
- `related_name` allows us to find all passengers given a flight

Remember to register this new model in `admin.py` and also make migrations using the two commands mentioned before

We can now show a flight's information with all its passengers' information as well

```Python
def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers
    })
```

And in `flight.html`

```HTML
<h2>Passengers:</h2>
<ul>
    {% for passenger in passengers %}
        <li>{{ passenger }}</li>
    {% empty %}
        <li>No Passengers.</li>
    {% endfor %}
</ul>
```

<img src="https://user-images.githubusercontent.com/99038613/179260415-add9702a-b095-4669-85b5-1fd8f59d955e.jpg" height=60%>

## Users

Django also makes it easy for us to create an authentification system, allowing users to sign in or out of the website. We'll start by creating an app called `users`. After going through the normal steps of creating a new app, in the `urls.py` in this new app, we add a few more routes:

```Python
urlpatterns = [
    path('', views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]
```

Then create a form where a user can log in:

```HTML
{% extends "users/layout.html" %}

{% block body %}
    {% if message %}
        <div>{{ message }}</div>
    {% endif %}

    <form action="{% url 'login' %}" method="post">
        {% csrf_token %}
        <input type="text", name="username", placeholder="Username">
        <input type="password", name="password", placeholder="Password">
        <input type="submit", value="Login">
    </form>
{% endblock %}
```

Then in `views.py`:

```Python
def index(request):
    # If no user is signed in, return to login page:
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

def login_view(request):
    return render(request, "users/login.html")

def logout_view(request):
    # Pass is a simple way to tell python to do nothing.
    pass
```

Next, we can head to the admin site and add some users. After that we will update the `login_view` function to handle a `POST` request with a username and password:

```Python
# Additional imports we'll need:
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        # Otherwise, return login page again with new context
        else:
            return render(request, "users/login.html", {
                "message": "Invalid Credentials"
            })
    return render(request, "users/login.html")
```

Then we will implement the log out function to log users out:

```Python
def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
                "message": "Logged Out"
            })
```

These are the backend operations during an authentication process. You are welcome to customize the `user.html` and `login.html` to make the login page more attractive

## Examples

Check out some [examples](examples/)
