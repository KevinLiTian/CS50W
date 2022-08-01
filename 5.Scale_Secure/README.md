# Scalability & Security

So far, our web applications have been running on local machines, hosting local servers; however, we might want more people to use our application through the internet. As more people use our web applications, we want the app to scale well, respond to lots of users requests without issues; and we also want to keep information secure, not leaking user data or leaving vulnerabilities for hackers to exploit upon

## Scalability

In order to let other people use our web applications, we need to run our app on web servers, which are physical hardwares, computers that are decicated to listening requests and responding to them. Servers can be either on-premise (we own and maintain the physical devices) or cloud (owned by companies suchas Amazon or Google, we pay to rent serrver space). There are benefits and drawbacks to both options:

- **Customization**: Hosting your own servers allows you to decide exactly how they work, more flexibility than cloud servers
- **Expertise**: It is much simper to host applications on cloud servers than maintain your own servers
- **Cost**: Cloud server hosting charge you more than it is to maintain the servers; however, the startup cost for hosting it yourself is high since you have to purchase physical hardwares
- **Scalability**: Cloud server typically scale better. If some day there are lots of visitors, your own server might not be able to handle that much requests and you will need to buy more physical hardwares, while cloud server allow you to rent space flexibly, charging based on how much visitors your site has

When a user sends an HTTP request to the server, the server should send back a response. However, in reality, ost servers get far more thhan one request at a time, as depicted below (white lines stand for requests):

![server](https://cs50.harvard.edu/web/2020/notes/8/images/server0.png)

This is where we run into the issue of scalability. A single server can handle only so many requests at once, forcing us to make plans about what to do when our one server is overworked. Whether we decide to host on premise or on the cloud, we have to determine how many requests a server can handle without crashing, which can be done using any number of benchmarking tools including Apache Bench.

### Scaling

Once we have some upper limit on how many requests our server can handling, we can begin thinking about how we want to handle the scaling of our application. Two different approaches to scaling include:

- **Vertical Scaling**: Better servers, where each can handle more requests
- **Horizontal Scaling**: More servers, split requests among servers

### Load Balancing

At some point we are going to have to go with horizontal scaling since there's a limit with vertical scaling, whereas the limit for horizontal scaling is much larger. When we use horizontal scaling, we encounter the problem of load balancing, the task to split requests among servers. We answer this question by employing a **load balancer**, which is another physical hardware that intercepts requests and assign them to servers. There are several methods to go about assigning:

- **Random**: Randomly assign requests to servers
- **Round-Robin**: Load balancer will alternate which server receives an incoming request. If we have three servers, the first request might go to server A, the second to server B, the third to server C, and the fourth back to server A
- **Fewest Connections**: Load balancer looks for the server that is handling the fewest requests and assign incoming requests to that server

Fewest connections method may seems the best but it takes longer for the load balancer to calculate and uses more computational power. Therefore, each method has its own specialty, we should decide accordingly

### Sessions

Another problem arises when we use horizontal scaling, that is sessions. Gmail for instance, if you login once, quit the browser then visit Gmail again, you'll still be logged in, this is because Google servers remembered your session. But if the load balancer we designed assign you to different servers each time we visit the same site, the servers are not able to remember your session since that information is on another server. Like many problems of scalability, we have multiple approaches:

- **Sticky Session**: The load balancer remembers which server each user was using and assign them to the same server they used. However, this adds tone of load on the load balancer and also the server if a lot of people sticks to one server
- **Database Sessions**: Session information is stored in a database that all servers have access to. The drawback here is it takes time and computing power to query from and write to a database
- **Client-Side Session**: Rather than storing information server-side, we can store them on users' browser as cookies. The drawbacks to this method include security concerns of hackers forge cookies to log in as another user

### Autoscaling

Servers receive requests unevenly throughout time, sometimes they receive tones of requests and sometimes there are no requests at all. This scenario brought about the idea of autoscaling, which has become common in cloud computing. The number of serverrs being used for your site can grow or shrink based on the requests servers receive

### Server Failure

Having multiple servers can help avoid what's known as a **Single Point of Failure**, which is when one piece of hardware fails, the entire site will crash. When scaling horizontally, the load balancer can detect which servers have crashed by sending periodic heartbeat requests to each server, and then stop assigning new requests to servers that have crashed. At this point, it seems we have simply moved our single point of failure from a server to the load balancer, but we can account for this by having backup load balancers available if our original happens to crash

### Scaling Databases

In addition to scaling servers, as the amount of data grow larger, we might also need a way to scale out databases. So far we've been storing data using SQLite inside a single file, but with more and more data, we might need to store data in separate files or even on a separate server. There are two main ways to go about scaling our database:

- **Vertical Partitioning**: Split data on a single huge table into several smaller tables with foreign key so we are able to not query the data more than we want
- **Horizontal Partitioning**: Storing multiple tables with the same format. For instance, splitting the `flights` table into `domestic_flights` and `international_flights` so we are able to deal with smaller dataset each query

### Database Replication

Even after scaling our database, it still remains as a Single Point of Failure where if the database server is down, the entire site is down. To avoid this, we can add more database servers that store the same data on each server

- **Single-Primary Replication**: Among all database servers, one of them is the primary data server which we can write and read from it, and we can only read data from others. However, it still contains a single point of failure when it comes to writing to the database
  ![SPR](https://cs50.harvard.edu/web/2020/notes/8/images/single_primary.png)
- **Multi-Primary Replication**: All of the database can be read from and written to. In single-primary replication, when we write to the primary data server, it syncs with all of the other; however, in multi-primary replication, issues arise since we could write to them at the same time

  - **Update Conflict**: Two requests write to the same data
  - **Uniqueness Conflict**: SQL database rows have unique identifiers and if writing at the same time, we might assign same id to two different entries
  - **Delete Conflict**: One request deletes a row and another tries to update it

  ![MPR](https://cs50.harvard.edu/web/2020/notes/8/images/multi_primary.png)

### Caching

Whenever we are working with large databases, it's important to recognize that every interaction with the database is costly, we should minimize the number of queries to the database server. For instance, the [New York Times](https://www.nytimes.com/) website have some database with all articles stored in it. It is not likely that the New York Times website queries the database for every article everytime a users visits the website. Since the articles commonly won't change until some other news is published, the website will remain the same for some time. This is where caching could be really useful

The idea of caching is when visiting a website, we store some information that is not likely to change for some amount of time, and when we visit the website again in the near future, the information doesn't have to be queried from the database, we can access it directly in the cache, which is faster and reduces the interaction with the database

One way to do this is by including this line in the header of an HTTP response:

`Cache-Control: max-age=86400`

This means for the next 86400 seconds, if the user visits the website again, use the cached data instead of querying from the database

In addition to client-side caching, caching can also be done on the server-side. With this cache, our backend setup will look a bit like the figure below, where all servers have access to a cache so that they don't have to query the database everytime

![cache](https://cs50.harvard.edu/web/2020/notes/8/images/server_cache.png)

Django provides its own [cache framework](https://docs.djangoproject.com/en/4.0/topics/cache/) allowing us to incorporate caching in our applications. This framework offers several ways of caching:

- **Per-View Caching**: This allows us to decide that once a specific view has been loaded, that same view can be rendered without going through the function for the next specified amount of time
- **Template-Fragment Caching**: This caches specific parts of a template so they do not have to be re-rendered. For example, we may have a navigation bar that rarely changes, meaning we could save time by not reloading it
- **Low-Level Cache API**: This allows you to do more flexible caching, essentially storing any information you would like to

## Security

Now, we’ll begin to discuss how to make sure our web applications are secure, which will involve many different measures that span nearly every topic we’ve discussed so far

### Git & GitHub

Git keeps track of all history commits, so if your git repo is public on Github, make sure to not put any personal information in any commits since everyone has access to all of your commits

### HTML

There are many vulnerabilities that arise from using HTML. One common weakness is known as a Phishing Attack, which occurs when a user who thinks they are going to one page is actually taken to another. These are not necesarily things we can account for when designing a website, but we should definitely keep them in mind when interacting with the web ourselves. For example, a malicious user might write out this HTML:

```HTML
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Link</title>
    </head>
    <body>
        <a href="https://cs50.harvard.edu/">https://www.google.com/</a>
    </body>
</html>
```

Which acts like this:

![vid](https://cs50.harvard.edu/web/2020/notes/8/images/phishing.gif)

The fact that HTML is actually sent to a user as part of a request opens up more vulnerabilities, because everyone has access to the layout and style that allowed you to create your site. For example, a hacker could go to [bankofamerica.com](https://cs50.harvard.edu/), copy all of their HTML, and paste it in their own site, creating a site that looks exactly like Bank of America’s. The hacker could then redirect the login form on the page so all usernames and passwords are sent to them. (Also, here’s the [real Bank of America link](https://www.bankofamerica.com/)–just wanted to see if you were checking urls before clicking!)

### HTTPS

As we discussed earlier in the course, most interactions that occur online follow HTTP protocol, although now more and more transactions use HTTPS, which is an encrypted version of HTTP. While using these protocols, information is transferred from one computer to another through a series of servers as pictured below

![HTTPS](https://cs50.harvard.edu/web/2020/notes/8/images/servers.png)

There is often no way to ensure that all of these transfers are secure, so it is important that all of this transferred information is **encrypted**, meaning that the characters of the message are altered so that the sender and receiver of the message can understand it, but no one else can

#### Secret-Key Cryptography

One approach to this is known as Secret-Key Cryptography. In this approach, the sender and receiver both have access to a secret key that only they know. Then, the secret key is used by the sender to encrypt a message which is then sent to the recipient who uses the secret key to decrypt the message. This method is extremely secure, but it produces a big problem when it comes to practicality. In order for it to work, both the sender and the receiver must have access to the secret key, which means they must meet in person to exchange a key securely. With the number of different websites we interact with on a daily basis, it is clear that in-person meetups are not an option

#### Public-Key Cryptography

An incredible advancement in cryptography that allows the internet to function as it does today is known as Public-Key Cryptography. In this method, there are two keys: one is public and can be shared, and the other must be kept private. Once these keys are established (there are several different mathematical methods for creating pairs of keys which could make up an entire course on their own, so we won’t discuss them here), a sender could look up the public key of a recipient and use it to encrypt a message, and then the recipient could use their private key to decrypt the message. When we use HTTPS rather than HTTP, we know that our request is being secured using public-key encryption

### Databases

In addition to our requests and responses, we must also make sure that our databases are secure. One common thing we’ll need to store is user information, including usernames and passwords as in the table below:

![database](https://cs50.harvard.edu/web/2020/notes/8/images/passwords.png)

However, you never actually want to store passwords in plaintext in case an unauthorized person gets access to your database. Instead, we’ll want to use a **hash function**, a function that takes in some text and outputs a seemingly random string, to create a hash of each password, as in the table below:

![database_hash](https://cs50.harvard.edu/web/2020/notes/8/images/hashes.png)

It is important to note that a hash function is one-way, meaning it can turn a password into a hash, but cannot turn a hash back into a password. This means that any company that stores user information this way does not actually know any of the users’ passwords, meaning each time a user attempts to sign in, the entered password will be hashed and compared to the existing hash. Thankfully, this process is already handled for us by Django. One implication of this storage technique is that when a user forgets their password, a company has no way of telling them what their old password now, meaning they would have to make a new one

There are some cases where you’ll have to decide as a developer how much information you are willing to leak. For example, many sites have a page for forgotten passwords that looks like this:

![img](https://cs50.harvard.edu/web/2020/notes/8/images/forgot0.png)

As a developer, you may want to include either a success or error message after submission:

![img](https://cs50.harvard.edu/web/2020/notes/8/images/sent.png)
![img](https://cs50.harvard.edu/web/2020/notes/8/images/error.png)

But notice how by typing in emails, anyone could determine who has an email registered with that site. This could be totally fine in cases where whether or not a person uses the site is inconsequential (maybe Facebook), but extremely reckless if the fact that you are a member of a certain site could put you in danger (maybe an online support group for victims of abuse)

Another way data could be leaked is in the time it takes for a response to come back. It probably takes less time to reject someone with an invalid email than a person with a correct email address and a wrong password

As we discussed earlier in the course, we must be ware of SQL Injection Attacks whenever we use straight SQL queries in our code

### APIs

We often use JavaScript in conjunction with APIs to build single-page applications. In the case when we build our own API, there are a few methods we can use to keep our API secure:

- **API Keys**: Only process requests from API clients who have a key you have provided to them
- **Rate Limiting**: Limit the number of requests any one user can make in a given time frame. This helps protect against Denial of Service (DOS) Attacks, in which a malicious user makes so many calls to your API that it crashes
- **Route Authentication**: There are many cases where we don’t want to give everyone access to all of our data, so we can use route authentication to make sure only specific users can see specific data

### JavaScript

There are a few types of attacks that malicious users may attempt using JavaScript. One example is known as **Cross-Site Scripting**, which is when a user writes their own JavaScript code and runs it on your website. For example, let’s imagine we have a Django application with a single URL:

```py
urlpatterns = [
    path("<path:path>", views.index, name="index")
]

# In views.py
def index(request, path):
    return HttpResponse(f"Requested Path: {path}")

```

This website essentially tells the user what URL they have navigated to:

![img](https://cs50.harvard.edu/web/2020/notes/8/images/pathworks.png)

But a user can now easily insert some Javascript into the page by typing it in the url:

![gif](https://cs50.harvard.edu/web/2020/notes/8/images/inject.gif)

While this alert example is fairly harmless, it wouldn’t be all that more difficult to include some JavaScript that manipulates the DOM or uses fetch to send a request

#### Cross-Site Request Forgery

We already discussed how we can use Django to prevent CSRF attacks, but let’s take a look at what could happen without this protection. As an example, imagine a bank has a URL you could visit that transfers money out of your account. A person could easily create a link that would make this transfer:

```HTML
<a href="http://yourbank.com/transfer?to=brian&amt=2800">
    Click Here!
</a>
```

This attack can be even more subtle than a link. If the URL is put in an image, then it will be accessed as your browser attempts to load the image:

```HTML
 <img src="http://yourbank.com/transfer?to=brian&amt=2800">
```

Because of this, whenever you are building an application that can accept some state change, it should be done using a POST request. Even if the bank requires a POST request, hidden form fields can still trick users into accidentally submitting a request. The following form doesn’t even wait for the user to click; it automatically submits!

```HTML
 <body onload="document.forms[0].submit()">
    <form action="https://yourbank.com/transfer"
    method="post">
        <input type="hidden" name="to" value="brian">
        <input type="hidden" name="amt" value="2800">
        <input type="submit" value="Click Here!">
    </form>
</body>
```

The above is an example of what Cross-Site Request Forgery might look like. We can stop attacks such as these by creating a CSRF token when loading a webpage, and then only accepting forms with a valid token

## Examples

Check out some [examples](examples/)

## What's Next?

We’ve discussed many web frameworks in this class such as Django and React, but there are more frameworks you might be interested in trying:

- Server-Side
  - [Express JS](https://expressjs.com/)
  - [Ruby on Rails](https://rubyonrails.org/)
  - [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  - …
- Client-Side
  - [Angular JS](https://angularjs.org/)
  - [React JS](https://reactjs.org/)
  - [Vue JS](https://vuejs.org/)
  - [React Native](https://reactnative.dev/)
  - …

In the future, you may also want to be able to deploy your site to the web, which you can do through a number of different services:

- [Amazon Web Services](https://aws.amazon.com/getting-started/hands-on/websites/)
- [GitHub Pages](https://pages.github.com/)
- [Heroku](https://www.heroku.com/)
- [Netlify](https://app.netlify.com/)
- [Google Cloud](https://cloud.google.com/)
- [Microsoft Azure](https://azure.microsoft.com/en-gb/)
- …

We’ve come a long way and covered a lot of material, but there’s still a lot to learn in the world of web programming. Although it can be overwhelming at times, one of the best ways to learn more is to jump into a project and see how far you can run with it. We believe that at this point you have a strong foundation in the concepts of web design, and that you have what it takes to turn an idea into your own working website!
