# weather

Overview
========
a micro app providing weather data\
Q&A: https://github.com/jamokop/weather/blob/master/Q_A.md

Environment
===========
python3,tornado,flask,mysql
deploy in google compute engine

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
this microservice provides api to handle weather data. u can retrieve weather data by city name , filter by a given date range.
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

##  Weather data query api service (port 80)
this microservice provide a query api. u can retrieve weather data by city name , filter by a given date range.\
demo: http://35.237.118.107/api/v1/weather?city=singapore&start=2018-10-28%2023:00:00&end=2018-10-28%2023:40:00

    python3 project/services/weather.py

    To look up weather data
    GET /api/v1/weather?city=[city]&start=[date1]&end=[date2]

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

Further
=======
- add cache in the api layer to improve performance,cause weather data won't change a lot
- return different data type(json,xml etc) based on user requirement
- may be add nginx in front of services
