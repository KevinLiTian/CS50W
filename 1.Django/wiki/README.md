# Wiki

Design a Wikipedia-like online encyclopedia with Django

## Background

[Wikipedia](https://www.wikipedia.org/) is a free online encyclopedia that consists of a number of encyclopedia entries on various topics

Each encyclopedia entry can be viewed by visiting that entry’s page. Visiting [https://en.wikipedia.org/wiki/HTML](https://en.wikipedia.org/wiki/HTML), for example, shows the Wikipedia entry for HTML. Notice that the name of the requested page (HTML) is specified in the route /wiki/HTML. Recognize too, that the page’s content must just be HTML that your browser renders

In practice, it would start to get tedious if every page on Wikipedia had to be written in HTML. Instead, it can be helpful to store encyclopedia entries using a lighter-weight human-friendly markup language. Wikipedia happens to use a markup language called [Wikitext](https://en.wikipedia.org/wiki/Help:Wikitext), but for this project we’ll store encyclopedia entries using a markup language called [Markdown](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)

By having one Markdown file represent each encyclopedia entry, we can make our entries more human-friendly to write and edit. When a user views our encyclopedia entry, though, we’ll need to convert that Markdown into HTML before displaying it to the user

## Video Demo

[![Watch the video](https://img.youtube.com/vi/DoJh0hTbG24/default.jpg)](https://youtu.be/DoJh0hTbG24)

## How to Use

In the `1.Django/wiki` diretory, run the command

`python manage.py runserver`

Then open the HTTP address the terminal provides using the browser of your choice
