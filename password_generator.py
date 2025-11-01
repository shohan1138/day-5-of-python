import random

# Lowercase letters
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']

# Uppercase letters
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                     'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']

# Symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
           '=', '+', '[', ']', '{', '}', '|', ';', ':', "'", ',', '.',
           '<', '>', '/', '?', '`', '~']

# Numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Password generator!")
nr_up_letters=int(input("how much uppercase letter you want:"))
nr_low_letters=int(input("how much lowercase letter you want:"))
nr_symbols=int(input("how much symbols you want:"))
nr_numbers=int(input("how much numbers you want:"))

# easy(serial)
# password=""
# for char in range(1,nr_up_letters+1):
#     random_up=random.choice(uppercase_letters)
#     password=password+random_up
# for char in range(1,nr_low_letters+1):
#     random_low=random.choice(lowercase_letters)
#     password=password+random_low
# for char in range(1,nr_symbols+1):
#     random_sym=random.choice(symbols)
#     password=password+random_sym
# for char in range(1,nr_numbers+1):
#     random_num=random.choice(numbers)
#     password=password+random_num
# print(f"easy password is:{password}")


# hard(suffle)
password_list=[]

for _ in range(nr_up_letters):
    password_list.append(random.choice(uppercase_letters))

for _ in range(nr_low_letters):
    password_list.append(random.choice(lowercase_letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))


# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ''.join(password_list)
print(f"your password is:{password}")