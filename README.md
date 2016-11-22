# Speech-Hacker


[![IMAGE ALT TEXT](images/screen.png)](https://www.youtube.com/watch?v=pV8FQpc1NlQ "Youtube_Video" )


## Description

Would you like to make any famous figure speak whatever you want? Use Speech-Hacker to train your own speaker and receive speeches spoken by them.

Speech-Hacker takes a large data base of audio speeches spoken by your chosen figure and uses PyDub to split them on words based on the amount of silence between them. It then creates smaller chunks of audio files containing words or small phrases. Speech-Hacker then uses the SpeechRecognition Library to convert audio chunks to text. At the end, your desired speech's words and phrases get associated with chunks of audio that were created and converted, so that you can receive a brand new speech spoken by your figure.

I'll show you how to get started:

   1. [Dependencies](https://github.com/ParhamP/Speech-Hacker#dependencies "Dependencies")

   2. [Install](https://github.com/ParhamP/Speech-Hacker#install "Install")

   3. [Up and Running](https://github.com/ParhamP/Speech-Hacker#up-and-running "Up and Running")

   4. [Usage](https://github.com/ParhamP/Speech-Hacker#usage "Usage")


## Dependencies

1. Python 2.7

2. PyDub: `pip install pydub`

3. SpeechRecognition: `pip install SpeechRecognition`

4. ffmpeg: `brew install ffmpeg --with-libvorbis --with-ffplay --with-theora` (Mac), `apt-get install ffmpeg libavcodec-extra-53` (Linux)


## Install

Download or `git clone https://github.com/ParhamP/Speech-Hacker.git`

## Up and Running

1. Choose your figure(s).

2. Browse the internet to find hours of relatively good quality audio files spoken by your figure. (Convert them to WAV)

3. cd to Speech-Hacker/src

4. Place your audio files you got in "speeches" folder.

5. In terminal enter: `python cut.py`.

6. Now, you have two choices for using SpeechRecognition:

	#### 1. IBM Watson (Excelent Quality) (Online)

	- Sign up at https://www.ibm.com/watson/developercloud/speech-to-text.html and obtain an IBM Watson Speech to text username and password.

	- Open watson.py with your IDE and enter your username and password for IBM_USERNAME and IBM_PASSWORD

	- In terminal enter: `python watson.py`

	#### 2. Or Sphinx (Ok Quality) (Offline)

	- In terminal enter: `python sphinx.py`

**Notice** : Step 6 may take hours to process. BUT, You only need to do the Up and Running steps once and from here you will only use the data base that you built to make speeches.

## Usage

1. cd to Speech-Hacker/src

2. Open myspeech.txt and type whatever you want your figure to say. 

	>**Notice:**  
	> * You can take a look at myDict.py and have a quick glance over all the words and phrases that were created  
	> * Save the file.  
	> * To make the speaker pause, type *pause whenever you want.  
	> * Only use lower case letters  
	> * Don't use periods, commas or other non-alphabetic characters   

3. In terminal enter: `python generate.py`

4. Tada! An audio file for the requested speech is created in the directory. 
