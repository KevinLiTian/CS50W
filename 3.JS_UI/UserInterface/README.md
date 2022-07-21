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

We can also make our website more interesting by adding some animation to it. CSS makes it easy for us to animate HTML elements

To create an animation with CSS, we need to define some key frames:

```CSS
@keyframes animation_name {
    from {
        /* Some styling for the start */
    }

    to {
        /* Some styling for the end */
    }
}

@keyframes animation_name {
    0% {
        /* Some styling for the start */
    }

    75% {
        /* Some styling after 3/4 of animation */
    }

    100% {
        /* Some styling for the end */
    }
}
```

Then to apply animation to HTML element, we include the `animation-name`, `animation-duration` and `animation-fill-mode` (typically `forwards`)

```CSS
@keyframes grow {
    from {
        font-size: 20px;
    }
    to {
        font-size: 100px;
    }
 }

h1 {
    animation-name: grow;
    animation-duration: 2s;
    animation-fill-mode: forwards;
}
```

![gif](https://cs50.harvard.edu/web/2020/notes/6/images/animate0.gif)

We can do more than just manipulating the font size, we can animate any CSS properties such as position:

```CSS
@keyframes move {
    from {
        left: 0%;
    }
    to {
        left: 50%;
    }
}

h1 {
    position: relative;
    animation-name: move;
    animation-duration: 2s;
    animation-fill-mode: forwards;
}
```

![gif](https://cs50.harvard.edu/web/2020/notes/6/images/animate1.gif)

We don't always to have use `from` and `to` to indicate the start and end, we can also use percentage:

```CSS
@keyframes move {
    0% {
        left: 0%;
    }
    50% {
        left: 50%;
    }
    100% {
        left: 0%;
    }
}
```

![gif](https://cs50.harvard.edu/web/2020/notes/6/images/animate2.gif)

Animation doesn't have to run only once, we can control the number of times the animation should run by using `animation-iteration-count`, we can even have an infinite animation by setting it to `infinite`

Moreover, we can use JavaScript to control the animation since JS is able to manipulate the DOM:

```JS
document.addEventListener('DOMContentLoaded', function() {

    // Find heading
    const h1 = document.querySelector('h1');

    // Pause Animation by default
    h1.style.animationPlayState = 'paused';

    // Wait for button to be clicked
    document.querySelector('button').onclick = () => {

        // If animation is currently paused, begin playing it
        if (h1.style.animationPlayState == 'paused') {
            h1.style.animationPlayState = 'running';
        }

        // Otherwise, pause the animation
        else {
            h1.style.animationPlayState = 'paused';
        }
    }
})
```

![gif](https://cs50.harvard.edu/web/2020/notes/6/images/animate4.gif)

Now let's see how we can apply this animation to the [social media posts](#infinite-scroll) example to make the user experience more pleasant

Now we wish to add a functionality such that the user is able hide certain posts by clicking a hide button. We can use a simple JS to achieve it:

```JS
// If hide button is clicked, delete the post
document.addEventListener('click', event => {

    // Find what was clicked on
    const element = event.target;

    // Check if the user clicked on a hide button
    if (element.className === 'hide') {
        element.parentElement.remove()
    }
});
```

![gif](https://cs50.harvard.edu/web/2020/notes/6/images/hide0.gif)

But if you don't look carefully, you can't even notice that a post disappeared since all the posts look the same and the next post move up immediately to fill in the spot of the disappearing post. If there's an animation to better show the process of hiding a post, the user experience will be much more pleasant

```CSS
@keyframes hide {
    0% {
        opacity: 1;
        height: 100%;
        line-height: 100%;
        padding: 20px;
        margin-bottom: 10px;
    }
    75% {
        opacity: 0;
        height: 100%;
        line-height: 100%;
        padding: 20px;
        margin-bottom: 10px;
    }
    100% {
        opacity: 0;
        height: 0px;
        line-height: 0px;
        padding: 0px;
        margin-bottom: 0px;
    }
}

.post {
    background-color: #77dd11;
    padding: 20px;
    margin-bottom: 10px;
    animation-name: hide;
    animation-duration: 2s;
    animation-fill-mode: forwards;
    animation-play-state: paused;
}
```

Then we modify our JavaScript to play the animation

```JS
// If hide button is clicked, delete the post
document.addEventListener('click', event => {

    // Find what was clicked on
    const element = event.target;

    // Check if the user clicked on a hide button
    if (element.className === 'hide') {
        element.parentElement.style.animationPlayState = 'running';
        element.parentElement.addEventListener('animationend', () => {
            element.parentElement.remove();
        });
    }
});
```

![gif](https://cs50.harvard.edu/web/2020/notes/6/images/hide1.gif)

## ReactJS

Writing JavaScript code is fairly complicated as you've seen so far, as a simple functionality requires quite a bit of JS code. Therefore, just like we can use Bootstrap as a CSS framework, we can use a JavaScript framework to write JS more efficiently. One of the most popular JS frameworks is a library called [React](https://reactjs.org/)

Just to demonstrate how powerful React is, see the below example to incrementing a number:

```JS
// Vanilla JavaScript
<h1>0</h1>

let num = parseInt(document.querySelector("h1").innerHTML);
num += 1;
document.querySelector("h1").innerHTML = num;

// ReactJS
<h1>{num}</h1>

num+=1
```

There are a number of ways to use ReactJS like the popular [create-react-app](https://reactjs.org/docs/create-a-new-react-app.html) command, but now we'll focus on using React in an HTML file. We'll include three JS Packages:

- `React`: ReactJS itself, defines components and their behaviors
- `ReactDOM`: Take React components and add to the DOM
- `Babel`: ReactJS is written in [JSX](https://reactjs.org/docs/introducing-jsx.html), which is slightly different from JS, so we'll need to use `Babel` to translate it into JS for the browser to understand

JSX is a superset of JS, with some additional features such as representing HTML inside of JS code. Let's see how it works via out first React application:

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <script src="https://unpkg.com/react@17/umd/react.production.min.js" crossorigin></script>
        <script src="https://unpkg.com/react-dom@17/umd/react-dom.production.min.js" crossorigin></script>
        <script src="https://unpkg.com/babel-standalone@6/babel.min.js"></script>
        <title>Hello</title>
    </head>
    <body>
        <div id="app"></div>

        <script type="text/babel">
            function App() {
                return (
                    <div>
                        Hello!
                    </div>
                );
            }

            ReactDOM.render(<App />, document.querySelector("#app"));
        </script>
    </body>
</html>
```

- In the head section, we include the three JS packages
- In the `script` tag, we use `type="text/babel"` to translate the script block into JS
- Then inside function `App`, we return an HTML representation which is being rendered using `ReactDOM`
- The `render` function takes in something to render and in this case is our `App` function, and a place to render it which is inside of the `div` with id `app`

![img](https://cs50.harvard.edu/web/2020/notes/6/images/react0.png)

React also supports rendering components within components:

```JSX
function Hello(props) {
    return (
        <h1>Hello, {props.name}!</h1>
    );
}

function App() {
    return (
        <div>
            <Hello name="Harry" />
            <Hello name="Ron" />
            <Hello name="Hermione" />
        </div>
    );
}
```

We can see that the function `App` renders the function `Hello` using HTML element like syntax. And notice that we can also pass in parameters and use `props.parameter_name` to access the parameter

![img](https://cs50.harvard.edu/web/2020/notes/6/images/react2.png)

#### useState

React has lots of hooks that we can take advantage of, one of them is `useState` which records and updates some sort of states. We can use it to create a simple math addition game

- `num1`: The first number to be added
- `num2`: The second number to be added
- `response`: User input
- `score`: User score

Now we can use `useState` to initialize these variables

```JSX
const [state, setState] = React.useState({
    num1: 1,
    num2: 1,
    response: "",
    score: 0
});
```

Then we can render a basic UI

```JSX
return (
    <div>
        <div>{state.num1} + {state.num2}</div>
        <input value={state.response} />
        <div>Score: {state.score}</div>
    </div>
);
```

![img](https://cs50.harvard.edu/web/2020/notes/6/images/add0.png)

Not the user cannot type anything in the input box since its value is fixed as `{state.response}` which is an empty string. We will add an `onChange` attribute to the input element and link it with a function to update both the state and the input box:

```JSX
<input onChange={updateResponse} value={state.response} />

function updateResponse(event) {
    setState({
        ...state,
        response: event.target.value
    });
}
```

We use `...state` to indicate that all other states remain the same

Then we need a way for the users to submit their answer, maybe by simply pressing the "enter" key. We'll add an event listener for this event:

```JSX
 <input onKeyPress={inputKeyPress} onChange={updateResponse} value={state.response} />

function inputKeyPress(event) {
    if (event.key === "Enter") {
        const answer = parseInt(state.response);
        if (answer === state.num1 + state.num2) {
            // User got question right
            setState({
                ...state,
                score: state.score + 1,
                response: "", // Empty the input box
                // Randomly generate 2 integers
                num1: Math.ceil(Math.random() * 10),
                num2: Math.ceil(Math.random() * 10)
            });
        } else {
            // User got question wrong
            setState({
                ...state,
                score: state.score - 1,
                response: "" // Empty the input box
            })
        }
    }
}

if (state.score === 10) {
    return (
        <div id="winner">You won!</div>
    );
}

```

Now that the main functionality has been implemented, we can add some simple styling to make the webpage more appealing

```CSS
#app {
    text-align: center;
    font-family: sans-serif;
}

#problem {
    font-size: 72px;
}

#winner {
    font-size: 72px;
    color: green;
}
```

![gif](https://cs50.harvard.edu/web/2020/notes/6/images/add1.gif)

## Examples

Check out some [examples](examples/)
