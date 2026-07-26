
fruits = ["apple", "banana", "cherry"]

# Turn the list into an iterator
my_iterator = iter(fruits)

# Grab items one by one using next()
print(next(my_iterator))  # Outputs: apple
print(next(my_iterator))  # Outputs: banana
print(next(my_iterator))  # Outputs: cherry

