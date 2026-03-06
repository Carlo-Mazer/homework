print("This application is only for adult user (18+)")

yob = int(input("What is your year of birth?"))

if 2026-yob >= 18:
    print("Welcome to the adult site content")

if 2026-yob <18:
    print("You are not meeting the legally requirements to enter this site")

# ____________________________

CURRENT_YEAR = 2026

print("This application is only for adult user (18+)")

yob = int(input("What is your year of birth?"))

user_age = 2026-yob

# checking if yob is correct

if yob < (2026-5):
    print("Access denied")

# checkin if user is old enough
if user_age >= 18:
    #user is old enough
    print(f"You are {user_age} years old! You can access the website")
    print("Welcome to the website!")

if user_age < 18:
    #user is not old enough
    print(f"You are {user_age} years old! Not enough to enter the website")
    print("Sorry! You are not old enough to enter the website")
    print(f"Come back to us in {user_age} year(s)!")

print()
print("Goodbye see you again!")

