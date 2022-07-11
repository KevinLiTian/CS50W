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

Figure 1

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

Now, we’ll need to create that template. To do this, we’ll create a folder called templates inside our app, then create a folder called hello (or whatever our app’s name is) within that, and then add a file called index.html

Figure 1

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

Figure 2

