# weather

Overview
========
a micro app providing weather data

Environment
===========
python3,tornado,flask,mysql

Install
=======

The quick way is use the provided `make` file.

<code>
$ make install
</code>

Starting and Stopping Services
==============================

To launch the services:

<code>
$ make launch
</code>

To stop the services: 

<code>
$ make shutdown
</code>


APIs and Documentation
======================

##  openweather spider service
this microservice is used to fetch weather data from openweather,run as a cron job per minute 
python3 project/services/spider.py [city]
return a insert id 
{
  insertid: xxx
}


