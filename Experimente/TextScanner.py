# @Felix Regler

import collections
import operator

chat = open('chat.txt','r', encoding="utf8")
content = chat.readlines()

counter = 0

name_counter = 0

for nachricht in content:
    if nachricht.find("Felix Regler") == 21:
        print(nachricht)
        name_counter += 1  
    counter += 1

print(counter)
print(name_counter)
