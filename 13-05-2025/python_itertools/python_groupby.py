from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)

for key, value in group_obj:
    print(key, list(value))
    
    
persons = [{'name':'tim', 'age':25}, 
           {'name': 'alex', 'age': 25},
           {'name': 'sara', 'age': 28}]

group_obj = groupby(persons, key=lambda x : x['age'])
for key, value in group_obj:
    print(key, list(value))