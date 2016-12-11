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
from SimpleAudioIndexer import SimpleAudioIndexer
from shutil import rmtree
import os
import subprocess


class Trainer(object):
    def __init__(self, username, password, src_dir, model):
        self.username = username
        self.password = password
        self.src_dir = src_dir
        self.model = model
        self.__enter__()

    def __enter__(self):
        for directory in ["dictionary", "dictionary/temp"]:
            if not os.path.exists("{}/{}".format(self.src_dir, directory)):
                os.mkdir("{}/{}".format(self.src_dir, directory))
        return self

    def __exit__(self, *args):
        rmtree("{}/dictionary/temp".format(self.src_dir))

    def audio_word_extractor(self, audio_file_basename, src_dir, word,
                             starting_second, ending_second, in_temp=False):
        subprocess.Popen(
            "sox {}/{} {}/dictionary{}/{}.wav trim {} {}".format(
                self.src_dir, audio_file_basename, self.src_dir,
                "/temp" * (in_temp), word, starting_second,
                ending_second - starting_second),
            shell=True).communicate()

    def dictionary_maker(self, verbose):
        temp_to_dict_dir = (
            lambda: subprocess.Popen(
                "mv {}/dictionary/temp/{}.wav {}/dictionary/{}.wav".format(
                    self.src_dir, word, self.src_dir, word),
                shell=True).communicate()
        )
        indexer = SimpleAudioIndexer(self.username, self.password,
                                     self.src_dir, verbose=verbose)
        indexer.index_audio(model=self.model)
        timestamps = indexer.get_timestamped_audio()
        for audio_basename in timestamps:
            for word_block in timestamps[audio_basename]:
                word = (word_block[0]).replace("'", "_")
                starting_second = word_block[1]
                ending_second = word_block[2]
                if verbose:
                    if word != word_block[0]:
                        print (str(word_block[0]) +
                               " contains ' character, replacing with _")
                self.audio_word_extractor(audio_basename, self.src_dir, word,
                                          starting_second, ending_second,
                                          in_temp=True)
                if verbose:
                    print ("{} was extracted from {} and saved in " +
                           "{}/dictionary/temp").format(word, audio_basename,
                                                        self.src_dir)
                try:
                    temp_word_size = os.path.getsize(
                        "{}/dictionary/temp/{}.wav".format(self.src_dir, word))
                    dict_word_size = os.path.getsize(
                        "{}/dictionary/{}.wav".format(
                            self.src_dir, word))
                    if (dict_word_size < temp_word_size):
                        temp_to_dict_dir()
                        if verbose:
                            print ("Temp version of {} has better quality, " +
                                   "moving to production").format(word)
                except OSError:
                    temp_to_dict_dir()
                    if verbose:
                        print ("{} is not in production, " +
                               "moving to production...").format(word)

    def model_maker(self):
        dict = {}
        # Flag will let us know if at least a WAV file was found to make model
        flag = False
        for file in os.listdir(self.src_dir + "/dictionary"):
            if file.endswith(".wav"):
                flag = True
                dict[file[:-4].lower().replace("_", "'")] = "dictionary/" + file
        if flag:
            # Write the generated dictionary to myDict.py
            mod_dir = self.src_dir + '/myDict.py'
            with open(mod_dir, 'w') as output_file:
                output_file.write(str(dict))
            if os.path.exists(mod_dir) and os.stat(mod_dir).st_size > 2:
                print('\033[94m' + "Success! A model was trained at " +
                      self.src_dir + '\033[0m')
            else:
                print("Your model could not be created.")
        else:
            print('\033[91m' + "Could not make a model. " +
                  "No WAV file was found in the directory you chose." +
                  '\033[0m')
