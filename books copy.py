books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

# Demonstration of appending and list and adding a list to another
print(books[1]) # Python for Data Analysis
books[1] = "Python for Data Analysis - Jason R. Briggs" # The list is muttable, but not the string. The string must be replaced
print(books[1]) # Python for Data Analysis - Jason R. Briggs
print(len(books[1])) # 42 - number of characters of Python for Data Analysis - Jason R. Briggs
print(len(books)) # 5 - number of objects in the list
print(books[len(books)-1]) # 5-1 = books[4]
print(books[4])

# Demonstration of copying and deleting a list
books2 = books # Copy a list
print(books2)

del book2 # Delete the new list
print(books2) # NameError - because the lsit no longer exists

# Deomonstration of deleting an indexed item and not the entire list
# del deletes the selected indexed item
# .pop() deletes the last indexed item if no reference is made
recommendation = books[1]
del books[1] # Deletes Python for Data Analysis - Jason R. Briggs
books.pop() # Removes last indexed item
books.pop(0) # Removes first indexed item
