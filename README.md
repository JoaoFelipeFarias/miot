# miot
middleware for IOT devices based on RESTful web API

## To use this project

### REST API
1. Configuration of working environment
```
	$ sudo apt-get install python3 python-pip
	$ sudo pip3 install virtualenv virtualenvwrapper
		Se estiver usando Pip3:
		echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
	$ echo "export WORKON_HOME=~/Env" >> ~/.bashrc
	$ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
	$ source ~/.bashrc
	$ mkvirtualenv redes_proj (or anything else you want)
```
2. Dependencies Installation
```
	CLONE PROJECT FROM GIT
	$ pip install -r requirements.txt
```
3. Run Project
```
$ sudo mongod 
$ python3 miot.py
```

### MQTT and ZMQ
1. Configuration of working environment
```
	$ sudo apt-get install mosquitto
	$ sudo apt-get install mosquitto-clients
	$ sudo apt-get install python3-zmq
	$ sudo pip3 install paho-mqtt
```
2. Run Project 
```
	$ mosquitto_sub -t '#'
	Other terminal: $ python3 w_sub_xxx.py
	Other terminal: $ python3 w_pub.py
	Other terminal: $ python3 v_sub_xxx.py
	Other terminal: Run Vinicius's code.
```
