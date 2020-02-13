#-----------Tableau 2-D------------------------#
#1
import numpy as np
#2
npvide = np.empty([1,10])

#3
nparr1 = np.zeros(10)

#4
nparr2 = np.ones(10)

#5
nparr3 = np.empty([1,10])
nparr3[0:10]=5

#6
npstring  = np.chararray((1,10))
npstring[0:10]= range(10)

print (npstring)

#7
tab1 = np.arange(1,10.5,0.5)

#8
tab2 = np.linspace(1,10,20)

#9
tab3 =np.arange(10,30)

#10
somme = np.sum(tab3)

#11
sommecum = np.cumsum(tab3)

#12
avg = np.mean(tab3)

#13
prodScal = np.vdot(tab2,tab3)

#14
Slct = np.select([tab3>20],[tab3])

#15
print ("affichage tab3")
print (tab3[:16:5]) # on part de 0  a 15 avec un pas de 5


#----------------------------Les Matrices-------------------#

#1
matId = np.eye(9)

#2
mat10x10 = np.ones((10,10)) 

#3
print (len(mat10x10)) 

#4-5
print (mat10x10.shape)



#6
matreshape = np.arange(0,9)
matreshape = matreshape.reshape((3,3))

#7
A=np.linspace(0.01,1.0,100).reshape((10,10))

#8
B = A[6:,:4]

#9
shap = B.shape
likeB1 = np.ones(shap)

#10
C= A[2:4,:7:2] # de 2 a 4, de 0 a 7 avec un pas de 2

#11
prodmat = np.dot(C,B)

#12
val055=A[5,4]


#13
colonne4 = A[:,3:4]

#14
ligne4 = A[3:4,:]

#15
#ligneSup5 = 

#16
avgGlob = np.mean(A)

#17
avgLine = np.mean (A,1)

#18
avgCols = np.mean(A,0)

#19
prodScalC1L1 = np.vdot(A[:,:1],A[:1,:])

#20
A[3:7,3:7] =0

#21
index0 = np.where(A==0)

#------------------------Les NOmbres Aleatoires--------------------#
#6
print ("alea")
alea6 = np.random.seed(42)
#1
Alea = np.random.rand(10)

#2
Alea2 = np.random.randint(0,100,100)

#3
Alea3 = np.random.randn(25)

#4
alea5 = np.random.rand(25)
print (alea5)

#5
Alea5 = np.random.randn(10,10)




#---------------------Les Entrees-Sorties--------------------------#

#1
np.savetxt("Alea5.csv",Alea5, delimiter = ",")

#2
load = np.genfromtxt("Alea5.csv",delimiter =",")
print (load)








