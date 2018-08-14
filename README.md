# looking_good_data
Simple API project for simulating a online store data service with multiple input sources

## Stack

The stack bellow was used mostly due to it's ease of installation, configuration and also efficiency and portability.
* Language: Python (3.5)
* Framework: Django (2.1)
* DB: SQLite (3.16.2)

## Pre-installation

This system was developed in Ubuntu 16.04, but will work properly on any other Operational System(OS X, Windows, etc.).

However, this guide will only include instructions for plugins and packages that are not already installed on this OS. For this reason, we assume that technologies like a python interpreter and SQLite are ready for use, and should not be on the scope of this document.

* Now install pipenv dependency manager:

```bash

$ pip install --user pipenv

```

## Project configuration and deployment

Now we'll start setting up the project.

* Clone the repo from github and change to project root directory. After that install project dependencies and go to python virtual env, by running:

```bash
$ pipenv install
$ pipenv shell
```

* Setup DB:

```bash
$ ./manage.py migrate
```

* Run tests to verify that everything is working fine:

```bash
$ ./manage.py test
```

* Open a new bash terminal window on the same folder path and start server
```bash
$ ./manage.py runserver
```

* Populate DB
```bash
$ 
