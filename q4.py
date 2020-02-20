# Use a list comprehension to create a list of squared numbers (n*n).
# The function receives the variables start and end,
# and returns a list of squares of consecutive numbers between start and end inclusively.
# For example, squares(2, 3) should return [4, 9].

def squares(start, end):
    return [n * n for n in range(start, end + 1)]


print(squares(2, 3))  # Should be [4, 9]
print(squares(1, 5))  # Should be [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



def highlight_word(sentence, word):
	return sentence.replace(word, word.upper())

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


def format_address(address_string):
    # Declare variables

    # Separate the address string into parts
    address_parts = address_string.split()
    print(address_parts)

    # Return the formatted string
    return "house number {} on street named {}".format(address_parts[0], ' '.join(address_parts[1:]))


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"