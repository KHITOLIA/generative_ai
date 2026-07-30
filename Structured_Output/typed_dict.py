from typing import TypedDict

class Person:
    name : str
    age : int

# new_person : Person = {"name" : "Tushar", "age" : "35"}
# print(new_person)

new_person = Person()
new_person.name = "Tushar"
new_person.age = 34
print(new_person.name)