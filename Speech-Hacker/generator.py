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
from distutils.spawn import find_executable


def audio_generator(dict_dir, text, output_dest):

    with open(dict_dir + "/myDict.py") as f:
        myDict = ast.literal_eval(f.read())

    # Open a text file to put in the data we receive from this module
    with open(dict_dir + '/list.txt', 'w') as f:
        # output_file = f.read()

        # Split the text on spaces and create a list with them
        textList = text.split(" ")

        # Loop through the list to receive the address of the audio file
        # associated with the input given in speech.text
        for i in range(len(textList)):
            if textList[i] in myDict.keys():
                f.write("file " + myDict[textList[i]] + "\n")

    # Check to see if the file is not empty (at least a word was generated)
    if os.stat(dict_dir + '/list.txt').st_size == 0:
        raise Exception('\033[91m' + "None of the words you entered was" +
                        " spoken by your figure." + '\033[0m')

    # If a file with the default name exits, create a new name with a
    # new suffix
    res = 0
    while(os.path.exists(output_dest + "/output" + str(res) + ".wav")):
        res += 1

    # Check to see if either ffmpeg or avconv is installed and assigns it
    ffmpeg = os.path.basename(find_executable("ffmpeg") or
                              find_executable("avconv"))
    if ffmpeg is None:
        raise Exception("Either ffmpeg or avconv is needed. " +
                        "Neither is installed or accessible")

    # Use ffmpeg to process the generated list.txt and create a new audio file
    # containing the speech of the text you had as input
    subprocess.Popen(ffmpeg + ' -y -f concat -i ' + dict_dir +
                     '/list.txt -c copy ' + output_dest + '/output' +
                     str(res) + '.wav', shell=True,
                     universal_newlines=True).communicate()
    # Delete the unecessary files that was made for ffmpeg use
    os.remove(dict_dir + '/list.txt')

    if os.path.exists(output_dest + "/output" + str(res) + ".wav"):
        print ('\033[94m' + "Speech-Hacker: " +
               "Your audio was generated at: " + output_dest + "/output" +
               str(res) + ".wav" + '\033[0m')
    else:
        print ("Speech-Hacker: " '\033[91m' +
               "Failed to generate your requested audio." + '\033[0m')
