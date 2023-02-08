'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.
NOTE: No hard-coding allowed except for keys for the dictionaries
1) print out the number of earthquakes
2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a
   magnitude > 6. Print out the new dictionary.
3) using the eq_dict dictionary, print out the information as shown below (first 
three shown):
Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364
Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604
Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628
'''
import json
infile = open('eq_data.json', 'r')
eq = json.load(infile)
print('Number of Earthquakes:', eq['metadata']['count'])
eq_dict = {}
for i in eq['features']:
    magnitude = i['properties']['mag']
    if magnitude > 6:
        location = i['properties']['place']
        latitude = i['geometry']['coordinates'][1]
        longitude = i['geometry']['coordinates'][0]
        eq_dict[location] = {'Magnitude': magnitude,
                             'Latitude': latitude, 'Longitude': longitude}

print(eq_dict)

for key, value in eq_dict.items():
    print(f'Location: {key}')
    print('Magnitude:', eq_dict[key]['Magnitude'])
    print('Longitude:', eq_dict[key]['Longitude'])
    print('Latitude:', eq_dict[key]['Latitude'], '\n')

# if you use hardcoded key [""] it will replace the original key
# if you use a variable in a key with no quotes, if the value of the variable changes it will make new key value pair
