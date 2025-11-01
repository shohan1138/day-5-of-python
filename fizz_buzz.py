for number in range(1,101):
    if number % 5 == 0 and number % 3 == 0:
        print(f"FIZZBUZZ")
    elif number % 5 == 0:
        print(f"BUZZ")
    elif number % 3 == 0:
        print(f"FIZZ")
    else:
        print(number)

