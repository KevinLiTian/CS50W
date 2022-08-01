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

#### Scaling

Once we have some upper limit on how many requests our server can handling, we can begin thinking about how we want to handle the scaling of our application. Two different approaches to scaling include:

- **Vertical Scaling**: Better servers, where each can handle more requests
- **Horizontal Scaling**: More servers, split requests among servers

#### Load Balancing

At some point we are going to have to go with horizontal scaling since there's a limit with vertical scaling, whereas the limit for horizontal scaling is much larger. When we use horizontal scaling, we encounter the problem of load balancing, the task to split requests among servers. We answer this question by employing a **load balancer**, which is another physical hardware that intercepts requests and assign them to servers. There are several methods to go about assigning:

- **Random**: Randomly assign requests to servers
- **Round-Robin**: Load balancer will alternate which server receives an incoming request. If we have three servers, the first request might go to server A, the second to server B, the third to server C, and the fourth back to server A
- **Fewest Connections**: Load balancer looks for the server that is handling the fewest requests and assign incoming requests to that server

Fewest connections method may seems the best but it takes longer for the load balancer to calculate and uses more computational power. Therefore, each method has its own specialty, we should decide accordingly

#### Sessions

Another problem arises when we use horizontal scaling, that is sessions. Gmail for instance, if you login once, quit the browser then visit Gmail again, you'll still be logged in, this is because Google servers remembered your session. But if the load balancer we designed assign you to different servers each time we visit the same site, the servers are not able to remember your session since that information is on another server. Like many problems of scalability, we have multiple approaches:

- **Sticky Session**: The load balancer remembers which server each user was using and assign them to the same server they used. However, this adds tone of load on the load balancer and also the server if a lot of people sticks to one server
- **Database Sessions**: Session information is stored in a database that all servers have access to. The drawback here is it takes time and computing power to query from and write to a database
- **Client-Side Session**: Rather than storing information server-side, we can store them on users' browser as cookies. The drawbacks to this method include security concerns of hackers forge cookies to log in as another user

#### Autoscaling

Servers receive requests unevenly throughout time, sometimes they receive tones of requests and sometimes there are no requests at all. This scenario brought about the idea of autoscaling, which has become common in cloud computing. The number of serverrs being used for your site can grow or shrink based on the requests servers receive

#### Server Failure

Having multiple servers can help avoid what's known as a **Single Point of Failure**, which is when one piece of hardware fails, the entire site will crash. When scaling horizontally, the load balancer can detect which servers have crashed by sending periodic heartbeat requests to each server, and then stop assigning new requests to servers that have crashed. At this point, it seems we have simply moved our single point of failure from a server to the load balancer, but we can account for this by having backup load balancers available if our original happens to crash
