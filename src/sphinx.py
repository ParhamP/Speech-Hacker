'''
Copyright 2016 Parham Pourdavood

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
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