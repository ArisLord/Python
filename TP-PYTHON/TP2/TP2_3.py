import numpy as np
import matplotlib.pyplot as plt

"""
#-------------------------------Partie 1 : Génération d’un histogramme de la répartition du Q-------------#
#1
np.random.seed(0)

#2
nparr = np.random.randn(500)

#3
u=100
o=15
nparr = nparr*o+u

#4
from random import sample
plt.hist(nparr,bins=50)


#5
plt.ylabel("Probabilité de densité")

#6
plt.xlabel("Quotient intellectuel")

#7
plt.grid()

#8 en attente

import math
y = (1 / o*math.sqrt(2*math.pi)) * math.exp((-1/2)*((50-u)/o)**2)

plt.show()


"""
#--------------------------Partie 2 : Gestion de données issues d’un fichier au format csv------------------------------#

#1-2
redwine = np.genfromtxt('./redwineNP.csv',delimiter=";")



fig = plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8]) 
ax.plot(redwine[:,9:11],redwine[:,10:11])
ax.set_xlabel("degre d'alcool")
ax.set_ylabel("qualite")
plt.show()



