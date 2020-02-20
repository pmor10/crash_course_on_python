name = "Paresa"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))

# formating strings
price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. with Tax: ${:.2f}".format(price, with_tax))


def to_celsius(x):
    return (x - 32) * 5/9

for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))