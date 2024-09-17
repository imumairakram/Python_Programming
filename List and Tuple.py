# --- Lists and Tuples in Python ---

# Marks example using a list
marks = [89.1, 90.3, 92.5, 94.6, 95.4, 97.3, 98.2]
print("Marks List: ", marks)
print("Type: ", type(marks))
print("Length of List: ", len(marks))
print("First element:", marks[0])
print("Second element:", marks[1])

# Slicing a list
li = [2, 4, 6, 8]
print("Sliced list (index 1 to 3):", li[1:4])
print("Type of list:", type(li))

# List methods
my_list = [2, 1, 5, 9, 6, 4]

# Adding elements to a list
my_list.append(3)
print("List after append:", my_list)

# Sorting list in ascending order
my_list.sort()
print("List after sort:", my_list)

# Sorting list in descending order
my_list.sort(reverse=True)
print("List after reverse sort:", my_list)

# Reversing the list order
my_list.reverse()
print("List after reverse:", my_list)

# Finding index of a value
print("Index of 5:", my_list.index(5))

# Counting occurrences of a value
print("Count of 5:", my_list.count(5))

# Copying the list
copy_list = my_list.copy()
print("Copy of list:", copy_list)

# Inserting an element at index 1
my_list.insert(1, 7)
print("List after insert:", my_list)

# Extending the list with another list
my_list.extend([7, 8, 9])
print("List after extend:", my_list)

# Popping an element at index 1
my_list.pop(1)
print("List after pop at index 1:", my_list)

# Removing a specific value
my_list.remove(5)
print("List after removing 5:", my_list)

# Clearing the entire list
my_list.clear()
print("List after clear:", my_list)

# List Operations: Movies example
movies = []
movie1 = input("Enter your 1st movie name: ")
movies.append(movie1)
movie2 = input("Enter your 2nd movie name: ")
movies.append(movie2)
movie3 = input("Enter your 3rd movie name: ")
movies.append(movie3)
print("Your favorite movies:", movies)

# List counting and sorting
grade = ["C", "A", "A", "A", "B", "A"]
print("Count of A in grades:", grade.count("A"))

value = ["C", "A", "D", "E", "B", "F"]
value.sort()
print("Sorted values:", value)


# --- Tuples in Python ---
# Tuples are immutable

tup = (2, 3, 5, 6)
print("Tuple:", tup)
print("Type of tuple:", type(tup))
print("First element:", tup[0])
print("Second element:", tup[1])

# Slicing a tuple
tup = (1, 2, 3, 4)
print("Sliced tuple (index 1 to 3):", tup[1:3])

# Tuple methods
tup = (1, 2, 3, 4, 5)
print("Index of 2:", tup.index(2))

tup = (1, 2, 3, 4, 5, 3, 9)
print("Count of 3 in tuple:", tup.count(3))

# More tuple operations
fruits = ("apple", "banana", "cherry")
print("Length of tuple:", len(fruits))
print("Is 'apple' in fruits:", "apple" in fruits)

# Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print("Concatenated tuple:", combined_tuple)

# Unpacking a tuple
person = ("Umair", 20, "Male")
name, age, gender = person
print("Name:", name)
print("Age:", age)
print("Gender:", gender)

# Nested tuples
nested_tuple = (("Umair", "Student"), ("Iqra", "University"))
print("Nested tuple:", nested_tuple)

# Tuple of lists
tuple_of_lists = ([1, 2, 3], [4, 5, 6])
print("Tuple of lists:", tuple_of_lists)

# List inside tuple modification
tuple_of_lists[0].append(4)
print("Modified tuple of lists:", tuple_of_lists)

