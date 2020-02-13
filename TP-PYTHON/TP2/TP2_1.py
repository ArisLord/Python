import numpy as np

#-----------------EXERCICE 1-----------------------------------#

#1
#6
alea6 = np.random.seed(42)
#1
Alea = np.random.rand(10)

#2
Alea2 = np.random.randint(0,100,100)

#3
Alea3 = np.random.randn(25)

#4
alea5 = np.random.rand(25)

#5
Alea5 = np.random.randint(0,100,(10,10))


#---------------------Les Entrees-Sorties--------------------------#

#1

np.savetxt("Alea5.csv",Alea5, delimiter = ",")

#2
load = np.genfromtxt("Alea5.csv",delimiter =",")


#-------------------------EXERCICE 2-------------------------------#

import matplotlib.pyplot as plt
"""
#1
tab1 = [1,4,8,9]
tab2 = [12,25,34,78]


plt.scatter(tab1,tab2)
plt.title('Nuage de point tab1 et tab2')

plt.xlabel('x')
plt.ylabel('y')
#plt.show()

#2
tab3 = np.random.randint(0,1000,1000)
plt.scatter(tab3,range(0,1000))

plt.xlabel('x')
plt.ylabel('y')
plt.title('Nuage de point numpy de 1000 rand')

plt.show()

#3
plt.plot (tab1,tab2,"r")
plt.xlabel("x-tab1")
plt.ylabel("y-tab2")
plt.title("courbe tab1-tab2")
plt.show()


#4
tab4 = np.random.randn(100)
plt.plot (tab4,"r")
plt.xlabel("x-tab4")
plt.ylabel("y-range")
plt.title("courbe tab4-range")
plt.show()


#5-6-7-8
fig = plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])

x=np.linspace(0,2,100) 
ax.plot(x,x,label="lineaire")
ax.plot(x,x**2,label="quadratique")
ax.plot(x,x**3,label="cubique")
ax.set_title("Comparaison des fonctions linéaire, quadratique et cubique")
ax.set_xlabel("Abscisse")
ax.set_ylabel("Ordonnee")
ax.legend()
plt.show()

#9-10
fig,axes=plt.subplots(nrows=1,ncols=3,figsize=(20,7))

i=1
t=0
titre=["Lineaire","quadratique","cubique"]
couleur =["blue","orange","green"]
for ax in axes :
	ax.plot(x,x**i,color=couleur[t])
	ax.set_xlabel("Abscisse")
	ax.set_ylabel("Ordonnee")
	ax.set_title(titre[t])
	i=i+1
	t=t+1	
plt.tight_layout()
plt.show()

"""
#11
from random import sample
table= np.random.uniform(0,10,100)
plt.hist(table,bins=10)
plt.show()
