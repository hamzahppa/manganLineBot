#!/usr/bin/python
import math
import simplejson as json
from pyrebase import pyrebase

config = {
	"apiKey": "AIzaSyB1U7icSEQX4ZTCdsRHxDUFieD-r7sDFKA",
    "authDomain": "manganbak.firebaseapp.com",
    "databaseURL": "https://manganbak.firebaseio.com",
    "storageBucket": "manganbak.appspot.com"
}

#define new firebase app
firebase = pyrebase.initialize_app(config)
# define database ref
db = firebase.database()
restoran = firebase.database().child('dataResto')

# define constant 
r_earth = 6378
pi = 3.1415

# define user lat long
lat = -7.569524
lng = 110.830291

# define boundary within 5 km of the location
new_lat1  = lat  + (5 / r_earth) * (180 / pi);
new_lat2  = lat  - (5 / r_earth) * (180 / pi);
new_lng1 = lng + (5 / r_earth) * (180 / pi) / math.cos(lat * pi/180);
new_lng2 = lng - (5 / r_earth) * (180 / pi) / math.cos(lat * pi/180);
print(new_lat1, new_lat2, new_lng1, new_lng2)

resto = db.child('dataResto').child(0).get()

# retrieve data resto by location
restoran_rad5 = restoran.order_by_child("map/lat").start_at(new_lat1).end_at(new_lat2).shallow()