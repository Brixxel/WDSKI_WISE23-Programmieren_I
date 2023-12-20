import random
import names

## @Felix_Regler 
## Version: 1.0
## 24.11.2023

### Ein Konklomerat an Aufgaben: ###

## Python scriot for the function: f(x) = sum[1->x] (1/i^2) ##
def sum_function(n):
    s = 0
    for x in range(1,n+1):
        s += 1 / (x**2)
    return s

#for i in range(1, 100):
#    print(sum_function(i))

### Fibonacci Sequence ##
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

#for i in range(100):
#    print(fib(i))


## Rekursieve additionsabfrage vom Nutzer ##
def rnd_add_user(rnd_a, rnd_b):
    if int(input(f"what is: {rnd_a} + {rnd_b} = ")) == rnd_b + rnd_a:
        print("passt!")
    else:
        print("nö!")
        rnd_add_user(rnd_a, rnd_b)

# rnd_add_user(random.randint(1,10000),random.randint(1,10000))

## Dictionary für Schulnoten ##
noten:dict[str, int] = {}
for x in range(1,10):
    name = names.get_full_name()
    noten[name] = random.randint(0,15)
print(noten)

def calc_avg(l):
    return sum(l) / len(l)

print(calc_avg(noten.values()))