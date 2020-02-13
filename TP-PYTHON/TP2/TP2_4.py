import pandas as pd
import numpy as np

#1
nparr=np.ones((3,4))
colonne= ["A","B","C","D"]
ligne=["i1","i2","i3"]
df=pd.DataFrame(data=nparr,columns=colonne,index=ligne)

#2
nparr2=np.ones((100,4))
colonne2= ["p1","p2","p3","p4"]
ligne2=[]

for i in range(1,101):
	ligne2.append("i"+str(i))

df2=pd.DataFrame(data=nparr2,columns=colonne2,index=ligne2)

#3
df2["p1"].apply(lambda x: x+x)
for i in range (0,101):
	if (i > 0):	
		df2["p1"][i-1:i+1]=i**1
		df2["p2"][i-1:i+1]=i**2
		df2["p3"][i-1:i+1]=i**3
		df2["p4"][i-1:i+1]=i**4
#4
print(df2.shape)

#5
print(df2.head(10))

#6
print(df2.tail(10))

#7
print(df2.columns)

#8
print(df2.dtypes)

#9
print(df2.info())

#10
print(df2.describe())

#11
print(df2.p4) #print(df2["p4"])

#12
print(df2[["p1","p4"]])

#13
print(df2.value_counts(bins=10))
