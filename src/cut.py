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
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
import wave
import contextlib

# source to our speeches data base
source = 'speeches'

# loop through each speech in speeches folder
for root, dirs, filenames in os.walk(source):
	for file in filenames:
		print file
		if file != ".DS_Store":
			sound_file = AudioSegment.from_wav("speeches/" + file)
			audio_chunks = split_on_silence(sound_file, 

			    # must be silent for at least 1 millisecond
			    min_silence_len=1,

			    # consider it silent if quieter than -50 dBFS
			    silence_thresh=-50
			)

			for i, chunk in enumerate(audio_chunks):
			    out_file = "chunks/audio{0}.wav".format(i)
			    print out_file
			    print "exporting", out_file

			    # export the chunked files to chunks folder
			    chunk.export(out_file, format="wav")
			    with contextlib.closing(wave.open(out_file,'r')) as g:
				    frames = g.getnframes()
				    rate = g.getframerate()

				    # calculate the duration of the chunked WAV file
				    duration = frames / float(rate)

				    # only move the files that are between 0.5 second to 1.5 second to the filtered folder
				    if duration > 0.5 and duration < 2:
				    	os.rename(out_file, "filtered/" + "audio{0}.wav".format(i))