CURRENT_YEAR = 2026
BUFFOR = 5
ADULTS_AGE = 18
THE_OLDEST_PERSON_AGE = 150
YOB_OLDEST = CURRENT_YEAR - THE_OLDEST_PERSON_AGE

yob_of_the_oldest_person = CURRENT_YEAR - THE_OLDEST_PERSON_AGE

print("This application is only for adult user (18+)")

yob = int(input("What is your year of birth?"))

user_age = 2026 - yob

# checking if yob is correct

if yob > (CURRENT_YEAR - BUFFOR):
    print(f"Are you sure that {yob} is your year of birth?")

if yob < (CURRENT_YEAR - BUFFOR):
    # checkin if user is old enough
    if user_age >= ADULTS_AGE:
        # user is old enough
        print(f"You are {user_age} years old! You can access the website")
        print("Welcome to the website!")

    if user_age < ADULTS_AGE:
        # user is not old enough
        print(f"You are {user_age} years old! Not enough to enter the website")
        print(f"Come back to us in {ADULTS_AGE - user_age} year(s)!")

print()
print("Goodbye see you again!")