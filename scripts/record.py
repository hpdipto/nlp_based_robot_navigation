
import queue
import time
import os
import sounddevice as sd
import soundfile as sf

from playsound import playsound

start = time.time()

file_name = "scripts/audio.wav"
# file_name = "audio.wav"


if "audio.wav" in os.listdir("scripts/"):
	os.remove(file_name)

q = queue.Queue()

def callback(indata, frames, time, status):
	"""This is called (from a separate thread) for each audio block."""
	if status:
		print(status, file=sys.stderr)
	q.put(indata.copy())



with sf.SoundFile(file_name, mode='x', samplerate=44100, channels=2) as file:
	with sd.InputStream(samplerate=44100, channels=2, callback=callback):
		while True:
			file.write(q.get())

			# checking if record stopping signal is available or not
			with open("scripts/flag.txt", "r") as fl:
				ln = fl.readline()
				if "1" in ln:
					break