# fileDownload & Create

from bs4 import BeautifulSoup
import requests
from ChatBoxSeturiIntrebari import *
from ChatBoxSeturiIntrebari4 import *

def url():
	dicto={}
	mate,romana,geografie,istorie,culturaGenerala,arte,sport=start()
	listaMaterie=[mate,romana,geografie,istorie,culturaGenerala,arte,sport]
	for materie in listaMaterie:
		dicto[materie.getNume()]=[]
		i=0
		url=materie.getUrl()
		req=requests.get(url)
		html_doc=req.text
		soup=BeautifulSoup(html_doc,'html.parser')
		lista=(soup.find_all('p')[2].get_text()).split(" ")
		print(lista)
		while i<len(lista)-1:
			wrap=(lista[i],lista[i+1])
			dicto[materie.getNume()].append(wrap)
			i+=2
	print(dicto)
	return dicto
	# {'mate':[('?','x'),('?','x')],'ro':[('?','x'),('?','x')]}


def citireFisiereMultiple():
	dicto={}
	listaMaterie=['mate','romana','geografie','istorie','culturaGenerala','arte','sport']
	for materie in listaMaterie:
		f=open(materie+".txt",'r')
		dicto[materie]=[]
		i=0
		text=f.readlines()
		while i<len(text):
			wrap=(text[i],text[i+1])
			dicto[materie].append(wrap)
			i+=2
	return dicto