a = int("Enter first number")
b = int("Enter second number")

c = a+b
print("The sum of the two numbers is",c)

# if i don't write int( with input then i would find 2+ 3 = 23 instead of 5)
# if i write just int and not input then value error but why

#%%

a = input("Enter the name of favourite animal")
print("My favourite animal is",a)

#%%

a = int(input("Enter the temperature"))
b = (5/9)*a + 32

print("The temperature in celsius is", b)

#%%

a = int(input("Enter the length of first side"))
b = int(input("Enter the length of the second side"))
c = int(input("Enter the length of third side"))
d = a+b+c
print(d)

#%%

a = float(input("Enter first number"))
# b = int(input("Enter second num"))
c = a*a
print(c)

#%%

a = [1,2,3,4,5,6]
del a[2:3]
               # start from 2 and stop 3
print(a)

#%%


a = [1,2,3]
b = [4,5,6]
a.append(b)

print(a)

#%%

a = [10,20,30,40]

a.pop(0)

print(a)

#%%

a = ["red","blue","green","yellow"]

print("The required index",a[2])


#%%

my_list = []

# Continuously ask the user for input
while True:
    value = input("Enter a value:")
    
    # If the user presses Enter without input, break the loop
    if value == 0:
        break
    
    # Convert input to integer and append to the list
    my_list.append(int(value))

# Print the list
print("Your list:", my_list)

#%%

def get_last_element(lst):
    while True:
        user_input = input("Enter a value (or 'No' to stop): ")
        if user_input.lower() == 'no':
            break
        lst.append(int(user_input))

    print("The last element is:", lst[-1])

my_list = []
get_last_element(my_list)

























