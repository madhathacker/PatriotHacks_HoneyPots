# This is a comment
# Python ignores these, they are here for you!

# Variables
string = "Patriot Hacks"
intiger = 2023
boolean = True

# Iterables
list_of_things = [string, intiger, boolean]
dictionary = {"frost_key": "Santa", "fire_key": "Demon"}
print(dictionary["frost_key"]) # grab the value that goes to a specific key

# Logic
if(intiger < 50):
    print("That's a small number!")
elif(intiger == 69 and boolean): # You can check multiple things
    print("Nice!")
elif(intiger == 420 or boolean): # You can have as many elif statements as you want
    print("Blaze it!")
elif intiger == 2023: # Notice I didn't need to use braces
    print("Better than 2022!")
else:
    print("This number isn't special!")

# Loops
counter = 0
while(counter  < 3): # while loop
    counter += 1
    print(counter)

print("Before Loop")
for number in range(1,10): # for loop need iterable
    print(f"Start of Loop {number}")
    if(number == 1):
        print("pass")
        pass
    elif(number == 2):
        print("continue")
        continue
    else:
        print("break")
        break
    print(f"End of Loop {number}")
print("After Loop")

# Functions
def say_hello(name: str) -> int: # Notice the type hinting? This isn't necessary but is a helpful comment.
    '''This functions takes a name, says hello, then return length of name''' # This is a docstring, Basically a fancy comment
    response = f"Hello {name}"
    print(response)
    return len(name) # Generally functions return one or more things

say_hello("World")

# Classes
class cats: # define a class for cats
    color = "black"

my_cat = cats() # create a instance of the cats class
print(my_cat.color)