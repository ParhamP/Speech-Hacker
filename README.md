# Speech-Hacker


[![IMAGE ALT TEXT](images/screen.png)](https://www.youtube.com/watch?v=pV8FQpc1NlQ "Youtube_Video" )


## Description

Would you like to make any famous figure speak whatever you want? Use Speech-Hacker to train your own speaker and receive speeches spoken by them.

Speech-Hacker takes a large data base of audio speeches spoken by your chosen figure and employs Simple Audio Indexer (Using Watson Speech API) to split them on words and to create smaller chunks of audio files containing those words. Finally, your desired speech's words and phrases get associated with audio chunks that were created and converted, so that you can receive a brand new speech spoken by your figure.


### Significant Improvement in New Version

In earlier versions, Speech-Hacker was using pydub to split words based on amount of silence between them. That worked, but it wasn't as smart as we wanted to be. Therefore, we thought of using IBM Watson Speech API to detect words. Of course, we got much better results! SimpleAudioIndexer was built as a separate project to help us implement this functionality for Speech-hacker. 



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

`Speech-Hacker -train -u IBM_USERNAME -p IBM_PASSWORD -d ABS_PATH_TO_YOUR_AUDIO_FILES_FOLDER`


### Command for generating your custom speech

`Speech-Hacker -generate -d ABS_PATH_TO_TRAINED_MODEL -t "WHAT_YOU WANT_TO_SAY" -g DESTINATION_FOR_REQUESTED_AUDIO`



#### If you would like to generate from a text file, you can alternatively enter:

`Speech-Hacker -generate -d ABS_PATH_TO_TRAINED_MODEL -f "ABS_PATH_OF_TEXT_FILE" -g DESTINATION_FOR_REQUESTED_AUDIO`




#### Arguments Description:

`-train` : Training mode

`IBM_USERNAME` : IBM Watson Speech to Text username

`IBM_PASWORD` : IBM Watson Speech to Text password

`ABS_PATH_TO_YOUR_AUDIO_FILES_FOLDER` : Absolute path to the folder you placed the audio of your figure

`-generate` : Generating mode

`ABS_PATH_TO_TRAINED_MODEL` : Absolute path of the folder of audios you entered when training.

`DESTINATION_FOR_REQUESTED_AUDIO` : The destination you would like to export your generated audio to. 




## Samples



#### I trained President Obama's speeches and here are some audio samples that I generated. Take a listen! (I made some of them to be twisted and funny. No offense :D)





"Let me give you an example. When I was in Washington, I fought hard to make sure your rights are under safety, like social security and other things."

[![IMAGE ALT TEXT](images/player2.png)](https://dl.dropboxusercontent.com/s/1mhp9xz95weh4wu/output22.wav?dl=0
 "Audio_Sample" )



"Black Friday was the best thing in the world! Did you go shopping?"

[![IMAGE ALT TEXT](images/player2.png)](https://dl.dropboxusercontent.com/s/itu5156itn1usnr/output23.wav?dl=0 "Audio_Sample" )



"American people now should care about science more than before since we have problems in this country."

[![IMAGE ALT TEXT](images/player2.png)](https://dl.dropboxusercontent.com/s/tmi3p73hgq2k7xm/output1.wav?dl=0 "Audio_Sample" )



"Call me on your phone so we can talk about important issues."

[![IMAGE ALT TEXT](images/player2.png)](https://dl.dropboxusercontent.com/s/piyagv6e6p8fccf/output24.wav?dl=0 "Audio_Sample" )



"I want a better job after this because this one did not make me sick enough!

[![IMAGE ALT TEXT](images/player2.png)](https://dl.dropboxusercontent.com/s/98kjcwytbaazjna/output46.wav?dl=0 "Audio_Sample" )


Make america great again and long live alt right! I am not sure of course what I just said!

[![IMAGE ALT TEXT](images/player2.png)](https://dl.dropboxusercontent.com/s/gfuncimepvu9fs5/output71.wav?dl=0 "Audio_Sample" )



## Thanks

Many thanks to the following GitHub users for contributing code and/or ideas:

[aalireza](https://github.com/aalireza> "aalireza")

[Stickerpants](https://github.com/Stickerpants> "Stickerpants")

[girishramnani](https://github.com/girishramnani> "girishramnani")

[ochawkeye](https://github.com/ochawkeye> "ochawkeye")


