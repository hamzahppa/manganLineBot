# Welcome to MANGAN Bot on Line

## UPDATED!
## python-firebase-test.py
- pure python 2
- use lib python-firebase by ozgur https://github.com/ozgur/python-firebase
- retrieve data by location (longitude) success. Try to change bounds ( 0.10 - 5.00 ). bounds is in KM, so 0.10 means 0.10 KM and so on

## data.py
Single data structure that retrieved from database


## getData.py
use pyrebase with python 3. Not support python 2

## pyfb2.py
use python-firebase with python 3. Support python 2

## Scheme
Define boundary. See code for the equation

1. Get data from firebase by location (define as "map/long" on "dataResto")
	Use query starAt and endAt. See https://firebase.google.com/docs/database/rest/retrieve-data

2. Filter again with latitude from retrieved data to get final data

3. Use google distancematrix to get estimated distance/ETA and etc.

## problem
### getData.py
1. Success retrieve data then need to query with startAt and endAt using
`restoran_rad5 = restoran.order_by_child("map/lat").start_at(new_lat1).end_at(new_lat2).shallow()`
2. Fail to read data. I dont know how to read the data

### pyfb2.py
1. Cannot use query because there is no function. Alternative, use the http request or use the params from this repo https://github.com/ozgur/python-firebase

