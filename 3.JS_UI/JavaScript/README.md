# JavaScript

Recall that in most online interactions, we have a client/user that sends an HTTP Request to a server, which sends back an HTTP Response. All of the Python code we’ve written so far using Django has been running on a server. JavaScript will allow us to run code on the client side, meaning no interaction with the server is necessary while it’s running, allowing our websites to become much more interactive

## Introduction to JavaScript

Let's try to write some simple JavaScript code that just says something like "Hello, world!"

`alert('Hello, world!');`

But how do we run it? It turns out that JavaScript can be written inside a HTML file within the `<script>` tags

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello</title>
        <script>
            alert('Hello, world!');
        </script>
    </head>
    <body>
        <h1>Hello!</h1>
    </body>
</html>
```

![1](https://user-images.githubusercontent.com/99038613/180077458-dfe1a841-4d4c-44af-92e6-e55eadd4ecc4.jpg)

#### Event

One feature of JavaScript that makes it helpful for web programming is that it supports [Event-Driven Programming](https://medium.com/@vsvaibhav2016/introduction-to-event-driven-programming-28161b79c223)

An event can be anything from clicking a button to submitting a form or even scrolling through the webpage. JavaScript enables us to "listen" to these events and react accordingly

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello</title>
        <script>
            function hello() {
                alert('Hello, world!')
            }
        </script>
    </head>
    <body>
        <button onclick="hello()">Click Here</button>
    </body>
</html>
```

The above program defines a JavaScript function using the keyword function, and notice that by adding an `onclick` attribute to the `button` tag, the JavaScript will listen to the button click event, and if it happens it will call the `hello()` function which sends an alert

#### Variables

JavaScript is a programming language just like Python, it has variables. There are multiple ways of declaring a variable in JS:

- `var`: Define a variable globally

  `var age = 20;`

- `let`: Define a variable that is limited in scope to the current block such as a function or loop

  `let counter = 1;`

- `const`: Define a value that will not change

  `const PI = 3.14;`

#### Template Literal

Similar to formatting strings in Python, JS uses template literals to concatenate variables with strings

```JavaScript
function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;

    if (counter % 10 === 0) {
        alert(`Count is now ${counter}`)
    }
}
```

#### Query Selector

It might be more beneficial if JavaScript can do more than just sending alerts, for example, interact with the HTML. `document` gives us the ability to search through the DOM and `querySelector` allows us to get an element from the DOM

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <script>
            function hello() {
                const header = document.querySelector('h1');
                if (header.innerHTML === 'Hello!') {
                    header.innerHTML = 'Goodbye!';
                }
                else {
                    header.innerHTML = 'Hello!';
                }
            }
        </script>
    </head>
    <body>
        <h1>Hello!</h1>
        <button onclick="hello()">Click Here</button>
    </body>
</html>
```

Notice that in the function `hello()`, we use `document.querySelector` to search the DOM with the tag `h1`, the `querySelector` will select the first matching element if there are multiple but in this case, there's only one `h1` element. Then we use `innerHTML` to select the content of that element, and compare it using `===`. Comparison can be done two ways in JS:

- `==`: Compare the value only
- `===`: Compare the value and the type of the variable

We generally use `===` to ensure they are the same. And we can modify the `innerHTML` just by assigning value to the variable. This program allows us to toggle the heading's content between "Hello!" and "Goodbye!" with the button. This is called DOM manipulation since we are dynamically changing the HTML content

## DOM Manipulation

Now we can apply the idea of DOM manipulation to achieve something more interesting:

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Count</title>
        <script>
            let counter = 0;
            function count() {
                counter++;
                document.querySelector('h1').innerHTML = counter;
            }
        </script>
    </head>
    <body>
        <h1>0</h1>
        <button onclick="count()">Count</button>
    </body>
</html>
```

![gif](https://cs50.harvard.edu/web/2020/notes/5/images/count2.gif)

The last example was a glimpse at how JS is able to manipulate the DOM. Just like inline CSS, inline JS such as the `onclick` attribute, are specific but will make the HTML page messy and not generalize well. Commonly, we would want to separate JS code from HTML elements. For example, we want to move the `onclick` attribute of the button to somewhere outside, we can use JS to manipulate the DOM and add the `onlick` attribute in the script:

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <script>
            function hello() {
                alert('Hello, world!')
            }
            document.querySelector('button').onclick = hello;
        </script>
    </head>
    <body>
        <button>Click Here</button>
    </body>
</html>
```

The above script adds an event listener to the button's `onclick` event, and the action of this event is the function `hello`. Notice that we are not calling the function like `hello()` with the parentheses, we are only linking this function as the action of the button's `onclick` event. By doing this, we are able to separate JS from HTML

However, if you try to above program, an error will be thrown saying that `Cannot set property 'onclick' of null`. Why would this happen? It turns out that `null` is like `None` of Python in JS, which means the query selector did not find an element of `button`. But there is one in the HTML... The reason is that the browser interprets this file line by line, and since the script is written before the button, when the browser executes the script, there is no button to be found. An easy way would be to move the script to the bottom, but there's a more common solution:

```JS
document.addEventListener('DOMContentLoaded', function() {
    // Some code here
});
```

The above is an event listener that respond to the `DOMContentLoaded` event, which happens when the HTML elements are loaded. We can add the other scripts inside to ensure that they will run after the DOM content is loaded

Another way to separate JS from HTML is to have all the JavaScript code inside another file:

In the HTML file, we only put a source link in the script tag

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <script src="app.js"></script>
    </head>
    <body>
        <button>Click Here</button>
    </body>
</html>
```

In another file called `app.js`:

```JS
function hello() {
    alert("Hello, world!");
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = hello;
});
```

Having JavaScript in a separate file is useful for a number of reasons:

- **Visual appeal**: Our individual HTML and JavaScript files become more readable.
- **Access among HTML files**: Now we can have multiple HTML files that all share the same JavaScript.
- **Collaboration**: We can now easily have one person work on the JavaScript while another works on HTML.
- **Importing**: We are able to import JavaScript libraries that other people have already written. For example Bootstrap has their own JavaScript library you can include to make your site more interactive.

#### CSS Manipulation

It turns out that we can use DOM manipulation to dynamically change the CSS properties as well

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
     <title>Colors</title>
     <script>
         document.addEventListener('DOMContentLoaded', function() {
            document.querySelectorAll('button').forEach(function(button) {
                button.onclick = function() {
                    document.querySelector("#hello").style.color = button.dataset.color;
                }
            });
         });
     </script>
</head>
<body>
    <h1 id="hello">Hello</h1>
    <button data-color="red">Red</button>
    <button data-color="blue">Blue</button>
    <button data-color="green">Green</button>
</body>
</html>
```

`querySelectorAll` is similar to `querySelector` but it selects all elements that matches the specification. `forEach` applies a function to each button selected and this function adds an event listener to the `onclick` event, the action of this event is to modify the `style.color` of the heading with id of `hello`. The color we will modify the heading to is specified using `button.dataset.color` which matches the `data-color` attribute on each button

This is a fairly complicated program since everything is nested, so take your time to read through the code and explanation, try to understand how it works'

![gif](https://cs50.harvard.edu/web/2020/notes/5/images/colors.gif)

#### More Events

Other than the `onclick` event, JS provides us with lots of [events](https://www.w3schools.com/js/js_events.asp) to play with

- onchange
- onmouseover
- onkeydown
- onkeyup
- onload
- onblur
- ...

An example of implementing the color change functionality with the `onchange` event:

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Colors</title>
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                document.querySelector('select').onchange = function() {
                    document.querySelector('#hello').style.color = this.value;
                }
            });
        </script>
    </head>
    <body>
        <h1 id="hello">Hello</h1>
        <select>
            <option value="black">Black</option>
            <option value="red">Red</option>
            <option value="blue">Blue</option>
            <option value="green">Green</option>
        </select>

    </body>
</html>
```

Notice that the `this` keyword is a special functionality in JS that Python does not support, if you have experience with C++, it might be familiar. `this` indicates the variable we are currently applying the function on, in this case is the `select` element since we are applying the function on its `onchange` event. So `this.value` is the value of the `select` element

![gif](https://cs50.harvard.edu/web/2020/notes/5/images/colors2.gif)

#### Interval

After seeing some DOM manipulation and event-driven programming, JS is always responding to some user input, such as clicking or selecting. In fact, JS can also do something automatically by a set interval. Such as incrementing a counter automatically for each second

```JS
let counter = 0;

function count() {
    counter++;
    document.querySelector('h1').innerHTML = counter;
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = count;

    setInterval(count, 1000);
});
```

The [`setInterval`](https://www.w3schools.com/jsref/met_win_setinterval.asp) function takes in a function to run, in this case is the `count` function, and an interval (in milliseconds) between function runs, in this case 1000 milliseconds, which is equivalent to 1 second

#### Local Storage

Everytime we refresh the webpage, everything will be restarted, whether it's the static HTML and CSS or JS variables, since they will all be reloaded by the browser. Sometimes, it is the way we want it to behave, but sometimes we might want it to remember something. We can easily accomplish this using a backend server such as Django, but is there a way to do everything client side? Local storage makes it possible to cache some information as key value pairs in the browser

```JS
// Check if there is already a vlaue in local storage
if (!localStorage.getItem('counter')) {

    // If not, set the counter to 0 in local storage
    localStorage.setItem('counter', 0);
}

function count() {
    // Retrieve counter value from local storage
    let counter = localStorage.getItem('counter');

    // update counter
    counter++;
    document.querySelector('h1').innerHTML = counter;

    // Store counter in local storage
    localStorage.setItem('counter', counter);
}

document.addEventListener('DOMContentLoaded', function() {
    // Set heading to the current value inside local storage
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;
});
```

- `localStorage.getItem(key)`: This function searches for an entry in local storage with a given key, and returns the value associated with that key
- `localStorage.setItem(key, value)`: This function sets and entry in local storage, associating the key with a new vlaue

## API

[Application Programming Interface (API)](https://www.mulesoft.com/resources/api/what-is-an-api) is the connection between different services. For example, if someone wants to use the Google Maps data, or currency exchange data in their website, since these data are constantly changing in real time, the website cannot use some static data, or manually transfering the data. This is where API comes in handy, every service generally has their own APIs, Google Maps for example, if you visit one of their API links, some real time data will be returned to you

#### JavaScript Object

A [JavaScript Object](https://www.w3schools.com/js/js_objects.asp) is very similar to a Python dictionary, which contains key value pairs. For example

```JS
let person = {
    first: 'Harry',
    last: 'Potter'
};
```

`person` is now a JavaScript Object, and we can access its values via the keys

```JS
person.first    // "Harry"
person.last     // "Potter"
person['first'] // "Harry"
person['last']  // "Potter"
```

JS objects store data in such structured way such that the data can be transfered easily from one site to another, particularly when using APIs. When visiting an API link for a service such as Google Maps, data will be returned in [JSON](https://www.w3schools.com/js/js_json_intro.asp) (JavaScript Object Notation) format:

```JSON
{
    "origin": {
        "city": "New York",
        "code": "JFK"
    },
    "destination": {
        "city": "London",
        "code": "LHR"
    },
    "duration": 415
}
```

#### Currency Exchange

Now we'll use the [European Central Bank’s Exchange Rate API](https://exchangeratesapi.io/) to build a simple currency exchange website

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Currency Exchange</title>
        <script src="currency.js"></script>
    </head>
    <body>
        <form>
            <input id="currency" placeholder="Currency" type="text">
            <input type="submit" value="Convert">
        </form>
        <div id="result"></div>
    </body>
</html>
```

For the JS, we will use something called [AJAX](https://www.w3schools.com/js/js_ajax_intro.asp) or Asynchronous JavasScript And XML, which allows us to access information from external pages even after our page has loaded. Particularly, we'll use the [`fetch`](https://javascript.info/fetch) function which sends an HTTP request to an API and get the data from it; however, since fetching data from API is the same as requesting from a server, it takes time and it might fail. Therefore the `fetch` function returns a [promise](https://web.dev/promises/) which tells our browser that something is going to be returned back, but not necessarily right away. We'll then use the `.then` syntax to specify that what will we do after the data has been fetched and returned back to us

```JS
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function() {

        // Send a GET request to the URL
        fetch('https://api.exchangeratesapi.io/latest?base=USD')
        // Put response into json form
        .then(response => response.json())
        .then(data => {
            // Get currency from user input and convert to upper case
            const currency = document.querySelector('#currency').value.toUpperCase();

            // Get rate from data
            const rate = data.rates[currency];

            // Check if currency is valid:
            if (rate !== undefined) {
                // Display exchange on the screen
                document.querySelector('#result').innerHTML = `1 USD is equal to ${rate.toFixed(3)} ${currency}.`;
            }
            else {
                // Display error on the screen
                document.querySelector('#result').innerHTML = 'Invalid Currency.';
            }
        })
        // Catch any errors and log them to the console
        .catch(error => {
            console.log('Error:', error);
        });
        // Prevent default submission
        return false;
    }
});
```

Notice that after getting the data from the API with `fetch` and `.then`, we'll need to transform the data into JSON format which is also a promise so we'll need to use `.then` again

## Examples

Check out some [examples](examples/)
