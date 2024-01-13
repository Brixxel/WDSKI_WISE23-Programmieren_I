
import numpy as np
import matplotlib.pyplot as plt

# %%

m = np.ones((2,5))
v = np.asarray([1,2,3,4,5])

m.dot(v)
m.dot(m.transpose())

r = np.random.uniform(size=(30,30,4))
plt.imshow(r)

# %%

#Ohne Rand
# z = np.ones((8,8))
# z[0:8:2,0:8:2] = 0
# z[1:8:2,1:8:2] = 0
# plt.imshow(z)

#Mit Rand
# y = np.ones((10,10))
# y[1:9:2,1:8:2] = 0
# y[2:9:2,2:9:2] = 0
# y[0:10:9] = 2 
# y[0:10,0:10:9] = 2
# plt.imshow(y)

x = np.ones((8,8))
print(x)
print(type(x))
x[0:8:2,0:8:2] = 0
x[1:8:2,1:8:2] = 0
x = np.pad(x,1,constant_values= 2)
plt.imshow(x)

# %%
import matplotlib . pyplot as plt
import numpy as np

x = np . linspace (0 , 2 * np .pi , 200 )
y = np .sin( x )

plt . plot (x , y )
plt . show ()

# %%

b = "Zerlege mich in kleinbuchstaben Woerter"
b = b.lower().split(" ")
print(b)

a = "hello"
a[1] = "q"

# %%
print([x for x in range(3)])
# %%

Integer = list(range(20))
Integer = [x+1 for x  in Integer]
print(Integer)

Sort_Integer = [x for x in Integer if x% 2 == 1] + [j for j in Integer if j % 2 == 0]
#Sort_Integer.extend([j for j in Integer if j % 2 == 0])
print(Sort_Integer)

# %%
Fiver_Integers = [x for x in range(5, 101, 10)]
print(Fiver_Integers)

# %%
import random

Random_Integers = [random.randint(-100, 100) for x in range(1000)]
print(Random_Integers)
if 0 in Random_Integers:
    print(Random_Integers.index(0))

# %%

class Dog:
    def __init__(self) -> None:
        pass
    
    def __init__(self, alter: int):
        self.alter = alter
        

dogo1 = Dog()
dogo2 = Dog(13)
    

# %%
