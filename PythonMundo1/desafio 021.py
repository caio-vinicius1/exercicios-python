#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
from pygame import mixer
mixer.init()
mixer.music.load('/storage/emulated/0/snaptube/download/SnapTube Audio/Leonardo Gonçalves - Somente a Ti (Áudio Oficial)(MP3_160K).mp3')
mixer.music.play()
while mixer.music.get_busy():
	pass