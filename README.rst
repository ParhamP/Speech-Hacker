Speech-Hacker (New Release)
===========================
Would you like to make any famous figure speak whatever you want? Use
Speech-Hacker to train your own speaker and receive speeches spoken by
them.

Description
-----------

Speech-Hacker takes a large data base of audio speeches spoken by your
chosen figure and employs Simple Audio Indexer (Using Watson Speech API)
to split them on words and to create smaller chunks of audio files
containing those words. Finally, your desired speech's words and phrases
get associated with audio chunks that were created and converted, so
that you can receive a brand new speech spoken by your figure.

Significant Improvement in New Version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In earlier versions, Speech-Hacker was using pydub to split words based
on amount of silence between them. That worked, but it wasn't as smart
as we wanted to be. Therefore, we thought of using IBM Watson Speech API
to index words. Of course, we got much better results!
SimpleAudioIndexer was built as a separate project to help us implement
this functionality for Speech-hacker.

Samples (Trained by President Obama's Speeches)
---------------------------------------------------

.. image:: http://www.kohls.com/media/38.0.0-339/images/thumb/videoPlayer_Icon.png
	:target: https://dl.dropboxusercontent.com/s/1mhp9xz95weh4wu/output22.wav?dl=0

"Let me give you an example. When I was in Washington, I fought hard to
make sure your rights are under safety, like social security and other
things."

.. image:: http://www.kohls.com/media/38.0.0-339/images/thumb/videoPlayer_Icon.png
	:target: https://dl.dropboxusercontent.com/s/itu5156itn1usnr/output23.wav?dl=0

"Black Friday was the best thing in the world! Did you go shopping?"

.. image:: http://www.kohls.com/media/38.0.0-339/images/thumb/videoPlayer_Icon.png
	:target: https://dl.dropboxusercontent.com/s/tmi3p73hgq2k7xm/output1.wav?dl=0

"American people now should care about science more than before since we
have problems in this country."

.. image:: http://www.kohls.com/media/38.0.0-339/images/thumb/videoPlayer_Icon.png
	:target: https://dl.dropboxusercontent.com/s/piyagv6e6p8fccf/output24.wav?dl=0

"Call me on your phone so we can talk about important issues."

.. image:: http://www.kohls.com/media/38.0.0-339/images/thumb/videoPlayer_Icon.png
	:target: https://dl.dropboxusercontent.com/s/98kjcwytbaazjna/output46.wav?dl=0

"I want a better job after this because this one did not make me sick
enough!

.. image:: http://www.kohls.com/media/38.0.0-339/images/thumb/videoPlayer_Icon.png
	:target: https://dl.dropboxusercontent.com/s/gfuncimepvu9fs5/output71.wav?dl=0

"Make america great again and long live alt right! I am not sure of
course what I just said!""

Get Started
-----------

1. `Dependencies <https://github.com/ParhamP/Speech-Hacker#dependencies>`__

2. `Install <https://github.com/ParhamP/Speech-Hacker#install>`__

3. `Setup <https://github.com/ParhamP/Speech-Hacker#setup>`__

4. `Usage <https://github.com/ParhamP/Speech-Hacker#usage>`__

5. `Thanks <https://github.com/ParhamP/Speech-Hacker#thanks>`__

Dependencies
------------

1. Python 2.7

2. `Simple Audio
   Indexer <https://github.com/aalireza/SimpleAudioIndexer>`__

3. IBM Watson Speech API Username and Password

4. pydub

Install
-------

``pip install Speech-Hacker``

Setup
-----

1. Choose your figure(s).

2. Browse the internet to find reasonable amount of relatively good
   quality audio files spoken by your figure. (Convert them to WAV)

3. Place all the audio files you found in a folder

4. Acquire IBM Watson Speech to Text username and password at
   https://www.ibm.com/watson/developercloud/speech-to-text.html (For
   help visit:
   `Here <https://www.ibm.com/watson/developercloud/doc/getting_started/gs-credentials.shtml>`__)

Usage
-----

Command for training a model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Speech-Hacker -train -u IBM_USERNAME -p IBM_PASSWORD -d ABS_PATH_TO_YOUR_AUDIO_FILES_FOLDER``

Command for generating your custom speech
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Speech-Hacker -generate -d ABS_PATH_TO_TRAINED_MODEL -t "WHAT_YOU WANT_TO_SAY" -g DESTINATION_FOR_REQUESTED_AUDIO``

If you would like to generate from a text file, you can alternatively enter:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``Speech-Hacker -generate -d ABS_PATH_TO_TRAINED_MODEL -f "ABS_PATH_OF_TEXT_FILE" -g DESTINATION_FOR_REQUESTED_AUDIO``

Arguments Description:
^^^^^^^^^^^^^^^^^^^^^^

``-train`` : Training mode

``IBM_USERNAME`` : IBM Watson Speech to Text username

``IBM_PASWORD`` : IBM Watson Speech to Text password

``ABS_PATH_TO_YOUR_AUDIO_FILES_FOLDER`` : Absolute path to the folder
you placed the audio of your figure

``-generate`` : Generating mode

``ABS_PATH_TO_TRAINED_MODEL`` : Absolute path of the folder of audios
you entered when training.

``DESTINATION_FOR_REQUESTED_AUDIO`` : The destination you would like to
export your generated audio to.

Thanks
------

Many thanks to the following GitHub users for contributing code and/or
ideas:

`aalireza <https://github.com/aalireza>`__

`raphaeldore <https://github.com/raphaeldore>`__

`Stickerpants <https://github.com/Stickerpants>`__

`girishramnani <https://github.com/girishramnani>`__

`ochawkeye <https://github.com/ochawkeye>`__
