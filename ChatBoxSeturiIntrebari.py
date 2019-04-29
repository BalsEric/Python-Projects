def citire(x):
	numeF=""
	lista=[]
	numeF="date"+str(x)+".txt"
	f=open(numeF,'r')
	l1=readline()
	l2=readline()
	while len(l1)>0 and len(l2)>0:
		lista.append(st)
		st=(l1,l2)
		l1=readline()
		l2=readline()
	lista.append(st)
	f.close()
	return lista
from random import random
def run():
	x=int(input("Cate domenii doriti?"))
	nr=random(0,x)
	print(citire(nr))
run()