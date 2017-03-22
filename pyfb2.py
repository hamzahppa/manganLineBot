#!/usr/bin/python
import math
import urllib.request
import urllib.parse
import requests
from firebase import firebase
firebase = firebase.FirebaseApplication('https://manganbak.firebaseio.com', None)

# define constant 
r_earth = 6378
pi = 3.1415

# define user lat long
lat = -7.5655367
lng = 110.8085373

# define boundary within 5 km of the location
bound = 2
new_lat1  = lat  + (bound / r_earth) * (180 / pi);
new_lat2  = lat  - (bound / r_earth) * (180 / pi);
new_lng1 = lng + (bound / r_earth) * (180 / pi) / math.cos(lat * pi/180);
new_lng2 = lng - (bound / r_earth) * (180 / pi) / math.cos(lat * pi/180);
print(new_lat1, new_lat2, new_lng1, new_lng2)

# get data resto from firebase
restorans = firebase.get('/dataResto', None)

# use param to query
restoran_params = firebase.get('/dataResto', None, params={'orderBy':'"map/long"', 'startAt': new_lng2, 'endAt': new_lng1})
#still error

# optional use http request
# define parameter
# params = {
# 	"orderBy" : "map/long",
# 	"startAt" : new_lng2,
# 	"endAt" : new_lng1
# }
# paramsencoded = urllib.parse.urlencode(params)

# restoran = urllib.request.urlopen('https://manganbak.firebaseio.com/dataResto.json?'+ paramsencoded).read()
# print(restoran)

results = requests.get("https://manganbak.firebaseio.com/dataResto.json", 
              params={'orderBy': '"map/long"', 'startAt': new_lng2, 'endAt': new_lng1})
print(results.content)