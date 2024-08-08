# Import the required module for text
# to speech conversion
from io import BytesIO
from gtts import gTTS

from pydub import AudioSegment
from pydub.playback import play

from mpyg321.mpyg321 import MPyg321Player

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'Welcome to geeksforgeeks!'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
tts = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
tts.save("vv.mp3")
#
# # Playing the converted file
# os.system("mpg321 welcome.mp3")
#
# player = MPyg321Player()
# player.play_song("welcome.mp3")

mp3_fp = BytesIO()
tts.write_to_fp(mp3_fp)

data = open('vv.mp3', 'rb').read()
data = open('vv.mp3', 'rb').read()

song = AudioSegment.from_file(BytesIO(data), format="mp3")
play(song)

