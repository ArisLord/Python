#1
liste1 = range (1,100,1)


#2
liste2=[]
for i in range(100,200):
	liste2.append(i)

#3
liste1=liste1 + liste2

#4
liste1.reverse()

#5
liste1.sort()

#6
liste3 = range (0,101,2)

#7
for i in liste3:
	if i % 10 == 0:
		liste3.remove(i)		
#8		
print("Exercice 8")
print(len(liste3))

#9
print("Exercice 9")
for i in liste3 :
	if i % 8 == 0:
		print (i)
#10
print("Exercice 10")
for i in range(0,20):
	print (liste3[i])

#11
print("Exercice 11")
for i in range(20,40):
	print (liste3[i])

#12
print("Exercice 12")
for i in range(-10,0):
	print (liste3[i])

#13
print ("Exercice 13")
liste4 = [ val for val in range(100) if val % 2 == 1]
print (liste4)

#14
print("Exercice 14")
liste5 =[1,1]
Dep=0

for i in range(0,3):
	for j in range(Dep,len(liste5)):
		liste5.append(liste5[j] + liste5[j+1])
		Dep = Dep + 1
print (liste5)

#15
print("Exercice 15")
def carre (x):
	return x*x

def parite (x):
	if x % 2 == 0:
		return True
	else:
		return False


def callback (function,liste):
	newliste =[]
	for elt in liste :
		newliste.append(function(elt))
	return newliste
#16
def callback2 (function,liste):
	newliste =[]
	for elt in liste :
		if parite(elt):		
			newliste.append(elt)
	return newliste

#17
def prodSom (x,y,i):
	return x+i,x*i
def callback3 (function,liste):
	somme = 0 
	produit = 1
	for elt in liste :
		somme , produit = function (somme,produit,elt)
	return somme,produit
print ("EXERCICE 17")
print (callback3(prodSom,[1,2,4,5]))
#18
def minMaxMoy(liste):
	somme,produit = callback3(prodSom,liste)
	moyenne = somme / len(liste)
	mini  = min (liste)
	maxi = max(liste)
	fichier = open("minMaxMoy.txt","a")
	fichier.write(" minimun "+str(mini)+" maximum "+str(maxi)+" moyenne "+str(moyenne)+"\n")

#19
liste6 = [1,2,3]
liste6bis = list(liste6)
print("Exercice 19-listes avant modif de liste6")
print(liste6)
print(liste6bis)
print("Exercice 19-listes apres modif de liste6")
liste6bis.append(9)
print(liste6)
print(liste6bis)
print("---------------------------")
print (callback(carre,liste5))
print (callback(parite,liste5))

minMaxMoy([10,18,14,20,12,16])



