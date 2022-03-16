from flask import Flask

# 'Flask' is a class where as 'flask' is a package.

app = Flask(__name__)        #__name__ is a special python variable that provides a unique name

@app.route('/')  # This is a decorator '/' is the homepage of the application.
def home():           # decorator always acts on a method.
    return "Hello, world!"  

app.run(port=5000)  # needs a specific port


## HTTP verbs

## A "GET, POST, DELETE, PUT, OPTIONS< HEAD" are some of the HTTPS verbs

## Verb              meaning                    e.g.

## GET        Retrieve something            GET/item/1
## POST       Receive data and use it       POST/item (JSON item)
## PUT        Change/Update                 PUT/item
## DELETE     Delete item                   DELETE/item/1

## REST Principles

# Its a way of thinking of how a web server responds to the data/request


