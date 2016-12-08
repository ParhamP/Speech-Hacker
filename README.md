# Speech-Hacker


[![IMAGE ALT TEXT](images/screen.png)](https://www.youtube.com/watch?v=pV8FQpc1NlQ "Youtube_Video" )


## Description

Would you like to make any famous figure speak whatever you want? Use Speech-Hacker to train your own speaker and receive speeches spoken by them.

Speech-Hacker takes a large data base of audio speeches spoken by your chosen figure and employes Simple Audio Indexer (Using Watson Speech API) to split them on words and to create smaller chunks of audio files containing those words. Finally, your desired speech's words and phrases get associated with audio chunks that were created and converted, so that you can receive a brand new speech spoken by your figure.


I'll show you how to get started:

   1. [Dependencies](https://github.com/ParhamP/Speech-Hacker#dependencies "Dependencies")

   2. [Install](https://github.com/ParhamP/Speech-Hacker#install "Install")

   3. [Setup](https://github.com/ParhamP/Speech-Hacker#setup "Setup")

   4. [Usage](https://github.com/ParhamP/Speech-Hacker#usage "Usage")


## Dependencies

1. Python 2.7

2. [Simple Audio Indexer](https://github.com/aalireza/SimpleAudioIndexer> "Simple Audio Indexer")

3. IBM Watson Speech API Username and Password

3. ffmpeg: `brew install ffmpeg --with-libvorbis --with-ffplay --with-theora` (Mac), `apt-get install ffmpeg libavcodec-extra-53` (Linux)


## Install

`pip install Speech-Hacker`


## Setup


1. Choose your figure(s).

2. Browse the internet to find reasonable amount of relatively good quality audio files spoken by your figure. (Convert them to WAV)

3. Place all the audio files you found in a folder

4. Acquire IBM Watson Speech to Text username and password at https://www.ibm.com/watson/developercloud/speech-to-text.html (For help visit: [Here](https://www.ibm.com/watson/developercloud/doc/getting_started/gs-credentials.shtml> "IBM_GetStarted"))


## Usage

### Command for training a model

`speech-hacker -train -u IBM_USERNAME -p IBM_PASSWORD -d ABS_PATH_TO_YOUR_AUDIO_FILES_FOLDER`


### Command for generating your custom speech

`Speech-Hacker -generate -d ABS_PATH_TO_TRAINED_MODEL -t "WHAT_YOU WANT_TO_SAY" -g DESTINATION_FOR_REQUESTED_AUDIO`



If you would like to generate from a text file, you can alternatively enter:

`Speech-Hacker -generate -d ABS_PATH_TO_TRAINED_MODEL -f "ABS_PATH_OF_TEXT_FILE" -g DESTINATION_FOR_REQUESTED_AUDIO`


## Thanks

Many thanks to the following GitHub users for contributing code and/or ideas:

[aalireza](https://github.com/aalireza> "aalireza")

[Stickerpants](https://github.com/Stickerpants> "Stickerpants")

[girishramnani](https://github.com/Stickerpants> "girishramnani")

[ochawkeye](https://github.com/ochawkeye> "ochawkeye")


