import json
import urllib.request
import webbrowser
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

file = open("iss.txt", "w")
file.write("There are currently" + str(result['number']) + "astronauts on the ISS: \n\n")

people = result['people']
for person in people:
    file.write(person['name'] + " - on board " + "\n")

# print Long and Lat
g = geocoder.ip('me')

file.write("\n Your current Lat / Long is : " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")
