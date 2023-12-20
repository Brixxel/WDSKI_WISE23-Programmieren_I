# @Felix Regler
# Kleine Übung aus der Vorlesung zu List comp

import random

list = [x for x in range(10)]
print(list)

my_list_1 = [x for x in range(101) if x % 10 == 5]
print(my_list_1)

print(random.randint(-1000, 1000))

my_list_2 = [random.randint(0, 1000) for x in range(1000)]
print(my_list_2)

