people = [ {"name": "Harry", "house": "Gryffindor"}, 
{"name": "Cho", "house":"Ravenclaw"}, 
{"name": "Draco", "house": "slytherin"}
]

def f(person):
    return person["house"]


people.sort(key=f)


people.sort(key=lambda person: person["name"])

print(people)