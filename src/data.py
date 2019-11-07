# - * - Coding : utf-8 - * -
import os
import requests
import json
import os
import time
import shutil
from config import getStatusUsing, setUrl, getUrl, put

path = '/home/sheylong/Documentos/Data/'
path_down = '/home/sheylong/Downloads/'

def removeDuplicate(dirs):
	for dire in dirs:
		if '(' in str(dire) and 'txt' in str(dire):
			os.remove(path_down+str(dire))
		else:
			if 'txt' in str(dire):
				shutil.move(path_down+str(dire), path)

def insertAll(lines):
	list_keys = []
	for i in range(1, len(lines)):
		key = lines[i].split('|')[0]
		list_keys.append(key)
	return list_keys

def verify(keys, list_keys):
	for key in keys:
		if str(key) not in list_keys:
			print(put(key,'Free'))
		else:
			print(put(key,'Ok'))

def data():
	isChange = raw_input("Deseja mudar a url? (S) or (N): ")

	if isChange == 'S' or isChange == 's' :
		url = raw_input("Insira o endereco da url: ")
		setUrl(str(url))
		print('A url foi alterada', getUrl())
	else:
		print('A url nao foi modificada')


	print('dirs: ')
	dirs = os.listdir(path_down)
	keys = getStatusUsing()
	print(dirs)
	removeDuplicate(dirs)
	dirs = os.listdir(path)
	print(dirs)
	list_keys = []
	for dire in dirs:
		file = open(path+str(dire))
		lines = file.readlines()
		list_keys.append(insertAll(lines))
	verify(keys, list_keys)

