# Django

Previously using HTML and CSS, we were able to create a static webpage. Static means that everytime one visits that webpage, everything will look exactly the same; however, that's not the case for most websites. Most websites changes over time with new informations, but how did they achieve that? Someone is constantly changing the HTML? Not likely. This process involves backend development, and Django allows us to use Python to create a backend that dynamically changes HTML and CSS

## HTTP

To understand how a backend works, we have to first understand what is a [Hypertext Transfer Protocol (HTTP)](https://developer.mozilla.org/en-US/docs/Web/HTTP). HTTP is a widely-accepted protocol for how messages are transfered back and forth across the internet. Typically, information online is passed between a client (user) and a server. The client sends some request to view a website and the server sends the HTML and CSS for that website so that the client's browser can render those files and display the webpage

Figure 1

The request can be of various types. Common ones are `GET` and `POST`. `GET` request appears everyday when one is browsing the internet, it basically means to ask the server for permission of viewing a website. `POST` on the other hand is when the user enters some information in, for example, an HTML form, then sending the information to the server

Requests are sent from the client to the server, and the server will reply or response. The response is usually some status code

Figure 2

Status code 200 indicates that the request is permitted and the HTML and CSS files are rendered by the clinet's browser to display the website. Status code 301 means the website has moved to another URL permanently. Status code 403 means that the client sending the request should not have the permission to view the website. Status code 404 is a common one which just means the website at the URL is not found. Status code 500 means the website itself has some bug in it
