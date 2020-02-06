
from django.shortcuts import render

from subprocess import run, PIPE
import subprocess as sp
import sys
import os
import requests as req

default_link = "https://www.mapquest.com/embed/latlng/23.727598,90.400471?center=23.72753844935974,90.40088564157486&zoom=18&maptype=map"
spoken_text = ""


def home(request):
	return render(request, 'layout.html', {'map_link':default_link})



def record(request):

	out = run([sys.executable, 'scripts/record.py'], shell=False, stdout=PIPE)

	return render(request, 'layout.html')




def output(request):

	with open("scripts/flag.txt", "w") as fl:
		fl.write("1")

	out = run([sys.executable, 'scripts/voice_to_text.py'], shell=False, stdout=PIPE)   # argument will comes after comma
	out = str(out.stdout)[2:-3]

	#global spoken_text
	spoken_text = out

	f = open("scripts/flag.txt", "w")
	f.close()

	return render(request, 'layout.html', {'text':out, 'map_link':default_link})





def route(request):

	# print("##",)

	
	input_text = request.POST.get("input_text")

	out = run([sys.executable, 'scripts/route_generation.py', input_text], shell=False, stdout=PIPE)   # argument will comes after comma
	out = str(out.stdout)[2:-3]

	# global default_link
	# default_link = out
	# out = default_link

	return render(request, 'layout.html', {'map_link':out, 'text': input_text})
