# Step 1: Create the decorator function
def my_decorator(func):
    # Step 2: Create a wrapper function inside it
    def wrapper():
        print("Something is happening BEFORE the function is called.")
        func()  # This calls your original function
        print("Something is happening AFTER the function is called.")
    return wrapper  # Return the wrapper function

# Step 3: Apply it using the @ symbol
@my_decorator
def say_hello():
    print("Hello, World!")

# Step 4: Run the function
say_hello()


#-------X---------X---------X----------X---------X--------X---------X--------X----
#output
'''Something is happening BEFORE the function is called.
Hello, World!
Something is happening AFTER the function is called.'''
