from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 20:
        break
    

a = [1,2,3,4,5]
for i in cycle(a):
    print(i)
    
a = [1, 2, 3, 4]
for i in repeat(1, 4):
    print(i)