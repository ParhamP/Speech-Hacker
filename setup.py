from distutils.core import setup

setup(
  name = 'Speech-Hacker',
  packages=['Speech-Hacker'],
  version = '0.3',
  scripts=['Speech-Hacker/Speech-Hacker', 'Speech-Hacker/generator.py',
           'Speech-Hacker/trainer.py'],
  description = "Makes famous people speak whatever you wish by linking their words",
  long_description="Speech-Hacker takes a large data base of audio speeches spoken by your chosen figure and employes Simple Audio Indexer (Using Watson Speech API) to split them on words and to create smaller chunks of audio files containing those words. Finally, your desired speech's words and phrases get associated with audio chunks that were created and converted, so that you can receive a brand new speech spoken by your figure.",
  author = 'Parham Pourdavood',
  author_email = 'ppourdavood@gmail.com',
  url = 'https://github.com/parhamp/Speech-Hacker',
  download_url = 'https://github.com/parhamp/Speech-Hacker/tarball/0.1',
  keywords = ['Speech', 'Linking Words', 'Speech Hacking', 'audio', 'ibm', 'watson', 'simpleaudioindexer'], # arbitrary keywords
  classifiers = [],
  install_requires = ['SimpleAudioIndexer'],
  license="Apache-2.0"
)
