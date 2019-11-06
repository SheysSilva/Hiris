import requests
import json

url = 'localhost'
port = '8080'

def setUrl(url):
	url = url

def getStatusUsing():
	get = requests.get('http://'+url+':'+port+'/using/')
	return get.json()

def getStatusOk():
	get = requests.get('http://'+url+':'+port+'/ok/')
	return get.json()

def getStatusFree():
	get = requests.get('http://'+url+':'+port+'/free/')
	return get.json()

def getKeys():
	get = requests.get('http://'+url+':'+port+'/chaves/')
	return get.json()

def getKeyId(id):
	get = requests.get('http://'+url+':'+port+'/chaves/'+srt(id))
	return get.json()

def setStatus(id, status):
	sett = requests.get('http://'+url+':'+port+'/set/')
	return sett.json()

def post(id):
	post = requests.post('http://'+url+':'+port+'/chaves/', data={'id': str(id)})
	return post.json()

def put(id, status):
	put = requests.put('http://'+url+':'+port+'/chaves/', data={'id': str(id), 'status': str(status)})
	return put.json()

def deletAll():
	delete = requests.delete('http://'+url+':'+port+'/chaves/')
	return delete.json()

def delete(id):
	delete = requests.delete('http://'+url+':'+port+'/chaves/', data={'id': str(id)})
	return delete.json()

