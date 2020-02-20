def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


result = convert_seconds(5000)
type(result)
print(result)


def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for letter in input_string:
		# Add any non-blank letters to the
		# end of one string, and to the front
		# of the other string.
		if letter != '' and letter!=' ':
			new_string = new_string + letter
			reverse_string = letter + reverse_string
	# Compare the strings
	print(new_string)
	print(reverse_string)
	if new_string.upper() == reverse_string.upper():
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("Alex@example.com", "Alex Diego")]))

