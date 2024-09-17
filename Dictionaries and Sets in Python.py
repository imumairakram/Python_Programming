# Dictionary Example
dict = {
    "Name": "Umair",
    "Subject": ["Python", "C", "Java"],
    "Topic": "dict, Sets",
    "Is_adult": True,
    "Age": 19,
    "Cgpa": 3.1,
    "I'd": [6, 2, 6, 1, 1]
}
print(dict)

# Creating an empty dictionary and adding an element
null_dict = {}
null_dict["name"] = "iqra_university"
print(null_dict)

# Nested Dictionary Example
student = {
    "name": "Umair",
    "Subjects": {
        "Physics": 98,
        "Chemistry": 97,
        "Math": 99
    }
}
print(student["Subjects"]["Chemistry"])

# Dictionary Methods: keys()
student = {
    "name": "Umair",
    "Subjects": {
        "Physics": 98,
        "Chemistry": 97,
        "Math": 99
    }
}
print(student.keys())

# Dictionary Methods: values()
print(student.values())
print(list(student.values()))

# Dictionary Methods: items()
print(student.items())
print(list(student.items()))
print(len(list(student.items())))
pairs = list(student.items())
print(pairs[0])

# Accessing dictionary with get() method
print(student.get("name2"))

# Dictionary update() method
student.update({"Biology": 89})
print(student)

# Sets Example
collection = {1, 2, 3, 4, "Hello", "World"}
print(collection)
print(type(collection))

collection = {1, 2, 3, 2, "Hello", "World", "World", 4}
print(collection)
print(len(collection))

collection = set()
print(type(collection))

# Set Methods: add()
collection.add(1)
collection.add(2)
collection.add(2)
print(collection)

# Set Methods: remove()
collection.remove(2)
print(collection)

# Set Methods: clear()
collection.clear()
print(collection)

# Set Methods: pop()
collection = {"Hello", "In", "The", "World", "Of", "Python"}
print(collection.pop())
print(collection.pop())

# Set Methods: union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))

# Set Methods: intersection()
print(set1.intersection(set2))
