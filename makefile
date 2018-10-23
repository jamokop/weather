# Microservices Project Make File
# author: umer mansoor

VIRTUALENV = $(shell which virtualenv )

clean: shutdown
	rm -fr microservices.egg-info
	rm -fr venv

venv:
	$(VIRTUALENV) -p /usr/bin/python3 venv

install: clean venv
	. venv/bin/activate; python setup.py install
	. venv/bin/activate; python setup.py develop

launch: venv shutdown
	. venv/bin/activate; python  project/services/spider.py &
	. venv/bin/activate; python  project/services/weather_db.py &
	#. venv/bin/activate; python  project/services/weather_api.py &

shutdown:
	ps -ef | grep "project/services/spider.py" | grep -v grep | awk '{print $$2}' | xargs -r sudo kill -9
	ps -ef | grep "project/services/weather_db.py" | grep -v grep | awk '{print $$2}' |  xargs -r sudo kill -9
	#ps -ef | grep "project/services/weather_api.py" | grep -v grep | awk '{print $$2}' | xargs -r sudo kill -9

