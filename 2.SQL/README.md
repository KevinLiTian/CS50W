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
DELETE FROM flights WHERE origin = "Shanghai" AND destination = "Paris";
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
