import speech_recognition as sr

from os import path

import os

# Enter username and password of IBM speech to text API

IBM_USERNAME = "" # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX

IBM_PASSWORD = "" # IBM Speech to Text passwords are mixed-case alphanumeric strings

dict = {}

speechSource = 'filtered'

r = sr.Recognizer()

# Loop through the folder of filtered audios
for root, dirs, filenames in os.walk(speechSource):
	for file in filenames:
		print file
		with sr.AudioFile("filtered/" + file) as sourcenew:
			audio = r.record(sourcenew)
			try:
				# Send the audio file to API and get data
				udata = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD).decode('utf-8')
			except sr.UnknownValueError:
				continue

			# Convert utf-8 to asciidata
			asciidata=udata.encode("ascii","ignore")[:-1]

			# Create a dictionary with keys being the text data that was received and with values being relative addresses of audios
			dict[asciidata] = "filtered/" + file

# Create a file to put the generated dictionary in it
output_file = open('myDict.py', 'w')
output_file.write("myDict = " + str(dict))