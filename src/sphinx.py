import speech_recognition as sr

from os import path

import os

dict = {}

speechSource = 'filtered'

r = sr.Recognizer()

# Loop through the folder of filtered audios
for root, dirs, filenames in os.walk(speechSource):
	for file in filenames:
		if file != ".DS_Store":
			with sr.AudioFile("filtered/" + file) as sourcenew:
				audio = r.record(sourcenew)
				try:
					# Send the audio file to API and get data
					udata = r.recognize_sphinx(audio).decode('utf-8')
				except sr.UnknownValueError:
					continue

				# Convert utf-8 to asciidata
				asciidata=udata.encode("ascii","ignore")

				# Create a dictionary with keys being the text data that was received and with values being relative addresses of audios
				dict[asciidata.lower()] = "filtered/" + file
				print("Process...")

dict["*pause"] = "filtered/pause.wav"
print("Success!")

# Create a file to put the generated dictionary in it
output_file = open('myDict.py', 'w')
output_file.write("myDict = " + str(dict))