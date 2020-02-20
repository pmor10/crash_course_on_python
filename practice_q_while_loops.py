# Fill in the blanks to make the print_prime_factors function print all the prime factors of a number.
# A prime factor is a number that is prime and divides another without a remainder.

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5


# The following code can lead to an infinite loop.
# Fix the code so that it can finish successfully for all numbers.
# Note: Try running your function with the number 0 as the input, and see what you get!
def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    while n % 2 == 0:
        if n == 0:
            break
        n = n / 2
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
    return False


print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False

# Fill in the empty function so that it returns the sum of all the divisors of a number, without including it.
# A divisor is a number that divides into another without a remainder.

def sum_divisors(n):
  # Return the sum of all divisors of n, not including n
    i = 1
    # We will add the divisible numbers here
    total = 0
    while i < n:
        # here is where we add the i's that divide evenly into n.
        if n % i == 0:
            total += i
            i+=1 # we still want to increase by 1
        else: # this is when n is not divisible by i, we add 1 to i to continue checking the next number.
            i += 1
    return total

print(sum_divisors(0))
print(sum_divisors(6))
print(sum_divisors(12))