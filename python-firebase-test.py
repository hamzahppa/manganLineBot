import math
from firebase import firebase

firebase = firebase.FirebaseApplication('https://manganbak.firebaseio.com', None)

# define constant 
r_earth = 6378
pi = 3.1415

# define user lat long
lat = -7.5655367
lng = 110.8085373

# define boundary within 5 km of the location
bound = 0.10
new_lat1  = lat  + (bound / r_earth) * (180 / pi);
new_lat2  = lat  - (bound / r_earth) * (180 / pi);
new_lng1 = lng + (bound / r_earth) * (180 / pi) / math.cos(lat * pi/180);
new_lng2 = lng - (bound / r_earth) * (180 / pi) / math.cos(lat * pi/180);
print new_lat1, new_lat2, new_lng1, new_lng2

result = firebase.get('/dataResto', None, {'orderBy' : '"map/long"', 'startAt' : new_lng2, 'endAt' : new_lng1})
print result
# see data.py
for x, restoran in result.items():
	for y, attr in restoran.items():
		print y, attr
# will print retrieved data