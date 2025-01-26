from random import randint

min_number = int(input("Enter the minimum number: "))
max_number = int(input("Enter the maximum number: "))

if min_number > max_number:
    print("The minimum number must be less than the maximum number.")
else:
    random_number = randint(min_number, max_number)
    print(f"Random number between {min_number} and {max_number}: {random_number}")