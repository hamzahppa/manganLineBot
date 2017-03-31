import math
from firebase import firebase
from math import radians, cos, sin, asin, sqrt

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

# haevrsine formula
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    return c * r_earth

# see data.py
for x, restoran in result.iteritems():
	if result[x]['map']['lat'] > new_lat2 and result[x]['map']['lat'] < new_lat1 :
		d = haversine(lng, lat, result[x]['map']['long'], result[x]['map']['lat']) * 1000 #in meters
		print result[x]['index'], d
		distance = {'distance' : d}
		result[x].update(distance)
		# print result[x]
		# final_result.update(result[x])
		final_result[x] = result[x]
# will print retrieved data

print final_result


