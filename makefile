# Microservices Project Make File
# author: umer mansoor

VIRTUALENV = $(shell which virtualenv )

clean: shutdown
	rm -fr microservices.egg-info
	rm -fr venv

venv:
	$(VIRTUALENV) -p /usr/bin/python3 venv

install: clean venv
	. venv/bin/activate; python3 setup.py install
	. venv/bin/activate; python3 setup.py develop

launch: venv shutdown
	. venv/bin/activate; python3  project/services/weather_db.py &
	. venv/bin/activate; sudo python3  project/services/weather.py &

test: venv shutdown
	. venv/bin/activate; export ENVIRONMENT='development'; python3  project/services/weather_db.py &
	. venv/bin/activate; export ENVIRONMENT='development'; sudo python3  project/services/weather.py &

shutdown:
	ps -ef | grep "project/services/weather_db.py" | grep -v grep | awk '{print $$2}' |  xargs -r sudo kill -9
	ps -ef | grep "project/services/weather.py" | grep -v grep | awk '{print $$2}' | xargs -r sudo kill -9

