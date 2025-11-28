# The original data structures
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Print the original data structures
# print("Original data structures:")
# print(ft_list)
# print(ft_tuple)
# print(ft_set)
# print(ft_dict)


# List: Mutable, ordered. Useful for modifiable sequences.
# Change the second element using its index (1).
ft_list[1] = "World!"

# Tuple: Immutable, ordered. Useful for fixed data like coordinates.
# Must be converted to a list, modified, and converted back to a tuple.
temp_list = list(ft_tuple)
temp_list[1] = "France!"
ft_tuple = tuple(temp_list)

# Set: Unordered, mutable, unique elements. Useful for removing duplicates.
# Remove the existing "tutu!" and add the new string.
# An element cannot be changed in place because sets are unordered.
ft_set.remove("tutu!")
ft_set.add("Angoulême!")

# Dictionary: Key-value pairs, mutable. Useful for structured data.
# Change the value associated with the key "Hello".
ft_dict["Hello"] = "42Angoulême!"

# The print statements to check the work
print("Modified data structures:")
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
