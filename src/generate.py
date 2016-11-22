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
from myDict import *
import os
import shlex
import subprocess
# Read the text from speech.txt file
with open("myspeech.txt") as f:
	text = f.read()

# Open a text file to put in the data we receive from this module
output_file = open('list.txt', 'w')

# Split the text on spaces and create a list with them
textList = text.split(" ")

# Loop through the list to receive the address of the audio file associated with the input given in speech.text
for i in range(len(textList)):
    try:
		# We basically try to check whether we can find audio files for our input if some of them get attached
		# Therefore here we try different concatenations of elements in textList to extend our chance of finding audio files for our input
        for j in range(1,7):
            desired_key = " ".join([textList[i+x] for x in range(j) ])
            if desired_key in myDict.keys():
                # Write the found audio address in the output_file in a format that will be readible by ffmpeg
                output_file.write("file "+ myDict[desired_key] + "\n")
                break



	# Handle index errors
    except IndexError:
        continue
res = 0
while(os.path.exists("output" + str(res) + ".wav")):
    res +=1
# Use ffmpeg to process the generated list.txt and create a new audio file containing the speech of the text you had as input
subprocess.Popen('ffmpeg -y -f concat -i list.txt -c copy output' + str(res) + '.wav', shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
