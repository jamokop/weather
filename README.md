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

##  Openweather spider service
this microservice is used to fetch weather data from openweather,run as a cron job per minute

    python3 project/services/spider.py [city]
    return a insert id
    {
      insertid: xxx
    }

##  Weather data service (port 5001)
this microservice provides method to handle weather data. u can retrieve weather data by city name , filter by a given date range.
And store the latest weather data.
    python3 project/services/weather_db.py

    To look up weather data in the databases
    GET /weather?city=[city]&start=[date1]&end=[date2]
    return a list of weather data
    {
        "data" : [
            {
                ...
            }
        ],
        "error"  : null,
        "status" : 200
    }

    To store weather data into database
    POST /weather
    {
        'city' : [city],
        'temp' : [temp],
        'humidity' : [humidity]
    }
    return a insert id
    {
      insertid: xxx
    }

