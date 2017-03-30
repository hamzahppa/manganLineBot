import math
from firebase import firebase

firebase = firebase.FirebaseApplication('https://manganbak.firebaseio.com', None)

# define constant 
r_earth = 6378
pi = 3.1415

# define user lat long
lat = -7.5651697
lng = 110.8102488

# define boundary within 5 km of the location
bound = 0.20
new_lat1  = lat  + (bound / r_earth) * (180 / pi);
new_lat2  = lat  - (bound / r_earth) * (180 / pi);
new_lng1 = lng + (bound / r_earth) * (180 / pi) / math.cos(lat * pi/180);
new_lng2 = lng - (bound / r_earth) * (180 / pi) / math.cos(lat * pi/180);
print new_lat1, new_lat2, new_lng1, new_lng2

result = firebase.get('/dataResto', None, {'orderBy' : '"map/long"', 'startAt' : new_lng2, 'endAt' : new_lng1})
final_result = {}

# see data.py
for x, restoran in result.items():
	if result[x]['map']['lat'] > new_lat2 and result[x]['map']['lat'] < new_lat1 :
		final_result.update(result[x])
# will print retrieved data

print final_result;