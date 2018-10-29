how do i get start with this project?
---
since i'm a newbie in microservices, the first two day all I do is surfing the internet and try to learn something about microservices. soooooo many websites in google, I'm overwhelmed soon. I don't know if there's a standard to create a microservice, but I think I do know what microservices are trying to achieve. It's all about independent and autonomous. people should be organized accroding to the services, choose their own language, handle their own data. And microservices should communicate with their endpoint (via http or messaging).So that we can isolate each service, have indepent deployment. Meanwhile, microservices has their disadvantages.The operation could be complex. Transation between different services would be a disaster. There are lots of other stuff to figure out, but i think i'm good enough to take my first step.

http request vs messaging
---
I think messaging is supposed to use between different microservices. For example , whenever a user register successfully, i would like to send a message to tell the email service to send a welcome email. Right now , i have three microservices, but i think they should work as a team. Because all these three microservices are mainly focus on the weather data.

spider service
---
At first, I create this service with flask. In order to fetch weather data i need to send a request. This is too much. A simple function would be good enough.

weather data service
---
At the beginning, i want to integrate it into spider service and api service directly. It's simple and only provides two methods , read from database and insert into database. But it doesn't look like "microservice", so i wrap it into flask. I don't know whether i need to use tornado as well. if u have performance concerns, i would rather add cache in the api layer.

weather api service
---
I don't know how many requests it gonna receive. Instead of using flask, i choose tornado. Tornado is asynchronous and non-blocking, faster than flask. i use Apachebench to send requests  to both data service and api service. with the same city and same date range , i can reach 240 requests per sec and above 1000 requests per sec respectively.
