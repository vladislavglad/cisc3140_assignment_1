# cisc3140_assignment_3
[![Build Status](https://travis-ci.org/vladislavglad/cisc3140_assignment_1.svg?branch=master)](https://travis-ci.org/vladislavglad/cisc3140_assignment_1)

After an Insane amount of attempts... after Travis CI spammed my Email with "Erorred Build" Messages...

Here it is! Deployed at: https://travis-heroku-deployment.herokuapp.com/

Main problems encountered:
* Build was constantly failing since in the app.py there is a line "app.run()" that allows the app to run indefinately if not stoped manually... Therfore, Travis CI was angry at that and after 10 minutes failed the build since no response from the app was given. Solution: create test.py file where you test the connection to the page with "unittest" module and ask Travis CI to run this file; this gives a definate response which satisfies Travis CI  
* Turns out there is https://travis-ci.org and https://travis-ci.com/. They are not the same thing: "org" is for public repos and uses webhooks to communicate wiht GitHub while "com" is for private repos and ask permission to connect to your account. Because of this, there was an authentication problem with Heroku, since Travis CI encrypts keys differently for each of its services. Solution: remove travis-ci.com from your account and authenticate only travis-ci.org with Heroku key with the following command: `travis encrypt $(heroku auth:token) --add deploy.api_key --org`  This encrypts the key specifically for "org" Travis.
* To deploy to the heroku you have to install gunicorn extenssion with `pip install gunicorn` and create a Procfile with one magic line in it: `web: gunicorn app:app`. (I've no Idea what it does, but it works)
* Additionaly, Heroku has Buildpacks that help with deployment; Specifically it has 'heroku/python' one that suports Django and Flask. Install with `--buildpack heroku/python` whenever creating a new app or add it manualy in your Heroku account.
* And, yeah! You need to download ***Ruby*** to install Travis command line interface and Heroku have thier own CLI which you allso have to download in order to get the Key and encrypt with Travis... 

## Why, oh why did it have to be this hard to deploy a simple flask app?

# cisc3140_assignment_1
Metadata exercise - creating a barebones api client with NASA’s api
