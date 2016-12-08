"""
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
"""

import os
import subprocess
import ast


def audio_generator(dict_dir, text, output_dest):

    with open(dict_dir + "/myDict.py") as f:
        myDict = ast.literal_eval(f.read())

    # Open a text file to put in the data we receive from this module
    output_file = open(dict_dir + '/list.txt', 'w')

    # Split the text on spaces and create a list with them
    textList = text.split(" ")

    # Loop through the list to receive the address of the audio file
    # associated with the input given in speech.text
    for i in range(len(textList)):
        if textList[i] in myDict.keys():
            output_file.write("file " + myDict[textList[i]] + "\n")

    # If a file with the default name exits, create a new name with a
    # new suffix
    res = 0
    while(os.path.exists(output_dest + "/output" + str(res) + ".wav")):
        res += 1

    # Use ffmpeg to process the generated list.txt and create a new audio file
    # containing the speech of the text you had as input
    subprocess.Popen('ffmpeg -y -f concat -i ' + dict_dir +
                     '/list.txt -c copy ' + output_dest + '/output' +
                     str(res) + '.wav', shell=True, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
    print ("Success! Your requested audio file is now at " + output_dest +
           "/output" + str(res) + ".wav")
