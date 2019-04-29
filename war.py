import json
from random import randrange

# CLASS FOR HEROES / VILLAINS
class struct:
	def __init__(self,id,name,desc,attack,health,IsVillan):
		self.id=id
		self.name = name
		self.descriere=desc
		self.attack=attack
		self.health=health
		self.isVilan=IsVillan
	def setAttack(self,newValue):
		self.attack=newValue
	def setHealth(self,newValue):
		self.health=newValue
	def getID(self):
		return self.id
	def getName(self):
		return self.name
	def getDesc(self):
		return self.descriere
	def getAttack(self):
		return self.attack
	def getHealth(self):
		return self.health
	def getIsVillan(self):
		return self.isVilan

# CLASS FOR PLANETS

class structPlanet:
	def __init__(self,id,name,desc,attackHero,healthHero,attackVil,healthVil):
		self.id=id
		self.name = name
		self.descriere=desc
		self.attackHero=attackHero
		self.healthHero=healthHero
		self.attackVil=attackVil
		self.healthVil=healthVil

	def getID(self):
		return self.id
	def getName(self):
		return self.name
	def getDesc(self):
		return self.descriere
	def getAttackHero(self):
		return self.attackHero
	def getHealthHero(self):
		return self.healthHero
	def getAttackVil(self):
		return self.attackVil
	def getHealthVil(self):
		return self.healthVil


characters=[]    # array of heroes & villains
planets=[]    # array of planets
chrH=[]
chrV=[]

# Printing the Planets's Name & description
def showPlanets(planets):
	print("1. Earth -" + planets[0].getDesc())
	print("2. Asgard -" + planets[1].getDesc())
	print("3. Xandar -"+ planets[2].getDesc())
	print("4. Conjunction -"+ planets[3].getDesc())
	print("5. Praxius IX -"+ planets[4].getDesc())

# Printing the Hero's Name & description
def showCharactersH(characters):
	print("1. Captain America -"+ characters[0].getDesc())
	print("2. Captain Marvel -" + characters[2].getDesc())
	print("3. Thor -" + characters[4].getDesc())
	print("4. Iron-Man -" + characters[6].getDesc())
	print("5. Black Panther -" + characters[7].getDesc())

# Printing the Villain's Name & description
def showCharactersV(characters):
	print("1. Thanos -" + characters[1].getDesc())
	print("2. Loki -" + characters[3].getDesc())
	print("3. Juggernaut -" + characters[5].getDesc())


#function for reading data from JSON and storing them into the arrays
def war():
	with open("characters.json", "r") as fisier:
		ex1_data = json.load(fisier)
	#print(ex1_data)
	for i in ex1_data:
		id=i['id']
		name=i['name']
		descr=i['description']
		attack=i['attack']
		health=i['health']
		isVil=i['isVillain']
		a=struct(id,name,descr,attack,health,isVil)
		characters.append(a)

	with open("planets.json", "r") as fisier:
		ex2_data = json.load(fisier)
	#print(ex2_data)
	for i in ex2_data:
		id=i['id']
		name=i['name']
		descr=i['description']
		attackH=i['modifiers']['heroAttackModifier']
		healthH=i['modifiers']['heroHealthModifier']
		attackV=i['modifiers']['villainAttackModifier']
		healthV=i['modifiers']['villainHealthModifier']
		a=structPlanet(id,name,descr,attackH,healthH,attackV,healthV)
		planets.append(a)

#returns a planet from the Planets array
def nr(arg):
	return planets[arg-1]


#returns a hero from the Characters array

def nrH(arg):
	return chrH[arg-1]

#returns a vilain from the Characters array
def nrV(arg):
	return chrV[arg-1]

#return the choosen Plant,Hero & Villain
def setUp():

	print("Please choose a planet ")
	showPlanets(planets)
	x=int(input())
	while(x<1 or x>5):
		print("Provide a valid planet")
		x = int(input())
	planet=nr(x)



	print("Please choose a Hero")
	showCharactersH(characters)
	y=int(input())
	while(y<1 or y>5):
		print("Please provide a valid hero")
		y = int(input())
	hero=nrH(y)



	print("Please choose a Villain")
	showCharactersV(characters)
	z = int(input())
	while z<1 or z>3:
		print("Please provide a valid villain")
		z = int(input())
	villain = nrV(z)
	return planet,villain,hero


# TeamMode Setup , returning a Planet and a Villain
def setUp2():
	print("Please choose a planet ")
	showPlanets(planets)
	x = int(input())
	while (x < 1 or x > 5):
		print("Provide a valid planet")
		x = int(input())
	planet = nr(x)

	print("Please choose a Villain to fight the Advengers team")
	showCharactersV(characters)
	z = int(input())
	while z < 1 or z > 3:
		print("Please provide a valid villain")
		z = int(input())
	villain = nrV(z)
	return planet, villain

# func. to creat the HeroTeam  , returning a list of heroes
def advengersTeam():
	team = []
	freq=[0,0,0,0,0]
	print("Create your TEAM !")
	showCharactersH(characters)
	print("Please choose one at a time . Type ,start' when you are done ")
	y = input()
	while (len(team)<=5):
		if (y == 'start'):
			break
		while (int(y) < 1 or int(y) > 5 ):
			print("Please provide a valid hero")
			y = input()
			if (y == 'start'):
				break
		if (y == 'start'):
			break
		if(freq[int(y)-1]==0):
			team.append(nrH(int(y)))
			freq[int(y)-1]=freq[int(y)-1]+1
			print("Choose again or type ,start' !")
			y = input()
			if (y == 'start'):
				break
			else:
				while (int(y) < 1 or int(y) > 5):
					print("Please provide a valid hero")
					y = input()
					if(y=='start'):
						break
		else:
			print("Hero already taken")
			print("Choose again or type ,start' !")
			y = input()
	return team

# func for checking HeroTeam's Health
def checkHealth(team):
	for i in team:
		if i.getHealth()>0:
			return True
	return False

# TeamMode func.
def appTeamMode():
	planet,villain=setUp2()
	team=advengersTeam()
	while(len(team)==0):
		print("You started without any heroes in your team !")
		team = advengersTeam()
	s=""
	for i in team:
		s=s+", "+i.getName()
	print("Our champions are :" + s + " VS " + villain.getName())  # displaying infos
	print("The fight is being held at {}".format(planet.getName()))
	print("--Stats updated after the planet--")

	# setting heros & villain stats after the Planet'stats
	for i in team:
		i.setAttack(planet.getAttackHero() + i.getAttack())
		i.setHealth(planet.getHealthHero() + i.getHealth())
	villain.setAttack(planet.getAttackVil() + villain.getAttack())
	villain.setHealth(planet.getHealthVil() + villain.getHealth())

	turnStart = randrange(0, len(team)+1)  # 0-villain   1,2,3 -heros

	while ( checkHealth(team) and villain.getHealth()>0):
		if turnStart==0:  # villain's turn
			dmgPerc = randrange(60, 100)  # choosing a random percentage
			dmg = int(villain.getAttack() * dmgPerc / 100)    #  calculating the dmg

			randomHero = randrange(0, len(team))
			while(team[randomHero].getHealth()<=0):
				randomHero = randrange(0, len(team))
			print(villain.getName()+"("+str(villain.getHealth())+")" + " damages "+team[randomHero].getName()+" with "+str(dmg)) #displaying infos
			team[randomHero].setHealth(team[randomHero].getHealth()-dmg)   # updating the Heath
			if(team[randomHero].getHealth()<=0):
				print(team[randomHero].getName()+ " remaining health is 0")
			else:
				print(team[randomHero].getName() + "'s remaining health is " + str(team[randomHero].getHealth()))
			turnStart=turnStart+1
		else:
			dmgPerc = randrange(60, 100)  # choosing a random percentage
			dmg = int(villain.getAttack() * dmgPerc / 100)  # calculating the dmg

			randomHero = randrange(0, len(team)) # I choose to make random for Heroes because one could fight alone vs the villain in a fight and the rest just watch
			while (team[randomHero].getHealth() <= 0):
				randomHero = randrange(0, len(team))

			print(team[randomHero].getName() + "(" + str(team[randomHero].getHealth()) + ")" + "damages with " + str(dmg))  # displaying infos
			villain.setHealth(villain.getHealth() - dmg)  # updating the Heath
			if (villain.getHealth() <= 0):
				print(villain.getName() + "'s remaining health is 0")
			else:
				print(villain.getName() + "'s remaining health is " + str(villain.getHealth()))
			turnStart=turnStart+1
			if turnStart==len(team)+1:
				turnStart=0

	# Checking who wom
	if checkHealth(team):
		print("Team wins !!")
	else:
		print("Team defetead")

	# Asking the Player if he wants to EXIT or a new Battle
	x = input(print("A new fight? (Y/N) "))
	if x == 'Y':
		appTeamMode()
	else:
		exit()


# main app
def app(planet,villain,hero):
	print("Our champions are :"+hero.getName() + " VS " + villain.getName())  # displaying infos
	print("The fight is being held at {}".format(planet.getName()))
	print("--Stats updated after the planet--")

	# setting hero & villains stats after the Planet'stats
	hero.setAttack(planet.getAttackHero() + hero.getAttack())
	hero.setHealth(planet.getHealthHero() + hero.getHealth())
	villain.setAttack(planet.getAttackVil() + villain.getAttack())
	villain.setHealth(planet.getHealthVil() + villain.getHealth())


	turnStart=randrange(0,2)  # 0 - hero   1- villain
	while hero.getHealth()>1 and villain.getHealth()>1:
		if turnStart==0:  # hero's turn
			dmgPerc=randrange(60,100)  # choosing a random percentage
			dmg=int(hero.getAttack()*dmgPerc/100) # calculating the dmg
			print(hero.getName() + "("+str(hero.getHealth())+")"+ "damages with " + str(dmg)) #displaying infos
			villain.setHealth(villain.getHealth()-dmg)   # updating the Heath
			if ( villain.getHealth() <=0):
				print(villain.getName() + "'s remaining health is 0" )
			else:
				print(villain.getName() + "'s remaining health is "+ str(villain.getHealth()))
			turnStart=1
		else:   # villain's turn
			dmgPerc = randrange(60, 100)  # choosing a random percentage
			dmg = int(villain.getAttack() * dmgPerc / 100)    #  calculating the dmg
			print(villain.getName()+"("+str(villain.getHealth())+")" + " damages with "+str(dmg)) #displaying infos
			hero.setHealth(hero.getHealth()-dmg)   # updating the Heath
			if(hero.getHealth()<=0):
				print(hero.getName() + "'s remaining health is 0")
			else:
				print(hero.getName() + "'s remaining health is " + str(hero.getHealth()))
			turnStart=0

	# Verifying who Won
	if(hero.getHealth()>0):
		print("Hero wins")
	else:
		print("Villain wins")


	# Asking the Player if he wants to EXIT or a new Battle
	x=input(print("A new fight? (Y/N) "))
	if x=='Y':
		planet, villain, hero = setUp()
		app(planet, villain, hero)
	else:
		exit()


war()
chrH = [characters[0], characters[2], characters[4], characters[6], characters[7]]
chrV = [characters[1], characters[3], characters[5]]
while(True):
	print("1.Solo mode   2.Team mode")
	x = input("Game mode:")
	if( x=='1'):
		planet,villain,hero = setUp()
		app(planet,villain,hero)
	else:
		if x=='2':
			appTeamMode()
		else:
			print("Command not found")



