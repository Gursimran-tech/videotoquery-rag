# just sample testing that model is working or not

import whisper
import json


model = whisper.load_model("small")


# just checking that model is working or not!!
result = model.transcribe(audio = "audios/12.mp4_Exercise 1 - Pure HTML Media Player _ Sigma Web Development Course - Tutorial #12.mp4.mp3", 
                          language="hi",
                          task="translate" ,
                          word_timestamps = False)

print(result)