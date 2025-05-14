import json

person = {
    "name":"John",
    "age" : 30,
    "city": "New York",
    "hasChildren": False,
    "titles":["engineer", "programmer"]
}

print(person)

personJSON =json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

# indent = format the output
# sort_keys - will sort the keys in ascending order if it is true

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

person = json.loads(personJSON)
print(personJSON)

class User:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
user = User("Max", 27)

userJson = json.dumps(user.__dict__)
print(userJson)