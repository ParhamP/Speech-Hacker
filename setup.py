from distutils.core import setup
import codecs
from os import path


here = path.abspath(path.dirname(__file__))

with codecs.open(path.join(here, 'README.md'), "rb", "utf-8") as f:
    long_description = f.read()

setup(
  name = 'Speech-Hacker',
  packages=['Speech-Hacker'],
  version = '0.4',
  scripts=['Speech-Hacker/Speech-Hacker', 'Speech-Hacker/generator.py',
           'Speech-Hacker/trainer.py'],
  description = "Makes famous people speak whatever you wish by linking their words",
  long_description=long_description,
  author = 'Parham Pourdavood',
  author_email = 'ppourdavood@gmail.com',
  url = 'https://github.com/parhamp/Speech-Hacker',
  download_url = 'https://github.com/parhamp/Speech-Hacker/tarball/0.1',
  keywords = ['Speech', 'Linking Words', 'Speech Hacking', 'audio', 'ibm', 'watson', 'simpleaudioindexer'], # arbitrary keywords
  classifiers = [],
  install_requires = ['SimpleAudioIndexer'],
  license="Apache-2.0"
)
