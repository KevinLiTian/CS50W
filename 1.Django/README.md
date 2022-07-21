# Django

Previously using HTML and CSS, we were able to create a static webpage. Static means that everytime one visits that webpage, everything will look exactly the same; however, that's not the case for most websites. Most websites changes over time with new informations, but how did they achieve that? Someone is constantly changing the HTML? Not likely. This process involves backend development, and Django allows us to use Python to create a backend that dynamically changes HTML and CSS

## HTTP

To understand how a backend works, we have to first understand what is a [Hypertext Transfer Protocol (HTTP)](https://developer.mozilla.org/en-US/docs/Web/HTTP). HTTP is a widely-accepted protocol for how messages are transfered back and forth across the internet. Typically, information online is passed between a client (user) and a server. The client sends some request to view a website and the server sends the HTML and CSS for that website so that the client's browser can render those files and display the webpage

![server_client](https://user-images.githubusercontent.com/99038613/178368862-907bb958-f8e3-46ea-b126-c02dc33427fd.jpg)

The request can be of various types. Common ones are `GET` and `POST`. `GET` request appears everyday when one is browsing the internet, it basically means to ask the server for permission of viewing a website. `POST` on the other hand is when the user enters some information in, for example, an HTML form, then sending the information to the server

Requests are sent from the client to the server, and the server will reply or response. The response is usually some status code

<img src="https://user-images.githubusercontent.com/99038613/178368869-8c76842f-be55-4a42-a1fb-337e421ae134.jpg" width=60%>

- **Status code 200**: The request is permitted and the HTML and CSS files are rendered by the clinet's browser to display the website
- **Status code 301**: The website has moved to another URL permanently
- **Status code 403**: The client sending the request should not have the permission to view the website
- **Status code 404**: The website at the URL is not found
- **Status code 500**: The website itself has some bug in it

## Django Features

Django is a web framework in Python that allows us to create a backend where the data can be stored, manipulated and also serve as a server to respond to client requests

- To get started, we’ll have to install Django, which means you’ll also have to [install pip](https://pip.pypa.io/en/stable/installation/) if you haven’t already done so
- Once you have Pip installed, you can run `pip3 install Django` in your terminal to install Django

#### Creating a Django Project

After installing Django, we can go through the steps of creating a new Django project:

1. Run `django-admin startproject PROJECT_NAME` to create a number of starter files for our project. Then run `cd PROJECT_NAME` to navigate into your new project’s directory
2. Open the directory in your text editor of choice. You’ll notice that some files have been created for you. We won’t need to look at most of these for now, but there are three that will be very important from the start:
   - `manage.py` is what we use to execute commands on our terminal. We won’t have to edit it, but we’ll use it often
   - `settings.py` contains some important configuration settings for our new project. There are some default settings, but we may wish to change some of them from time to time
   - `urls.py` contains directions for where users should be routed after navigating to a certain URL
3. Start the project by running `python manage.py runserver`. This will open a development server, which you can access by visiting the URL provided. This development server is being run locally on your machine, meaning other people cannot access your website. This should bring you to a default landing page:

   ![DefaultPage](https://user-images.githubusercontent.com/99038613/178370083-bb07982f-9307-472d-8a22-90997b37ffbb.jpg)

4. Next, we’ll have to create an application. Django projects are split into one or more applications. Most of our projects will only require one application, but larger sites can make use of this ability to split a site into multiple apps. To create an application, we run `python manage.py startapp APP_NAME`. This will create some additional directories and files that will be useful shortly, including `views.py`
5. Now, we have to install our new app. To do this, we go to `settings.py`, scroll down to the list of `INSTALLED_APPS`, and add the name of our new application to this list

<img src="https://user-images.githubusercontent.com/99038613/178370096-7945c8bf-7a68-4caf-8e86-47df16042920.jpg" width=60%>

#### Routes

Now, in order to get started with our application:

1. Next, we’ll navigate to `views.py`. This file will contain a number of different views, and we can think of a view for now as one page the user might like to see. To create our first view, we’ll write a function that takes in a `request`. For now, we’ll simply return an `HttpResponse` (A very simple response that includes a response code of 200 and a string of text that can be displayed in a web browser) of “Hello, World”. In order to do this, we have include `from django.http import HttpResponse`. Our file now looks like:

   ```Python
   from django.shortcuts import render
   from django.http import HttpResponse

   # Create your views here.

   def index(request):
       return HttpResponse("Hello, world!")
   ```

2. Now, we need to somehow associate this view we have just created with a specific URL. To do this, we’ll create another file called `urls.py` in the same directory as `views.py`. We already have a `urls.py` file for the whole project, but it is best to have a separate one for each individual app

3. Inside our new urls.py, we’ll create a list of url patterns that a user might visit while using our website. In order to do this:

   1. We have to make some imports: `from django.urls import path` will give us the ability to reroute URLSs, and `from . import views` will import any functions we’ve created in `views.py`
   2. Create a list called `urlpatterns`. For each desired URL, add an item to the `urlpatterns` list that contains a call to the `path` function with two or three arguments: A string representing the URL path, a function from `views.py` that we wish to call when that URL is visited, and (optionally) a name for that path, in the format `name="something"`. For example, here’s what our simple app looks like now:

      ```Python
      from django.urls import path
      from . import views

      urlpatterns = [
          path("", views.index, name="index")
      ]
      ```

      The `""`, first argument of the `path` function indicates that if the URL is just `localhost:8000/myapp`, then use the `index` function in `views.py`

   3. Now, we’ve created a `urls.py` for this specific application, and it’s time to edit the `urls.py` created for us for the entire project. When you open this file, you should see that there’s already a path called `admin` which we’ll go over later. We want to add another path for our new app, so we’ll add an item to the `urlpatterns` list. This follows the same pattern as our earlier paths, except instead of adding a function from `views.py` as our second argument, we want to be able to include all of the paths from the `urls.py` file within our application. To do this, we write: `include("APP_NAME.urls")`, where `include` is a function we gain access to by using also importing `from django.urls import include` as shown in the urls.py below:

      ```Python
      from django.contrib import admin
      from django.urls import path, include

      urlpatterns = [
          path('admin/', admin.site.urls),
          path('myapp/', include("myapp.urls"))
      ]
      ```

Now, when initiating the server using `python manage.py runserver` and visit the URL `localhost:8000/myapp`, the webpage should look like this:

![1](https://user-images.githubusercontent.com/99038613/178374363-14526742-579f-40e5-8e7b-f5561afe156b.jpg)

Now that we’ve had some success, let’s go over what just happened to get us to that point:

1. When we accessed the URL `localhost:8000/hello/`, Django looked at what came after the base URL (`localhost:8000/`) and went to our project’s `urls.py` file and searched for a pattern that matched `hello`
2. It found that extension because we defined it, and saw that when met with that extension, it should `include` our `urls.py` file from within our application
3. Then, Django ignored the parts of the URL it has already used in rerouting (`localhost:8000/hello/`, or all of it) and looked inside our other `urls.py` file for a pattern that matches the remaining part of the URL
4. It found that our only path so far (`""`) matched what was left of the URL, and so it directed us to the function from `views.py` associated with that path
5. Finally, Django ran that function within `views.py`, and returned the result (`HttpResponse("Hello, world!")`) to our web browser

Now, if we want to, we can change the index function within views.py to return anything we want it to! We could even keep track of variables and do calculations within the function before eventually returning something

Also, we can add more functions inside `views.py` to display differently when the URL is different

```Python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")

def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse("Hello, David!")
```

Inside urls.py (within our application):

```Python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("brian", views.brian, name="brian"),
    path("david", views.david, name="david")
]
```

So when the URL is `localhost:8000/hello/brian`, the webpage will show "Hello, Brian!" or when the URL is `localhost:8000/hello/david`, the webpage will show "Hello, David!"

However, this shortly gets tedious when there's hundreds of names or even thousands. It's not a good design and also not possible to hard code thousands of functions and link them to thousands of URLs. Django provides a feature that allows us to parameterize variables. For example, let's create a general function called `greet` in `views.py`:

```Python
def greet(request, name):
    return HttpResponse(f"Hello, {name}!")
```

This function takes in one more parameter `name` and pass into the HttpResponse as a formatting string. Then in the `urls.py`, the `path` will look like:

`path("<str:name>", views.greet, name="greet")`

By using `<>`, the end part of the URL will be passed as a `name` variable into the `greet` function and it will return an HttpResponse which renders the page with "Hello, {name}"

#### Templates

So far, our HTTP Responses, have been only text, but we can include any HTML elements we want to! For example, I could decide to return a blue header instead of just the text in our index function:

```Python
def index(request):
    return HttpResponse("<h1 style=\"color:blue\">Hello, world!</h1>")
```

But it would get very tedious to write an entire HTML page within a function. It would also constitute bad design since sometimes there are a group of people working on backend, Python, for example, and others working on frontend, HTML and CSS. We want to separate the work for each of them to avoid problems

This is why we’ll now introduce [Django’s templates](https://docs.djangoproject.com/en/4.0/topics/templates/), which will allow us to write HTML and CSS in separate files and render those files using Django. The syntax we’ll use for rendering a template looks like this:

```Python
def index(request):
    return render(request, "hello/index.html")
```

Now, we’ll need to create that template. To do this, we’ll create a folder called templates inside our app, then create a folder called `hello` (or whatever our app’s name is) within that, and then add a file called `index.html`

![files](https://user-images.githubusercontent.com/99038613/178374885-7f477a7c-34f4-4246-835c-52fe2e730279.jpg)

Next, we’ll add whatever we want to that new file:

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
    </body>
</html>
```

Now, when we visit the main page of our application, we can see the header and title have been updated:

<img src="https://user-images.githubusercontent.com/99038613/178374894-5f3d6dc9-330a-4e53-ba4a-fd23064f7c2f.jpg" width=60%>

In addition to writing some static HTML pages, we can also use [Django’s templating language](https://docs.djangoproject.com/en/4.0/ref/templates/language/) to change the content of our HTML files based on the URL visited. Let’s try it out by changing our `greet` function from earlier:

```Python
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize() # Capitalize the first character
    })
```

Notice that we passed a third argument into the `render` function here, one that is known as the context. In this context, we can provide information that we would like to have available within our HTML files. This context takes the form of a Python dictionary. Now, we can create a `greet.html` file:

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello</title>
    </head>
    <body>
        <h1>Hello, {{ name }}!</h1>
    </body>
</html>
```

You’ll noticed that we used some new syntax: `{{}}`. This syntax allows us to access variables that we’ve provided in the context argument. Now, when we try it out:

![examples](https://user-images.githubusercontent.com/99038613/178376233-e9117430-f262-4029-af14-735412e32121.jpg)

Now, we’ve seen how we can modify our HTML templates based on the context we provide. However, the Django templating language is even more powerful than that, so let’s take a look at a few other ways it can be helpful

#### Conditionals

We may want to change what is displayed on our website depending on some conditions. For example, if you visit the site www.isitchristmas.com, you’ll probably be met with a page that looks like this:

<img src="https://user-images.githubusercontent.com/99038613/178376245-d56baae2-d696-4168-8172-8bde5ce9019a.jpg" width=60%>

But this website will change on Christmas day, when the website will say YES. To make something like this for ourselves, let’s try creating a similar application, where we check whether or not it is New Year’s Day. Let’s create a new app to do so, recalling our process for creating a new app:

1. Run `python manage.py startapp newyear` in the terminal
2. Edit `settings.py`, adding “newyear” as one of our `INSTALLED_APPS`
3. Edit our project’s `urls.py` file, and include a path similar to the one we created for the `hello` app:

   `path('newyear/', include("newyear.urls"))`

4. Create another `urls.py` file within our new app’s directory, and update it to include a path similar to the index path in `hello`:

   ```Python
   from django.urls import path
   from . import views

   urlpatterns = [
       path("", views.index, name="index"),
   ]
   ```

5. Lastly, Create an `index` function in `views.py`

Now that we’re set up with our new app, let’s figure out how to check whether or not it’s New Year’s Day. To do this, we can import Python’s [datetime](https://docs.python.org/3/library/datetime.html) module

In the `index` function in `views.py`:

```Python
import datatime

def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })
```

Now, let’s create our `index.html` template. We’ll have to again create a new folder called `templates`, a folder within that called `newyear`, and a file within that called `index.html`. Inside that file, we’ll write something like this:

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Is it New Year's?</title>
    </head>
    <body>
        {% if newyear %}
            <h1>YES</h1>
        {% else %}
            <h1>NO</h1>
        {% endif %}
    </body>
</html>
```

In the code above, notice that when we wish to include logic in our HTML files, we use `{%` and `%}` as opening and closing tags around logical statements. Also note that Django’s formatting language requires you to include an `{% endif %}` tag indicating that we are done with our if-else block. Now, we can open up to our page to see:

<img src="https://user-images.githubusercontent.com/99038613/178376256-4340536a-5512-4ae6-aeeb-2154f1e6c4b1.jpg" width=60%>

#### Styling

If we want to add a CSS file, which is a static file because it doesn’t change, we’ll first create a folder called `static` in the application, then create a `newyear` folder within that, and then a `styles.css` file within that. In this file, we can add any styling we wish:

```CSS
h1 {
    font-family: sans-serif;
    font-size: 90px;
    text-align: center;
}
```

Now, to include this styling in our HTML file, we add the line `{% load static %}` to the top of our HTML template, which signals to Django that we wish to have access to the files in our `static` folder. Then, rather than hard-coding the exact path to a stylesheet as we did before, we’ll use some Django-specific syntax:

`<link rel="stylesheet" href="{% static 'newyear/styles.css' %}">`

Now, if we restart the server, we can see that the styling changes were in fact applied:

<img src="https://user-images.githubusercontent.com/99038613/178379780-be99f712-23df-4406-ab09-ed97253499c5.jpg" width=60%>

## TODO List

Now, let’s take what we’ve learned so far and apply it to a mini-project: creating a TODO list. Let’s start by, once again, creating a new app:

1. Run `python manage.py startapp tasks` in the terminal
2. Edit `settings.py`, adding “tasks” as one of our `INSTALLED_APPS`
3. Edit our project’s `urls.py` file, and include a path similar to the one we created for the `hello` app:

   `path('tasks/', include("tasks.urls"))`

4. Create another `urls.py` file within our new app’s directory, and update it to include a path similar to the index path in `hello`:

   ```Python
   from django.urls import path
   from . import views

   urlpatterns = [
       path("", views.index, name="index"),
   ]
   ```

5. Create an `index` function in `views.py`

Now, let’s begin by attempting to simply create a list of tasks and then display them to a page. Let’s create a Python list at the top of `views.py` where we’ll store our tasks. Then, we can update our `index` function to render a template, and provide our newly-created list as context.

```Python
from django.shortcuts import render

tasks = ["foo", "bar", "baz"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
```

Now, let’s work on creating our template HTML file:

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Tasks</title>
    </head>
    <body>
        <ul>
            {% for task in tasks %}
                <li>{{ task }}</li>
            {% endfor %}
        </ul>
    </body>
</html>
```

Notice here that we are able to loop over our tasks using syntax similar to our conditionals from earlier, and also similar to a Python loop. When we go to the tasks page now, we can see our list being rendered:

<img src="https://user-images.githubusercontent.com/99038613/178379794-66b874c6-52cd-4b10-aa3d-759a6b2aa00b.jpg" width=60%>

#### Forms

Now that we can see all of our current tasks as a list, we may want to be able to add some new tasks. To do this we’ll start taking a look at using forms to update a web page. Let’s begin by adding another function to `views.py` that will render a page with a form for adding a new task:

```Python
# Add a new task:
def add(request):
    return render(request, "tasks/add.html")
```

Next, make sure to add another path to `urls.py`:

`path("add", views.add, name="add")`

Now, we’ll create our `add.html` file, which is fairly similar to `index.html`, except that in the body we’ll include a form rather than a list:

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Tasks</title>
    </head>
    <body>
        <h1>Add Task:</h1>
        <form action="">
            <input type="text", name="task">
            <input type="submit">
        </form>
    </body>
</html>
```

However, what we’ve just done isn’t necessarily the best design, as we’ve just repeated the bulk of that HTML in two different files. Django’s templating language gives us a way to eliminate this poor design: [template inheritance](https://tutorial.djangogirls.org/en/template_extending/). This allows us to create a `layout.html` file that will contain the general structure of our page:

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Tasks</title>
    </head>
    <body>
        {% block body %}
        {% endblock %}
    </body>
</html>
```

Notice that we’ve again used `{%...%}` to denote some sort of non-HTML logic, and in this case, we’re telling Django to fill this “block” with some text from another file. Now, we can alter our other two HTML files to look like:

In `index.html`:

```HTML
{% extends "tasks/layout.html" %}

{% block body %}
    <h1>Tasks:</h1>
    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

And in `add.html`

```HTML
{% extends "tasks/layout.html" %}

{% block body %}
    <h1>Add Task:</h1>
    <form action="">
        <input type="text", name="task">
        <input type="submit">
    </form>
{% endblock %}
```

Notice how we can now get rid of much of the repeated code by extending our layout file. Now, our index page remains the same, and we now have an add page as well:

<img src="https://user-images.githubusercontent.com/99038613/178379804-72202cac-a062-4ade-bb1e-a2b4ba7a34b4.jpg" width=60%>

Next, it’s not ideal to have to type “/add” in the URL any time we want to add a new task, so we’ll probably want to add some links between pages. Instead of hard-coding links though, we can now use the `name` variable we assigned to each path in `urls.py`, and create a link that looks like this:

`<a href="{% url 'add' %}">Add a New Task</a>`

where ‘add’ is the name of that path. We can do a similar thing in our `add.html`:

`<a href="{% url 'index' %}">View Tasks</a>`

This could potentially create a problem though, as we have a few routes named `index` throughout our different apps. We can solve this by going into each of our app’s `urls.py` file, and adding an `app_name` variable, so that the files now look something like this:

```Python
from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]
```

Then for the links:

```HTML
<a href="{% url 'tasks:index' %}">View Tasks</a>
<a href="{% url 'tasks:add' %}">Add a New Task</a>
```

Now, let’s work on making sure the form actually does something when the user submits it. We can do this by adding an `action` to the form we have created in `add.html`:

`<form action="{% url 'tasks:add' %}" method="post">`

And to prevent [Cross-Site Request Forgery (CSRF) Attack](https://portswigger.net/web-security/csrf), we must add a CSRF token in the form which serves as an identifier:

```HTML
<form action="{% url 'tasks:add' %}" method="post">
    {% csrf_token %}
    <input type="text", name="task">
    <input type="submit">
</form>
```

#### Django Forms

While we can create forms by writing raw HTML as we’ve just done, Django provides an even easier way to collect information from a user: [Django Forms](https://docs.djangoproject.com/en/4.0/ref/forms/api/). In order to use this method, we’ll add the following to the top of `views.py` to import the `forms` module:

`from django import forms`

Now, we can create a new form within `views.py` by creating a Python class called `NewTaskForm` that inherits from Django forms:

```Python
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
```

Now that we’ve created a `NewTaskForm` class, we can include it in the context while rendering the `add` page:

```Python
# Add a new task:
def add(request):
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
```

Now, within `add.html`, we can replace our input field with the form we just created:

```HTML
{% extends "tasks/layout.html" %}

{% block body %}
    <h1>Add Task:</h1>
    <form action="{% url 'tasks:add' %}" method="post">
        {% csrf_token %}
        {{ form }}
        <input type="submit">
    </form>
    <a href="{% url 'tasks:index' %}">View Tasks</a>
{% endblock %}
```

There are several advantages to using the `forms` module rather than manually writing an HTML form:

- If we want to add new fields to the form, we can simply add them in views.py without typing additional HTML
- Django automatically performs [client-side validation](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation)
- Django provides simple [server-side validation](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation)

Now that we have a form set up, let’s work on what happens when a user clicks the submit button. When a user navigates to the add page by clicking a link or typing in the URL, they submit a `GET` request to the server, which we’ve already handled in our `add` function. When a user submits a form though, they send a `POST` request to the server, which at the moment is not handled in the `add` function. We can handle a `POST` method by adding a condition based on the request argument our function takes in. The comments in the code below explain the purpose of each line:

```Python
# Add a new task:
def add(request):

    # Check if method is POST
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = NewTaskForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            task = form.cleaned_data["task"]

            # Add the new task to our list of tasks
            tasks.append(task)

            # Redirect user to list of tasks
            return redirect("tasks:index")

        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
```

A quick note: in order to redirect the user after a successful submission, we need a few more imports:

```Python
from django.urls import reverse
from django.shortcuts import redirect
```

#### Sessions

At this point, the TODO list is working as it load additional user input tasks and render on the webpage; however, it is problematic to store the task list as a gloabl variable inside `views.py`. Because it means that all of the users who visit this page will see the exact same list of TODOs, which is not what we want in this case. In order to solve this problem, we introduce [sessions](https://docs.djangoproject.com/en/4.0/topics/http/sessions/)

Sessions are a way to store unique data on the server side for each client. To use sessions in our application, we’ll first delete our global `tasks` variable, then alter our `index` function, and finally make sure that anywhere else we had used the variable `tasks`, we replace it with `request.session["tasks"]`

```Python
def index(request):
    # Check if there already exists a "tasks" key in current session
    if "tasks" not in request.session:

        # If not, create a new list
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

# Add a new task:
def add(request):
    if request.method == "POST":
        # Take in the data the user submitted and save it as form
        form = NewTaskForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            task = form.cleaned_data["task"]

            # Add the new task to our list of tasks
            request.session["tasks"] += [task]

            # Redirect user to list of tasks
            return redirect("tasks:index")
        else:

            # If the form is invalid, re-render the page with existing information.
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
```

In order to store the session data, we must first run the command `python manage.py migrate` in the terminal

## Examples

Check out some [examples](examples/)
