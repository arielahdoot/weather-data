import sys
import json
import requests

def read_and_write(file,output_file):
	output_file.write("Location,Temperature,Wind Speed,Weather Description")
	file.next()
	for line in file:		
		url = "http://api.openweathermap.org/data/2.5/weather?q={},US&APPID=???????????????&units=imperial".format(line.strip())
		response = requests.get(url)
		json_data = json.loads(response.text)
		if json_data['cod'] == 200:
			output_file.write("\n{},{},{},{}".format(json_data['name'], json_data['main']['temp'], json_data['wind']['speed'], json_data['weather'][0]['description']))

if __name__ == '__main__':
	try:
		filename = sys.argv[1]
		file = open(filename,"r")
		output_file = open("output_file.csv","w")
		read_and_write(file,output_file)
	except Exception as e:
		print e
	else:
		file.close()
		output_file.close()
