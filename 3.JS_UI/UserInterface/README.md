# User Interface

A User Interface is how visitors to a web page interact with that page. Our goal as web developers is to make these interactions as pleasant as possible for the user, and there are many methods we can use to do this

## Single Page Application

Previously, if we want a website with multiple pages, we would create multiple HTML templates and using different routes in a Django application. Now with the power of JavaScript, we can have a single HTML file and use JS to manipulate the DOM and creates the illusion of having multiple pages

Take a look at the following HTML:

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Single Page</title>
        <style>
            div {
                display: none;
            }
        </style>
        <script src="singlepage.js"></script>
    </head>
    <body>
        <button data-page="page1">Page 1</button>
        <button data-page="page2">Page 2</button>
        <button data-page="page3">Page 3</button>
        <div id="page1">
            <h1>This is page 1</h1>
        </div>
        <div id="page2">
            <h1>This is page 2</h1>
        </div>
        <div id="page3">
            <h1>This is page 3</h1>
        </div>
    </body>
</html>
```

Now if you open it with any browser, only there buttons will be shown and not the `div`s since they have the `display:none` property. Now what we want is when we click a button, the corresponding page should be displayed

```JS
// Shows one page and hides the other two
function showPage(page) {

    // Hide all of the divs:
    document.querySelectorAll('div').forEach(div => {
        div.style.display = 'none';
    });

    // Show the div provided in the argument
    document.querySelector(`#${page}`).style.display = 'block';
}

// Wait for page to loaded:
document.addEventListener('DOMContentLoaded', function() {

    // Select all buttons
    document.querySelectorAll('button').forEach(button => {

        // When a button is clicked, switch to that page
        button.onclick = function() {
            showPage(this.dataset.page);
        }
    })
});
```

![gif](https://cs50.harvard.edu/web/2020/notes/6/images/singlepage1.gif)

#### Our Own API

In many cases, it is unrealistic to load everything when we first visit a webpage since it will take too long. Common times, we'll need a server to access data when needed. We'll see how to use Django as our own API and use JS to request data from it in the previous one page application

In the `urls.py`:

```py
urlpatterns = [
    path("", views.index, name="index"),
    path("sections/<int:num>", views.section, name="section")
]
```

And in `views.py`:

```py
from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

# The texts are much longer in reality, but have
# been shortened here to save space
texts = ["Text 1", "Text 2", "Text 3"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")
```

Now in `index.html`, we take advantage of AJAX, to make a request to our own server to get the data and display it on the screen:

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Single Page</title>
        <style>
        </style>
        <script>

            // Shows given section
            function showSection(section) {

                // Find section text from server
                fetch(`/sections/${section}`)
                .then(response => response.text())
                .then(text => {
                    // Log text and display on page
                    console.log(text);
                    document.querySelector('#content').innerHTML = text;
                });
            }

            document.addEventListener('DOMContentLoaded', function() {
                // Add button functionality
                document.querySelectorAll('button').forEach(button => {
                    button.onclick = function() {
                        showSection(this.dataset.section);
                    };
                });
            });
        </script>
    </head>
    <body>
        <h1>Hello!</h1>
        <button data-section="1">Section 1</button>
        <button data-section="2">Section 2</button>
        <button data-section="3">Section 3</button>
        <div id="content">
        </div>
    </body>
</html>
```

![gif](https://cs50.harvard.edu/web/2020/notes/6/images/singlepage2.gif)

#### Manual URL & Browsing History

One disadvantage of this site is that the URL is less informative and if you noticed, the URL is not even changing since we are essentially on the same page. We can solve this problem by using the [JavaScript History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API). This API enables us to update the URL manually

```JS
// When back arrow is clicked, show previous section
window.onpopstate = function(event) {
    console.log(event.state.section);
    showSection(event.state.section);
}

function showSection(section) {
    fetch(`/sections/${section}`)
    .then(response => response.text())
    .then(text => {
        console.log(text);
        document.querySelector('#content').innerHTML = text;
    });

}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {
            const section = this.dataset.section;

            // Add the current state to the history
            history.pushState({section: section}, "", `section${section}`);
            showSection(section);
        };
    });
});
```

Notice the `history.pushState` function, which will add a new element to the browsing history based on three arguments:

1. Data associated with the state
2. A title parameter which is commonly an empty string `""`
3. What should be displayed in the URL

![gif](https://cs50.harvard.edu/web/2020/notes/6/images/singlepage3.gif)

### Scroll

In the last example, we used an important JS object known as the [`window`](https://www.w3schools.com/js/js_window.asp). The window not only can access and update browser history, it also has some important properties that we can take advantage of to make our user interface more attractive and interactive

- `window.innerWidth`: Width of window in pixels
- `window.innerHeight`: Height of window in pixels

![window](https://cs50.harvard.edu/web/2020/notes/6/images/innerMeasures.png)

While the window represents what is visible to the users, the [`document`](https://www.w3schools.com/js/js_htmldom_document.asp) refers to the entire DOM, which can be much larger than the visible window so the users will need to scroll through it

- `window.scrollY`: How many pixels we have scrolled from the top of the page
- `document.body.offsetHeight`: The height in pixels of the entire document

![scroll](https://cs50.harvard.edu/web/2020/notes/6/images/scroll.png)

We can take advantage of these properties and make our UI responsive to scrolling. For example, we can calculate if the user has scrolled to the end of a page using

`window.scrollY + window.innerHeight >= document.body.offsetHeight`

And an example program to turn the background to green if the user has scrolled the end of the page:

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Scroll</title>
        <script>

            // Event listener for scrolling
            window.onscroll = () => {

                // Check if we're at the bottom
                if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {

                    // Change color to green
                    document.querySelector('body').style.background = 'green';
                } else {

                    // Change color to white
                    document.querySelector('body').style.background = 'white';
                }
            };
        </script>
    </head>
    <body>
        <p>1</p>
        <p>2</p>
        <!-- More paragraphs left out to save space -->
        <p>99</p>
        <p>100</p>
    </body>
</html>
```

![gif](https://cs50.harvard.edu/web/2020/notes/6/images/scrollgreen.gif)

#### Infinite Scroll

Now we've seen that we can check if users have scrolled to the very end, but changing the background color does not seem that useful. Think about some social media, where you can see some posts, and when you scroll to the very bottom, more posts will be loaded. This can be done using this exact method

In `urls.py`

```py
urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts")
]
```

In `views.py`

```py
import time

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "posts/index.html")

def posts(request):

    # Get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    # Generate list of posts
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    # Artificially delay speed of response
    time.sleep(1)

    # Return list of posts
    return JsonResponse({
        "posts": data
    })
```

In this view, we've created our own API to generate some example posts that only says "Post #n"

Now if we visit the URL `localhost:8000/posts?start=10&end=15`, it will return the following JSON:

```JSON
{
    "posts": [
        "Post #10",
        "Post #11",
        "Post #12",
        "Post #13",
        "Post #14",
        "Post #15"
    ]
}
```

In the `index.html` template:

```HTML
{% load static %}
<!DOCTYPE html>
<html>
    <head>
        <title>My Webpage</title>
        <style>
            .post {
                background-color: #77dd11;
                padding: 20px;
                margin: 10px;
            }

            body {
                padding-bottom: 50px;
            }
        </style>
        <script scr="{% static 'posts/script.js' %}"></script>
    </head>
    <body>
        <div id="posts">
        </div>
    </body>
</html>
```

In the `script.js` file, we check if the user has scrolled to the bottom of the page, and if so, we will make a request to our server to get the next 20 posts then display them

```JS
// Start with first post
let counter = 1;

// Load posts 20 at a time
const quantity = 20;

// When DOM loads, render the first 20 posts
document.addEventListener('DOMContentLoaded', load);

// If scrolled to bottom, load the next 20 posts
window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
};

// Load next set of posts
function load() {

    // Set start and end post numbers, and update counter
    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;

    // Get new posts and add posts
    fetch(`/posts?start=${start}&end=${end}`)
    .then(response => response.json())
    .then(data => {
        data.posts.forEach(add_post);
    })
};

// Add a new post with given contents to DOM
function add_post(contents) {

    // Create new post
    const post = document.createElement('div');
    post.className = 'post';
    post.innerHTML = contents;

    // Add post to DOM
    document.querySelector('#posts').append(post);
};
```

![gif](https://cs50.harvard.edu/web/2020/notes/6/images/infscroll.gif)

## Animation
