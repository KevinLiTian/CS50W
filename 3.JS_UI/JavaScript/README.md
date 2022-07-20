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

#### Query Selector

It might be more beneficial if JavaScript can do more than just sending alerts, for example, interact with the HTML. `document` gives us the ability to search through the DOM and `querySelector` allows us to get an element from the DOM

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Count</title>
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

We generally use `===` to ensure they are the same. And we can modify the `innerHTML` just by assigning value to the variable. This program allows us to toggle the heading's content between "Hello!" and "Goodbye!" with the button

## DOM Manipulation
