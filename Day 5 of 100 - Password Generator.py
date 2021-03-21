#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []

# Random picks from each list
for letter in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for symbol in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for num in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

# Joining random picked list together 
random.shuffle(password_list)

# Converting list in to a string
result = "".join(str(i) for i in password_list)

# another way to convert a list into a string.
# result = ""
# for char in password_list:
#     result += char


print(f"Your new password is: {result}")

input("Press enter to close")
