# LOGICS
from ChatBoxSeturiIntrebari2 import *
from difflib import SequenceMatcher
def userPC():
	dicto=url()
	x=0
	nrIntrb = 1
	listaMaterie = ['matematica', 'romana', 'geografie', 'istorie', 'culturaGenerala', 'arte', 'sport']
	print("Vom incepecu materia: {0}".format(listaMaterie[x]))
	print("Prima intrebare: \nCalculator: {}".format(dicto[listaMaterie[x]][nrIntrb][0]))
	userInput=input("Raspuns :")

	nrIntrbReusite=0
	ok=logics(listaMaterie[x],userInput,dicto,nrIntrb)
	## {'mate':[('?','x'),('?','x')],'ro':[('?','x'),('?','x')]}
	while userInput!="exit":
		if x==8:
			print("Ai terminat tot testul !")
			break
		if ok==1:
			print("Raspuns corect !")
			nrIntrbReusite+=1
		else:
			print("Raspuns gresit...")
		
		if nrIntrbReusite/nrIntrb>0.7 and nrIntrb>5:
			print("Vom trece la alta materie ! Te descurci exelent !")
			x+=1
			nrIntrb=1
			nrIntrbReusite=0
		elif nrIntrbReusite/nrIntrb<0.3 and nrIntrb>5:
			print("Vom trece la alta materie ! Mai trebuie sa inveti putin ... !")
			x+=1
			nrIntrb=1
			nrIntrbReusite=0
		else:
			nrIntrb+=1
			print("Urmatoarea intrebare: \nCalculator: {}".format(dicto[listaMaterie[x]][nrIntrb][0]))
			userInput=input("Raspuns :")
			ok=logics(listaMaterie[x],userInput,dicto,nrIntrb)

def logics(x,userInput,dicto,nr):

	ok=text(userInput,dicto[x][nr])
	return ok

def mate(userInput,tuplu):
	for i,j in enumerate(tuplu[0]):
		if int(i) in [1,2,3,4,5,6,7,8,9,0]:
			var=j
			break
	firstvarOk=0
	secondvarOK=0
	for i in range(j,len(tuplu[0])):
		if int(i) in [1,2,3,4,5,6,7,8,9,0] and firstvarOk==0:
			firstVar=int(i)
			firstvarOk=1
		elif int(i) in [1,2,3,4,5,6,7,8,9,0] and secondvarOk==0:
			secondVar=int(i)
			secondvarOk=1
		elif i=='+':
			if firstVar+secondVar==int(userInput):
				return 1
			else:
				return 0
		elif i=='-':
			if firstVar-secondVar==int(userInput):
				return 1
			else:
				return 0
		elif i=="*":
			if firstVar*secondVar==int(userInput):
				return 1
			else:
				return 0
		elif i=='/':
			if firstVar/secondVar==int(userInput):
				return 1
			else:
				return 0


def text(userInput,intrb):
	lungimeAct=0
	text=userInput.split(" ")
	rasp=intrb[1].split(" ")
	for i in range(0,len(text)):
		if sequenceMatch(text[i],rasp[i])==True:
			lungimeAct+=1
	if lungimeAct==len(rasp):
		return 1
	else:
		return 0
		
def sequenceMatch(word1,word2):
	s = SequenceMatcher(a=word1.lower(),b=word2.lower())
	limit = 0.70
	b = s.ratio()
	if b>=limit:
		return True
	return False
