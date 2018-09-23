from collections import namedtuple
LatLong = namedtuple('LatLong', 'lat long')
City = namedtuple("SHITE", ['name', 'country', 'population', 'coordinates'])
portland = City('Portland', 'US', 1000000, LatLong(45.51, 122.65))

print(portland)

print(City._make(portland))

print('bloop')