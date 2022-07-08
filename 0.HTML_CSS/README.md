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

#### Document Objet Model (DOM)

<img src="https://user-images.githubusercontent.com/99038613/177905929-2bcfc647-b63a-41e1-b364-b8aa2ae0c986.jpg" height=30% width=30%>

The DOM is a convenient way of visualizing the way HTML elements relate to each other using a tree-like structure. Above is an example of the DOM layout for the "Hello, world" HTML file

#### More HTML Elements

Otherthan the html, head and body elements that are used in almost all the webpages, there are more elements to describe different layout of the webpage such as headings, lists, links, images or
bold/italics

Note: <!----> represents comments in HTML files

- **Headings**: `<h1></h1>`, `<h2></h2>`, ..., `<h6></h6>`
- **Lists**: `<ol></ol>`, `<ul></ul>`, `<li>,</li>`
- **Links**: `<a href="google.com">`
- **Images**: `<img src="image.png">`
- **Bold/Italics**: `<strong></strong>`, `<i></i>`

##### Example Program

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

#### Forms

The previous elements were not interactive, they only show something to the users. Forms are elements that can interact with users, users can enter texts, select from options or submit the form

##### Example Program

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

