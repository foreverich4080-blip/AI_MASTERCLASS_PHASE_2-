# this week we will learn how software talks to another software.
# by sending api requests, reading json, protecting your api keys band calling api keys from python and javascripts.
# apis are how your code talks to other services , other database, and other systems.
#  what is an api
# an api (application programming interface) is the way one program talks to another program .
# example mt5 talking with the python or economic data calender talking to python or javascripts.
# as a developer apis is how you give your programs superpowers.
#


# STEP 1.

# YOU SEND A REQUESTS   your code send an HTTP request to a url where url is the address of the api.
# when sending requests is just like normal browsing but at now its being done by the python automatically.
#

# STEP 2 .

# the api process the requests , then the server receive the requests, then check if you are allowed tro make it, run whatever logic is needed to and then prepare the response.


# STEP 3.
# YOU THEN receive the response as the json format which is the way that can be read by both humans and by computers.
# you then parse it and use what you only needed

#  HTTP HAS DIFFERENT FORMAT TODAY WE WILL LOOK AT GRT AND POS WHERE GET IS TO LOOK FOR A CERTAIN AINFORMATION FROM A SERVER WHILE POS IS TO UPDATE OR POST A CERTAIN INFORMATION INSIDE A SERVER.

# we will use the REST  which is the world apis and has no keys to manage

# day 1 examples.

import requests

url ="https://restcountries.com/v3.1/name/kenya"

response = requests.get(url)
print("status code:",response.status_code)
print("data received",response.json())
status = response.status_code
if status == 200:
    data = response.json()
    print("data received",data)



success = 200
not_found = 404
not_authorized = 401
too_many_requests = 429
server_errors = 500

 # always check the status code before trusting any data.


# reading the api documentation.
# every api has the documentation thats tell what requests is accepted and what it sends back.
# always choose a good documentation when looking for the api to work with as a developer.

# look for this in apis.
# 1 look for the BASE URL to know the root address that all the address start at.
# 2 look for the  ENDPOINT  to know specific paths you add to the base url to get different data .
# 3 look for PARAMETERS  to know options you can add to control the output.
# look for authentication weather you need a key or account to use it.
# look for RATE LIMITS to know how many requests are allowed per minutes per hour oe even per day , this avoid you from being burned by the server.
#



# HTTP = HYPER TEXT TRANSFER PROTOCOL.


import requests

API_KEY = "rc_live_YOUR_KEY_HERE"  # paste your key
headers = {"Authorization": f"Bearer {API_KEY}"}

r = requests.get("https://api.restcountries.com/countries/v5?region=Africa", headers=headers)
print(r.json())














