import sys
import requests
import json

if len(sys.argv) != 3:
	print("Usage: executable 'Current Position' 'Destination'")
	exit()

departure = requests.get('https://api.navitia.io/v1/coverage/fr-idf/pt_objects?q=' + sys.argv[1] + '&disable_geojson=true', auth=('74c2531a-4e3e-41d3-8617-d6ed3501dd22', ''))
departure = json.loads(departure.text)["pt_objects"]

arrival = requests.get('https://api.navitia.io/v1/coverage/fr-idf/pt_objects?q=' + sys.argv[2] + '&disable_geojson=true', auth=('74c2531a-4e3e-41d3-8617-d6ed3501dd22', ''))
arrival = json.loads(arrival.text)["pt_objects"]

lines = requests.get('https://api.navitia.io/v1/coverage/fr-idf/physical_modes/physical_mode:Metro/lines?disable_geojson=true', auth=('74c2531a-4e3e-41d3-8617-d6ed3501dd22', ''))
lines = json.loads(lines.text)["lines"]

line_ids = []
for l in lines:
	line_ids.append(l['id'])


start_lines = requests.get('https://api.navitia.io/v1/coverage/fr-idf/stop_areas/' + departure[0]['id'] + '/physical_modes/physical_mode:Metro/lines?disable_geojson=true&disable_disruptions=true', auth=('74c2531a-4e3e-41d3-8617-d6ed3501dd22', ''))
start_lines = json.loads(start_lines.text)["lines"]
sl_ids = []
for line in start_lines:
	sl_ids.append(line["id"])

end_lines = requests.get('https://api.navitia.io/v1/coverage/fr-idf/stop_areas/' + arrival[0]['id'] + '/physical_modes/physical_mode:Metro/lines?disable_geojson=true&disable_disruptions=true', auth=('74c2531a-4e3e-41d3-8617-d6ed3501dd22', ''))
end_lines = json.loads(end_lines.text)["lines"]
el_ids = []
for line in end_lines:
	el_ids.append(line["id"])

