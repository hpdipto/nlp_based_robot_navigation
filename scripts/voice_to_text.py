
# source: https://realpython.com/python-speech-recognition/

import os
import speech_recognition as sr


r = sr.Recognizer()


# usually this notation is wrong but django need this way of specifying the path
sound = "scripts/audio.wav"


# snd = AudioSegment.from_mp3(audio_file)
# snd.export(sound, format="wav")

voice = sr.AudioFile(sound)

with voice as source:
	# audio = r.record(source)

	# for noisy audio
	r.adjust_for_ambient_noise(source)
	audio = r.record(source)

try:
	text = r.recognize_google(audio)
except:
	text = "Please speak loudly!"

print(text)
