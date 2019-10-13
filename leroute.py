import sys
import requests
import json

if len(sys.argv) != 3:
	print("Usage: executable 'Current Position' 'Destination'")
	exit()

departure = requests.get('https://api.navitia.io/v1/coverage/fr-idf/physical_modes/physical_mode:Metro/lines', auth=('74c2531a-4e3e-41d3-8617-d6ed3501dd22', ''))
print(departure.text)

# print("\n--------------- --------------------\n")

# arrival = requests.get('https://api.navitia.io/v1/coverage/fr-idf/pt_objects?q=' + sys.argv[2], auth=('74c2531a-4e3e-41d3-8617-d6ed3501dd22', ''))
# # print(arrival.text)

# print (json.loads(arrival.text)["pt_objects"])