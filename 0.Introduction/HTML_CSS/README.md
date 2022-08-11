# HTML & CSS

The premise of building a web application is to have webpages. HTML and CSS are the fundamental building blocks of webpages, where they describe the structure and the style respectively

## HTML

Hypertext Markup Language (HTML) is a language that describes the layout/structure of webpages. For instance, texts, images, tables, forms, etc. are all described by HTML. As always, the first program in any language is "Hello World", see the example below

```HTML
<!DOCTYPE html> # Tell the web browser this file is in HTML5
<html lang="en"> # Language is English
    <head>
        <title>Hello!</title> # The title of the webpage is "Hello!"
    </head>
    <body>
        Hello, world!
    </body>
<html>
```

<img src="https://user-images.githubusercontent.com/99038613/177906700-4fc0c79f-2e6f-4e4c-bb9d-a0e221c2a8b0.jpg" width=60%>

HTML is structured by elements, or pairs of tag, which are the `<>` pairs. For instance, the `<html>` and `</html>` are the opening and closing tag for this HTML file. HTML elements can include attributes such as the `lang="en"` in the opening _html_ tag, indicates that this webpage is in English

### Document Object Model (DOM)

<img src="https://user-images.githubusercontent.com/99038613/177905929-2bcfc647-b63a-41e1-b364-b8aa2ae0c986.jpg" height=30% width=30%>

The DOM is a convenient way of visualizing the way HTML elements relate to each other using a tree-like structure. Above is an example of the DOM layout for the "Hello, world" HTML file

### More HTML Elements

Otherthan the html, head and body elements that are used in almost all the webpages, there are more elements to describe different layout of the webpage such as headings, lists, links, images, bold/italics, tables, etc.

- **Headings**: `<h1></h1>`, `<h2></h2>`, ..., `<h6></h6>`
- **Lists**: `<ol></ol>`, `<ul></ul>`, `<li>,</li>`
- **Links**: `<a href="google.com">`
- **Images**: `<img src="image.png">`
- **Bold/Italics**: `<strong></strong>`, `<i></i>`

#### Example Program

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>HTML Elements</title>
    </head>
    <body>
        <!-- We can create headings using h1 through h6 as tags. -->
        <h1>A Large Heading</h1>
        <h2>A Smaller Heading</h2>
        <h6>The Smallest Heading</h6>

        <!-- The strong and i tags give us bold and italics respectively. -->
        A <strong>bold</strong> word and an <i>italicized</i> word!

        <!-- We can link to another page (such as cs50's page) using a. -->
        View the <a href="https://cs50.harvard.edu/">CS50 Website</a>!

        <!-- We used ul for an unordered list and ol for an ordered one. both ordered and unordered lists contain li, or list items. -->
        An unordered list:
        <ul>
            <li>foo</li>
            <li>bar</li>
            <li>baz</li>
        </ul>
        An ordered list:
        <ol>
            <li>foo</li>
            <li>bar</li>
            <li>baz</li>
        </ol>

        <!-- Images require a src attribute, which can be either the path to a file on your computer or the link to an image online.
        It also includes an alt attribute, which gives a description in case the image can't be loaded. -->
        An image:
        <img src="../../images/duck.jpeg" alt="Rubber Duck Picture">
        <!-- We can also see above that for some elements that don't contain other ones, closing tags are not necessary. -->

        <!-- Here, we use a br tag to add white space to the page. -->
        <br/> <br/>

        <!-- A few different tags are necessary to create a table. -->
        <table>
            <thead>
                <th>Ocean</th>
                <th>Average Depth</th>
                <th>Maximum Depth</th>
            </thead>
            <tbody>
                <tr>
                    <td>Pacific</td>
                    <td>4280 m</td>
                    <td>10911 m</td>
                </tr>
                <tr>
                    <td>Atlantic</td>
                    <td>3646 m</td>
                    <td>8486 m</td>
                </tr>
            </tbody>
        </table>
    </body>
<html>
```

<img src="https://user-images.githubusercontent.com/99038613/177905942-4f770665-a675-46d5-a93c-4433378095c8.jpg" height=40% width=40%>

### Forms

The previous elements were not interactive, they only show something to the users. Forms are elements that can interact with users, users can enter texts, select from options or submit the form

#### Example Program

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Forms</title>
</head>
<body>
    <form>
        <input type="text" placeholder="First Name" name="first">
        <input type="password" placeholder="Password" name="password">
        <div>
            Favorite Color:
            <input name="color" type="radio" value="blue"> Blue
            <input name="color" type="radio" value="green"> Green
            <input name="color" type="radio" value="yellow"> Yellow
            <input name="color" type="radio" value="red"> Red

        </div>
        <input type="submit">
    </form>
</body>
</html>
```

<img src="https://user-images.githubusercontent.com/99038613/177906854-511465e3-a07a-4ffc-8c0d-fd2c8f0c76e3.jpg" width=60%>

## CSS

Cascading Style Sheet (CSS) is used to customize the appearance of a website. CSS properties can be applied to HTML elements to change the way they look to the users. For instance

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
    </head>
    <body>
        <h1 style="color: blue; text-align: center;">A Colorful Heading!</h1>
        Hello, world!
    </body>
<html>
```

<img src="https://user-images.githubusercontent.com/99038613/178088415-6c5ec938-4ae8-4b5f-88fb-ca3718b79261.jpg" width=60%>

### Inline Styling

By adding the attribute "style" in the h1 element in the above example, the heading turns to blue color and is aligned at the center of the webpage. This styling method is called "inline styling", which the style is specified within the HTML element. Inline styling is powerful as it gives certain elements some appearance; however, if we have lots of styling, the inline styling method can make the HTML file messy.

### Head Styling

Another way of styling is to put the style in the head section of the HTML page. For instance

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
        <style>
            h1 {
                color: blue;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h1 >A Colorful Heading!</h1>
        Hello, world!
    </body>
</html>
```

The `style` tag within the head section is specifying the style of this HTML page, and the `h1` in the style specifies that all `h1` elements in this HTML file should have the style in the curly brackets. This method allows the style to be only in the head section, provides readability and cleanness. But the style in the head section only specifies the style in this certain HTML page, commonly a website will have lots of HTML pages, what if some other HTML pages also want the same style? We can copy and paste, but it's not the best design pattern to have things everywhere

### CSS Files

A good way to implement CSS is to create another .css file and link it in the head section of the HTML page, such that any HTML file can borrow CSS properties from the .css file. For instance

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Hello!</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <h1 >A Colorful Heading!</h1>
        Hello, world!
    </body>
</html>
```

In another file called `styles.css`

```CSS
h1 {
    color: blue;
    text-align: center;
}
```

### CSS Properties

There are too many CSS properties that can be modified to make the website looks better. Some most common properties are:

- **Color**: the color of text
- **Text-align**: where elements are placed on the page
- **Background-color**: can be set to any color
- **Width**: in pixels or percent of a page
- **Height**: in pixels or percent of a page
- **Padding**: how much space should be left inside an element
- **Margin**: how much space should be left outside an element
- **Font-family**: type of font for text on page
- **Font-size**: in pixels
- **Border**: size type (solid, dashed, etc) color

### CSS Selectors

In the previous examples, the styling only applies to certain HTML elements such as headings; however, sometimes not all headings should have the same styling, so it's not enough to select only `h1`, we want a way to specify which `h1` the styling should be applied to. There are two ways to do this

- ID: Unique symbol of a element. For instance `<h1 id="thish1">`, then in the CSS file, use `#thish1` to select, where `#` specifies id of element

- Class：Sometimes we want a group of element to look the same, but id is unique to each element. Class can be used to give a group of elements the same styling. For instance, `<h1 class="foo">` and `<h2 class="foo">` then in the CSS file, use `.foo` too select all elements with the class foo

There are more advanced selectors such as multiple element selector, descendant selector,, child selector, attribute selector, etc.

### Responsive Design

Nowadays people browse the web not only using their computers, but also pads and mobile phones. The website that looks nice on computer does not necessarily look good on mobile devices. That's why we introduce responsive design, which makes the website looks good whatever the device is.

The simplest way is to add one line of code below in the head section of the HTML file

`<meta name="viewport" content="width=device-width, initial-scale=1.0">`

This method improves the appearance of the website on mobile devices in some cases but still not good enough. Another way to deal with responsive design is through media queries, which the browser identifies the screen size and give specified CSS properties

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Screen Size</title>
        <style>
            @media (min-width: 600px) {
                body {
                    background-color: red;
                }
            }

            @media (max-width: 599px) {
                body {
                    background-color: blue;
                }
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the page!</h1>
    </body>
</html>
```

The above code specifies that when the screen is larger than 600px in width, the body will have color red, and when the screen is smaller than 599px, like on a mobile phone, the color of the body will turn to blue

## Bootstrap & Sass

CSS is complex and tedious, therefore use some extensions would be helpful to make better appearance with less effort

### Bootstrap

It turns out that there are many libraries that other people have already written that can make the styling of a webpage even simpler. One popular library that we’ll use throughout the course is known as [bootstrap](https://getbootstrap.com/). By simply including a link in the head section of the HTML, we are able to use written CSS classes in Bootstrap

```HTML
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
```

### Sass

Syntactically Awesome Style Sheets (Sass) is an extension to CSS which makes the CSS more efficient and readable. Notice that whatever is written using Sass can all be written in CSS, Sass only makes the syntax more efficient and convenient

#### Variables

For instance, Sass introduces variables using "$" so that whenever we want to change the color, we don't have to change one by one, we can only change the value of the variable. The Sass is written in .scss files

```SCSS
/* In a .scss file */
$color: red;

ul {
    font-size: 14px;
    color: $color;
}

ol {
    font-size: 18px;
    color: $color;
}
```

Notice that we cannot directly use this .scss file as a link in the head section of the HTML page, since HTML does not recognize .scss files. The .scss files have to be "compiled" into .css files using the command line `sass variables.scss:variables.css`. Or if one does not want to write this command everytime one changes the .scss file, one can use the command `sass --watch variables.scss:variables.css` so that the sass will automatically monitor the changes and recompile if any

#### Inheritance

One more feature that Sass gives us is known as inheritance, which a CSS property can inherit from other CSS properties to make the CSS more efficient. For instance

```SCSS
%message {
    font-family: sans-serif;
    font-size: 18px;
    font-weight: bold;
    border: 1px solid black;
    padding: 20px;
    margin: 20px;
}

.success {
    @extend %message;
    background-color: green;
}

.warning {
    @extend %message;
    background-color: orange;
}

.error {
    @extend %message;
    background-color: red;
}
```

By using `@extend`, the latter three properties inherits from the `%message` property, providing better syntax

<img src="https://user-images.githubusercontent.com/99038613/178119010-c9ae9f77-a508-4096-b350-65c673b9dd56.jpg" width=60%>

## Examples

Check out some [examples](examples/)
