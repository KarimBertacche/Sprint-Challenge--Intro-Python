# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

  def __str__(self):
    return f"({self.name}, {self.lat}, {self.lon})"

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
import csv

cities = []

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  with open("cities.csv", "r") as csv_city:
    city_data = csv.reader(csv_city, delimiter=',')
    line_count = 0
    for record in city_data:
      if line_count == 0:
        line_count += 1
      else:
        # For each city record, create a new City instance and add it to the `cities` list
        cities.append(City(record[0], float(record[3]), float(record[4])))
        line_count += 1
    
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user
print("Pass the first set of latitude an logitude values:")
first_coordinates = input(">>> ").split(",")
print("Pass the second set of latitude an logitude values:")
second_coordinates = input(">>> ").split(",")

# print(first_coordinates)
# print(second_coordinates)

[lat1, lon1] = [first_coordinates[0].strip(), first_coordinates[1].strip()]
[lat2, lon2] = [second_coordinates[0].strip(), second_coordinates[1].strip()]

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):

  # TODO Ensure that the lat and lon valuse are all floats
  min_lat = float(lat1) if lat1 < lat2 else float(lat2)
  max_lat = float(lat1) if lat1 > lat2 else float(lat2)
  min_lon = float(lon1) if lon1 < lon2 else float(lon2)
  max_lon = float(lon1) if lon1 > lon2 else float(lon2)
  
  # within will hold the cities that fall within the specified region
  within = []

  # Go through each city and check to see if it falls within
  # the specified coordinates.
  for city in cities:
    if (city.lat > min_lat and city.lat < max_lat) and (city.lon > min_lon and city.lon < max_lon):
        within.append(city) 

  for city in within:
    print(f"name:{city.name}, lat:{city.lat}, lon:{city.lon}")

  return within