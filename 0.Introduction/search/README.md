# Search

An re-implementation of Google Search

### Background

When you perform a Google search, as by typing in a query into Google’s homepage and clicking the “Google Search” button, how does that query work? Let’s try to find out

Navigate to [google.com](https://www.google.com/), type in a query like “Harvard” into the search field, and click the “Google Search” button.

As you probably expected, you should see Google search results for “Harvard.” But now, take a look at the URL. It should begin with `https://www.google.com/search`, the route on Google’s website that allows for searching. But following the route is a `?`, followed by some additional information

Those additional pieces of information in the URL are known as a query string. The query string consists of a sequence of GET parameters, where each parameter has a name and a value. Query strings are generally formatted as

`field1=value1&field2=value2&field3=value3...`

where an `=` separates the name of the parameter from its value, and the `&` symbol separates parameters from one another. These parameters are a way for forms to submit information to a web server, by encoding the form data in the URL

If you look through the URL, you should see that one of the GET parameters in the URL is `q=Harvard`. This suggests that the name for the parameter corresponding to a Google search is q (likely short for “query”)

It turns out that, while the other parameters provide useful data to Google, only the `q` parameter is required to perform a search. You can test this for yourself by visiting `https://www.google.com/search?q=Harvard`, deleting all the other parameters. You should see the same Google results!

Using this information, we are able to re-implement a front end for Google's search engine

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Search</title>
    </head>
    <body>
        <form action="https://www.google.com/search">
            <input type="text" name="q">
            <input type="submit" value="Google Search">
        </form>
    </body>
</html>
```

## Video Demo

[![Watch the video](https://img.youtube.com/vi/nYtm2S3cETE/default.jpg)](https://www.youtube.com/watch?v=nYtm2S3cETE)

## How to Use

Open `index.html` with the browser of your choice

## Note

If out of curiosity, one would like to see what the GET parameters for a URL are, I wrote a simple Python script in the _readurl_ directory. Navigate to that directory, copy and paste the URL in the _url.txt_, run the command

`python readurl.py url.txt`

The result will be generated in the result.txt which the URL is being splited into several pieces and each piece is a GET parameter
