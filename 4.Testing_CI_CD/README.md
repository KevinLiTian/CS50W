# Testing & CI/CD

In our development workflow, we might encounter various tedious issues such as having to test a huge code base by hand, or when working as a team, there are lots of conflicts between commits, etc. We will introduce some best practices of software development, including automation of the testing process, and tools to achieve continous integration/delivery

## General Testing

One important part of the software development process is the act of **Testing** the code we’ve written to make sure everything runs as we expect it to

### Assert

One of the simplest ways we can run tests in Python is by using the `assert` command. This command should be followed by something we think should be true

```Python
def square(x):
    return x * x

assert square(10) == 100
""" Output:

"""
```

We think that the square of 10 should be equal to 100, if there's no bug within our square function, then the `assert` will not output anything, as if it doesn't exist; however, if something went wrong:

```Python
def square(x):
    return x + x

assert square(10) == 100

""" Output:
Traceback (most recent call last):
  File "assert.py", line 4, in <module>
    assert square(10) == 100
AssertionError
"""
```

The `assert` will give us some information about where things went wrong so we don't have to start nowhere. `assert` doesn't seem that useful in this simple example, but imagine the code base is enormous, and with the help of `assert`, you will be able to identify where things went wrong immediately

### Test Driven Development

As you begin building larger projects, you may want to consider using test-driven development, a development style where every time you fix a bug, you add a test that checks for that bug to a growing set of tests that are run every time you make changes. Ensuring that later features does not affect existing ones

Let's look at an example:

```py
import math

def is_prime(n):

    # We know numbers less than 2 are not prime
    if n < 2:
        return False

    # Checking factors up to sqrt(n)
    for i in range(2, int(math.sqrt(n))):

        # If i is a factor, return false
        if n % i == 0:
            return False

    # If no factors were found, return true
    return True
```

The above program is designed to identify prime numbers, and we want to test if this function is flawless. We can write a test function:

```py
from prime import is_prime

def test_prime(n, expected):
    if is_prime(n) != expected:
        print(f"ERROR on is_prime({n}), expected {expected}")
```

Then we can run this test function with different inputs by hand and test whether expected output matches current output. But there are lots of numbers to test, if we do it by hand everytime, then test-driven development is meaningless since we are trying to make debugging more convenient

One way to do this is by creating a shell script, which is some commands to be run in the terminal:

In a file called `test_prime.sh`:

```sh
python3 -c "from tests0 import test_prime; test_prime(1, False)"
python3 -c "from tests0 import test_prime; test_prime(2, True)"
python3 -c "from tests0 import test_prime; test_prime(8, False)"
python3 -c "from tests0 import test_prime; test_prime(11, True)"
python3 -c "from tests0 import test_prime; test_prime(25, False)"
python3 -c "from tests0 import test_prime; test_prime(28, False)"
```

Then we can run this shell script in the terminal by running `./test_prime.sh`. Which will then give the result:

```
ERROR on is_prime(8), expected False
ERROR on is_prime(25), expected False
```

### Unit Testing

A popular Python testing method is unit testing, which makes testing easier and provides some useful outputs for debugging. Let's take a look at what a unit testing program would look like for the `is_prime` function

```py
# Import the unittest library and our function
import unittest
from prime import is_prime

# A class containing all of our tests
class Tests(unittest.TestCase):

    def test_1(self):
        """Check that 1 is not prime."""
        self.assertFalse(is_prime(1))

    def test_2(self):
        """Check that 2 is prime."""
        self.assertTrue(is_prime(2))

    def test_8(self):
        """Check that 8 is not prime."""
        self.assertFalse(is_prime(8))

    def test_11(self):
        """Check that 11 is prime."""
        self.assertTrue(is_prime(11))

    def test_25(self):
        """Check that 25 is not prime."""
        self.assertFalse(is_prime(25))

    def test_28(self):
        """Check that 28 is not prime."""
        self.assertFalse(is_prime(28))


# Run each of the testing functions
if __name__ == "__main__":
    unittest.main()
```

Notice that each test function within the `Tests` class followed a pattern:

- Name of the function begin with `test_`, which is required in order to be run automatically by `unittest.main()`
- Each function contains a docstring, these are not just for readability, they will be displayed as outputs if anything went wrong for that function
- In each function, there's an assertion in the form of `self.assertSOMETHING`. There are many assertions provided by Python such as `assertTrue`, `assertFalse`, `assertEqual`, `assertGreater`, [etc](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual).

Now if we run these tests by running this Python module, we get the output of:

```sh
...F.F
======================================================================
FAIL: test_25 (__main__.Tests)
Check that 25 is not prime.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests1.py", line 26, in test_25
    self.assertFalse(is_prime(25))
AssertionError: True is not false

======================================================================
FAIL: test_8 (__main__.Tests)
Check that 8 is not prime.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests1.py", line 18, in test_8
    self.assertFalse(is_prime(8))
AssertionError: True is not false

----------------------------------------------------------------------
Ran 6 tests in 0.001s

FAILED (failures=2)
```

- The line `...F.F` indicates which test failed. Each `.` is a passed test case and each `F` is a failed test case
- Then, for each tests failed, we are given the name of the function, such as `FAIL: test_25 (__main__.Tests)`
- Next, we have the docstring we wrote for that function, `Check that 25 is not prime.`
- And we have a traceback of which line is the error

  ```sh
  Traceback (most recent call last):
  File "tests1.py", line 26, in test_25
  self.assertFalse(is_prime(25))
  AssertionError: True is not false
  ```

- Finally we have a summary of tests

  ```sh
  Ran 6 tests in 0.001s

  FAILED (failures=2)
  ```

Now if we fixed the error in the `is_prime` function which is the line:

`for i in range(2, int(math.sqrt(n)) + 1):`

Then run the unit test again:

```sh
......
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```

## Web Testing

Now let's see how the idea of automated testing can be applied to web applications, starting with the Django framework

### Django Testing

We'll use the `flights` example when we first learned Django models. Consider the `Flight` model with entries `origin`, `destination` and `duration`. We want to make sure they meet two requirements:

1. The `origin` and `destination` are not the same
2. The duration is longer than 0

After writing out the model itself and a test function, now our model class could look this:

```py
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

    def is_valid_flight(self):
        return self.origin != self.destination or self.duration > 0
```

Now let's use the `test.py` file, which we haven't touched before. The Django's [TestCase](https://docs.djangoproject.com/en/4.0/topics/testing/overview/) library is automatically imported in this file

The advantage of using Django's TestCase library is that a completely new database will be created, independent of our original database, and is solely for testing purposes.

Now we can import all of the models we want to use and create some objects:

```py
from .models import Flight, Airport

class FlightTestCase(TestCase):

    def setUp(self):

        # Create airports.
        a1 = Airport.objects.create(code="AAA", city="City A")
        a2 = Airport.objects.create(code="BBB", city="City B")

        # Create flights.
        Flight.objects.create(origin=a1, destination=a2, duration=100)
        Flight.objects.create(origin=a1, destination=a1, duration=200)
        Flight.objects.create(origin=a1, destination=a2, duration=-100)
```

Now we have setup some airports and flights, we can write some test cases just like Python unit testing:

```py
def test_departures_count(self):
    a = Airport.objects.get(code="AAA")
    self.assertEqual(a.departures.count(), 3)

def test_arrivals_count(self):
    a = Airport.objects.get(code="AAA")
    self.assertEqual(a.arrivals.count(), 1)
```

We can also test our `is_valid_flight` function:

```py
def test_valid_flight(self):
    a1 = Airport.objects.get(code="AAA")
    a2 = Airport.objects.get(code="BBB")
    f = Flight.objects.get(origin=a1, destination=a2, duration=100)
    self.assertTrue(f.is_valid_flight())

def test_invalid_flight_destination(self):
    a1 = Airport.objects.get(code="AAA")
    f = Flight.objects.get(origin=a1, destination=a1)
    self.assertFalse(f.is_valid_flight())

def test_invalid_flight_duration(self):
    a1 = Airport.objects.get(code="AAA")
    a2 = Airport.objects.get(code="BBB")
    f = Flight.objects.get(origin=a1, destination=a2, duration=-100)
    self.assertFalse(f.is_valid_flight())
```

We can run all tests by running the command `python manage.py test`. The output is similar to unit test outputs, though it also logs the creation and destruction of the testing database:

```sh
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..FF.
======================================================================
FAIL: test_invalid_flight_destination (flights.tests.FlightTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/cleggett/Documents/cs50/web_notes_files/7/django/airline/flights/tests.py", line 37, in test_invalid_flight_destination
    self.assertFalse(f.is_valid_flight())
AssertionError: True is not false

======================================================================
FAIL: test_invalid_flight_duration (flights.tests.FlightTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/cleggett/Documents/cs50/web_notes_files/7/django/airline/flights/tests.py", line 43, in test_invalid_flight_duration
    self.assertFalse(f.is_valid_flight())
AssertionError: True is not false

----------------------------------------------------------------------
Ran 5 tests in 0.018s

FAILED (failures=2)
Destroying test database for alias 'default'...
```

From the output, we see that our `is_valid_flight` function returns `true` when it should've returned `false`. If you check carefully, you might find that we made a mistake by using `or` instead of `and`:

```py
 def is_valid_flight(self):
    return self.origin != self.destination and self.duration > 0
```

Now if we run the tests again, we are able to get better results:

```sh
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.014s

OK
Destroying test database for alias 'default'...
```

### Client Testing

Aside from server testing such as how our database is behaving, we also want to test whether the client side works as intended. We can do this by creating a `Client` object which behaves like a real browser, making requests to the server. Then we can test the requests and responses:

```py
from django.test import Client, TestCase

def test_index(self):

    # Set up client to make requests
    c = Client()

    # Send get request to index page and store response
    response = c.get("/flights/")

    # Make sure status code is 200
    self.assertEqual(response.status_code, 200)

    # Make sure three flights are returned in the context
    self.assertEqual(response.context["flights"].count(), 3)

def test_valid_flight_page(self):
    a1 = Airport.objects.get(code="AAA")
    f = Flight.objects.get(origin=a1, destination=a1)

    c = Client()
    response = c.get(f"/flights/{f.id}")
    self.assertEqual(response.status_code, 200)

def test_invalid_flight_page(self):
    max_id = Flight.objects.all().aggregate(Max("id"))["id__max"]

    c = Client()
    response = c.get(f"/flights/{max_id + 1}")
    self.assertEqual(response.status_code, 404)

def test_flight_page_passengers(self):
    f = Flight.objects.get(pk=1)
    p = Passenger.objects.create(first="Alice", last="Adams")
    f.passengers.add(p)

    c = Client()
    response = c.get(f"/flights/{f.id}")
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.context["passengers"].count(), 1)

def test_flight_page_non_passengers(self):
    f = Flight.objects.get(pk=1)
    p = Passenger.objects.create(first="Alice", last="Adams")

    c = Client()
    response = c.get(f"/flights/{f.id}")
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.context["non_passengers"].count(), 1)
```

### Selenium

So far, we are testing our web application with Django and the tests are written on the server side. What if we only have access to the front-end of the web app? Let's see an example of a counter webpage:

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Counter</title>
        <script>

            // Wait for page to load
            document.addEventListener('DOMContentLoaded', () => {

                // Initialize variable to 0
                let counter = 0;

                // If increase button clicked, increase counter and change inner html
                document.querySelector('#increase').onclick = () => {
                    counter ++;
                    document.querySelector('h1').innerHTML = counter;
                }

                // If decrease button clicked, decrease counter and change inner html
                document.querySelector('#decrease').onclick = () => {
                    counter --;
                    document.querySelector('h1').innerHTML = counter;
                }
            })
        </script>
    </head>
    <body>
        <h1>0</h1>
        <button id="increase">+</button>
        <button id="decrease">-</button>
    </body>
</html>
```

There are two buttons to increase/decrease the number, and we want to test if everything works as expected. There are several existing frameworks to achieve this, one of which is [Selenium](https://www.selenium.dev/)

With Selenium, we'll be able to test the front-end with Python. Our main tool is known as a Web Driver, which will open up a web browser on your computer. Let's see an example, where we are using both `selenium` and `ChromeDriver`, so if you want to try yourself, run the commands

```sh
pip install selenium
pip install webdriver-manager
```

```py
import os
import pathlib

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Finds the Uniform Resourse Identifier of a file
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# Sets up web driver using Google chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
```

The above is all the setup we need, then we can start testing our counter application using the following commands in the Python shell

```shell
# Find the URI of our newly created file
>>> uri = file_uri("counter.html")

# Use the URI to open the web page
>>> driver.get(uri)

# Access the title of the current page
>>> driver.title
'Counter'

# Access the source code of the page
>>> driver.page_source
'<html lang="en"><head>\n        <title>Counter</title>\n        <script>\n            \n            // Wait for page to load\n            document.addEventListener(\'DOMContentLoaded\', () => {\n\n                // Initialize variable to 0\n                let counter = 0;\n\n                // If increase button clicked, increase counter and change inner html\n                document.querySelector(\'#increase\').onclick = () => {\n                    counter ++;\n                    document.querySelector(\'h1\').innerHTML = counter;\n                }\n\n                // If decrease button clicked, decrease counter and change inner html\n                document.querySelector(\'#decrease\').onclick = () => {\n                    counter --;\n                    document.querySelector(\'h1\').innerHTML = counter;\n                }\n            })\n        </script>\n    </head>\n    <body>\n        <h1>0</h1>\n        <button id="increase">+</button>\n        <button id="decrease">-</button>\n    \n</body></html>'

# Find and store the increase and decrease buttons:
>>> increase = driver.find_element_by_id("increase")
>>> decrease = driver.find_element_by_id("decrease")

# Simulate the user clicking on the two buttons
>>> increase.click()
>>> increase.click()
>>> decrease.click()

# We can even include clicks within other Python constructs:
>>> for i in range(25):
...     increase.click()
```

Like before, we prefer not to manually type all these commands in the shell to test the functionality of our web app, we want automated testing, and we can use unit test to achieve it:

In `test.py`

```py
# Basic Setup Needed Before all Test Cases

# Standard outline of testing class
class WebpageTests(unittest.TestCase):

    def test_title(self):
        """Make sure title is correct"""
        driver.get(file_uri("counter.html"))
        self.assertEqual(driver.title, "Counter")

    def test_increase(self):
        """Make sure header updated to 1 after 1 click of increase button"""
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("increase")
        increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "1")

    def test_decrease(self):
        """Make sure header updated to -1 after 1 click of decrease button"""
        driver.get(file_uri("counter.html"))
        decrease = driver.find_element_by_id("decrease")
        decrease.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "-1")

    def test_multiple_increase(self):
        """Make sure header updated to 3 after 3 clicks of increase button"""
        driver.get(file_uri("counter.html"))
        increase = driver.find_element_by_id("increase")
        for i in range(3):
            increase.click()
        self.assertEqual(driver.find_element_by_tag_name("h1").text, "3")

if __name__ == "__main__":
    unittest.main()
```

Now if we run `python test.py`, a browser will open up and do all the testing, the results will be printed to the terminal

![gif](https://cs50.harvard.edu/web/2020/notes/7/images/fail.gif)

## Continuous Integration/Delivery

CI/CD is a set of software development best practices that dictate how code is written by a team of programmers, and how the code is later delivered to users

- CI
  - Frequent merges to the main branch
  - Automated unit testing with each merge
- CD
  - Short release schedules, new versions will be released frequently

Benefits including but not bounded to:

- When a large amount of programmers working on the same project, compatiblility issues arises such that people's code doesn't always merge perfectly. CI allows teams to resolve smaller conflicts each time
- Unit testing with each merge allows programmers to isolate the part of the code that is causing the problem easily and quickly
- Frequent releasing new versions allows developers to tackle smaller bugs after each launch
- Release small, incremental changes allows users to get a taste of new features everytime rather than being overwhelmed with an entirely new version
- Shorter waiting time for each release allows company to stay ahead in the competitive market

### Github Actions

One popular tool to help with CI is [GitHub Actions](https://github.com/features/actions), which allows the Git repository to automatically run a customed test set after each push

In order to set up a GitHub action, we'll use a configuration language called YAML. YAML structures data into key-value pairs (similar to JSON & Python Dictionary)

```YAML
key1: value1
key2: value2
key3:
    - item1
    - item2
    - item3
```

To trigger GitHub actions, we'll need to create a `.github` directory in the root directory, then create a `workflows` directory inside of it, and finally a `SOMETHING.yml` file within that. In this case we'll call it `ci.yml`, in this file we write:

```YAML
name: Testing
on: push

jobs:
  test_project:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Run Django unit tests
      run: |
        pip3 install --user django
        python3 manage.py test
```

- `name`: We give our workflow a name, in this case is `Testing`
- `on`: We specify when will this workflow run, in this case, it will run everytime someone pushes to this repository
- `job`: The jobs to run on every push
- `test_project`: We give our job the name `test_porject`, we can have more jobs but in this case, we only need one. Every job must define two components
- `run-on`: Specifies which of GitHub’s virtual machines we would like our code to be run on
- `steps`: Actions that should occur
- `uses`: Specify the github action we want to use
- `name`: A description of the action we are taking
- `run`: After the run key, we type the commands we wish to run. In this case we want to install `Django` and run the tests. We need to install `Django` because we are running the job on GitHub's VM, not our local machine. If there's any other dependencies, we also need to install them first

Now if we push anything to the GitHub repository and check the GitHub webpage for that repository, click the `Actions` tab, we can see that our job is running. Wait for it to finish and we can then see the results

![gif](https://cs50.harvard.edu/web/2020/notes/7/images/action.gif)

### Docker

Modern softwares have large amount of dependencies, and problem can arise in the world of software development when the configuration on your computer is different than the one your colleage is using, maybe you are using some version of Python and Django while your co-worker is using other versions, some codes might not be compatible when working together. One way to solve this is to use a tool called Docker, which is a containerization software, much like a virtual environment, which has a set of configuration isolated from outside environments. While Docker is a bit like a Virtual Machine, they are different techhnologies. A VM (like the one we used in GitHub Actions) is an entire virtual computer with its own OS, which takes up lots of space, and it ends up taking a lot more when its running. Dockers, on the other hand, are much ligher weight

The first step to creating a Docker container is to create a Docker File, inside this file we'll provide instructions for how to create a Docker Image which describes the dependencies and configuration

```dockerfile
FROM python:3
COPY .  /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
```

- `FROM python:3`: The `FROM` keyword basically builds our Docker on top of an existing standard Docker image, allows us not having to re-define some basic setup
- `COPY . /usr/src/app`: This shows that we wish to copy everything from our current directory (`.`) and store it in the `/usr/src/app` directory in our new container
- `WORKDIR /usr/src/app`: This sets up where we will run commands within the container (A bit like `cd` on the terminal)
- `RUN pip install -r requirements.txt`: In this line, assuming you’ve included all of your requirements to a file called `requirements.txt`, they will all be installed within the container
- `CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]`: Finally, we specify the command that should be run when we start up the container

We've only used SQLite as our database so far, but it is almost never used as it's not as easily scaled as other systems. What if we want to run a separate server for our database such as MySQL or PostgreSQL? Docker allows us to have two containers and compose them with Docker Compose. Two containers run in separate servers, but are able to communicate with each other. To demonstrate Docker Compose, we'll create a YAML file called `docker-compose.yml`:

```yml
version: "3"

services:
  db:
    image: postgres

  web:
    build: .
    volumes:
      - .:/usr/src/app
    ports:
      - "8000:8000"
```

- We specify we are using version 3 of Docker Compose
- `db`: Sets up the database container based on an image written already by Postgres
- `web`: sets up our server's container by instructing Docker to:
  - Use the `Dockerfile` within the current directory
  - Use the specified path within the container
  - Use port 8000 of the container to port 8000 to our computer

Now we are ready to start up our services with the command `docker-compose up`. which will launch both servers inside of new Docker containers

If we want to run commands within the Docker container, we can use `docker ps` to show all of the docker containers that are running. Then find the `CONTAINER ID` of the container we wish to enter, then run `docker exec -it <CONTAINER ID> bash -l`. This will let you enter the `usr/src/app` path within the container. We can exit by pressing CTRL-D

## Examples

Check out some [examples](examples/)
