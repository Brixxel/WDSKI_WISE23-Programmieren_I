import matplotlib.pyplot as plt
import random

## @Felix_Regler 
## Version: 1.0
## 17.11.2023

## Moving Average (Schnitt zweier benachbarter Zahlen in X als neues Array ausgeben)
## ausführliche Dkumentation folgt

## das zugrundeliegede Tupel x erstellen:
v = list()
v.append(0)
i = 0

while i < 20:
   j = random.randint(1,20)
   v.append(j)
   i += 1
x = tuple(v)


## eihentliche Berechnung des AVG.
i = 0
l = list()
l.append(0)
xList = list(x)

while i+2 < len(x):
   y = (x[i] + x[i+1]) / 2
   print(y)
   l.append(y)
   i+=1


## Plotting
print(x)
print(tuple(l))

plt.plot(xList)
plt.plot(l)
plt.show()
