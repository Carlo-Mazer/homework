# loop
from operator import truediv

choice = "Good girl"

print("-- REPLY 'yes' OR 'no' --")

print("Do you want to make love with me?")


  if choice == "yes":
    print(choice)
condition = True

while condition:
    print(choice)

    again = input("Again?")
    if again == "yes":
        condition = True
    else:
        condition = False


print("-- Wrong Answer --")