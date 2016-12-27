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

import ast
import os
from pydub import AudioSegment


def audio_generator(dict_dir, text, output_dest):

    with open(dict_dir + "/myDict.py") as f:
        myDict = ast.literal_eval(f.read())

    textList = text.split(" ")

    mainList = []

    for i in textList:
        if i in myDict.keys():
            mainList.append(AudioSegment.from_wav(dict_dir + "/" + myDict[i]))

    # Check to see if at least one word was generated
    if mainList == []:
        raise Exception('\033[91m' + "None of the words you entered was" +
                        " spoken by your figure." + '\033[0m')

    # If a file with the default name exits, create a new name with a
    # new suffix
    res = 0
    while(os.path.exists(output_dest + "/output" + str(res) + ".wav")):
        res += 1

    mainAudio = mainList[0]

    # Concatenate selected audio words
    for i in range(1, len(mainList)):
        mainAudio += mainList[i]

    # Export the joined audio
    mainAudio.export(output_dest + '/output' + str(res) + '.wav', format="wav")

    if os.path.exists(output_dest + "/output" + str(res) + ".wav"):
        print ('\033[94m' + "Speech-Hacker: " +
               "Your audio was generated at: " + output_dest + "/output" +
               str(res) + ".wav" + '\033[0m')
    else:
        print ("Speech-Hacker: " '\033[91m' +
               "Failed to generate your requested audio." + '\033[0m')
