"""
--------------------------------------------------------------------------
Wakey Wakey - WiFi
--------------------------------------------------------------------------
License:   
Copyright 2022 Garrett French

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Use three buttons, a Wifi module, a Bluetooth module, and a GPS module for an
alarm clock that has spatial awareness, can tell weather data for its current
location, and can perform the regular functions of an alarm clock.

Sourced codes:
https://www.geeksforgeeks.org/get-the-city-state-and-country-names-from-latitude-and-longitude-using-python/
https://stackoverflow.com/questions/33997361/how-to-convert-degree-minute-second-to-degree-decimal

"""
import time
import datetime
import requests
from geopy.geocoders import Nominatim
import re

YOUR_API_KEY = "Enter your API Key here"

def internet_on():
	print ('Checking Internet Connection')
	try:
		r =requests.get('https://api.amazon.com/auth/o2/token')
	        print ('Connection OK')
		return True
	except:
		print ('Connection Failed')
		return False
		
def find_weather(self, lat, lon, date):
    # lat/lon is in the format '''51°36'9.18"N'''
 
 
	# initialize Nominatim API
	geolocator = Nominatim(user_agent="geoapiExercises")
 
	# Need to take in Latitude and Longitude values from GPS module
	[lat, lon] = gps.get_coordinates()
	
	deg, minutes, seconds, direction =  re.split('[°\''']', lat)
	Latitude = (float(deg) + float(minutes)/60 + float(seconds)/(60*60)) * (-1 if direction in ['W', 'S'] else 1)
	
	deg, minutes, seconds, direction =  re.split('[°\''']', lon)
	Longitude = (float(deg) + float(minutes)/60 + float(seconds)/(60*60)) * (-1 if direction in ['W', 'S'] else 1)
	
	
	# Latitude & Longitude input
	print(Latitude)
	print(Longitude)
	# Latitude = "25.594095"
	# Longitude = "85.137566"
	
	# Latitude & Longitude 
 
	location = geolocator.reverse(Latitude+","+Longitude)
 
	address = location.raw['address']
 
	# Traverse the GPS data
	city = address.get('city', '')
	state = address.get('state', '')
	country = address.get('country', '')
	print('City : ', city)
	print('State : ', state)
	print('Country : ', country)
	
	time = float(time.time())
	
	# Pull weather data from API
	url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{0},{1}/{2}?key={3}".format(city, country, time, YOUR_API_KEY)
	wdata = requests.get(url)

	tempmax = re.search('tempmax":(.+?),"tempmin', wdata)
	tempmin = re.search('tempmin":(.+?),"temp') wdata)
	tempcur = re.search('temp":(.+?),"feelslikemax', wdata)
	
	print('Temperature - Daily High = ')
	print(tempmax)
	print('Temperature - Daily Low = ')
	print(tempmin)
	print('Temperature - Current = ')
	print(tempcur)