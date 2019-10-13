import sys
import requests

if len(sys.argv) != 3:
	print("Usage: executable 'Current Position' 'Destination'")
	exit()

request = requests.get('https://api.navitia.io/v1/coverage/sandbox/pt_objects?q=etro%200', auth=('3b036afe-0110-4202-b9ed-99718476c2e0', ''))
print(request.text)
