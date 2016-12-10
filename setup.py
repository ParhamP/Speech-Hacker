from distutils.core import setup




setup(
  name = 'Speech-Hacker',
  packages=['Speech-Hacker'],
  version = '0.7',
  scripts=['Speech-Hacker/Speech-Hacker', 'Speech-Hacker/generator.py',
           'Speech-Hacker/trainer.py'],
  description = "Makes famous people speak whatever you wish by linking their words",
  long_description="Speech-Hacker takes a large data base of audio speeches spoken by your chosen figure and employes Simple Audio Indexer (Using Watson Speech API) to split them on words and to create smaller chunks of audio files containing those words. Finally, your desired speech's words and phrases get associated with audio chunks that were created and converted, so that you can receive a brand new speech spoken by your figure.\nIn earlier versions, Speech-Hacker was using pydub to split words based on amount of silence between them. That worked, but it wasn't as smart as we wanted to be. Therefore, we thought of using IBM Watson Speech API to detect words. Of course, we got much better results! SimpleAudioIndexer was built as a separate project to help us implement this functionality for Speech-hacker.",
  author = 'Parham Pourdavood',
  author_email = 'ppourdavood@gmail.com',
  url = 'https://github.com/parhamp/Speech-Hacker',
  download_url = 'https://github.com/parhamp/Speech-Hacker/tarball/0.7',
  keywords = ['Speech', 'Linking Words', 'Speech Hacking', 'audio', 'ibm', 'watson', 'simpleaudioindexer'], # arbitrary keywords
  classifiers = [],
  install_requires = ['SimpleAudioIndexer'],
  license="Apache-2.0"
)
