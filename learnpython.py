# https://www.learnpython.org/en/Basic_Operators#google_vignette
# Example 1
number = 1 + 2 * 3 / 4.0
print(number)

# Example 2
remainder = 11 % 3
print(remainder)

# Example 3
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

# Example 4
helloworld = "hello" + " " + "world"
print(helloworld)

# Example 5
lotsofhellos = "hello" * 10
print(lotsofhellos)

# Example 6
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# Example 7
print([1,2,3] * 3)

# Exercise
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print(f"x_list contains {len(x_list)} objects")
print(f"y_list contains {len(y_list)} objects")
print(f"big_list contains {len(big_list)} objects")

