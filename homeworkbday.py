# Personalized Birthday Card Generator

from datetime import datetime

# Get the current year automatically
current_year = datetime.now().year

# Prompt the user for information
print("=== Birthday Card Generator ===")

recipient_name = input("Enter the recipient's name: ")

# Ask for year of birth and convert to integer
year_of_birth = int(input("Enter the recipient's year of birth (e.g., 1990): "))

personal_message = input("Enter your personalized birthday message: ")

sender_name = input("Enter your name: ")

# Calculate the age
age = current_year - year_of_birth

# Generate the birthday card
print("\n" + "=" * 40)
print("🎉 Happy Birthday Card 🎉")
print("=" * 40)

print(f"\n{recipient_name}, let's celebrate your {age} years of awesomeness!")
print(f"Wishing you a day filled with joy and laughter as you turn {age}!\n")

print(personal_message + "\n")

print("With love and best wishes,")
print(sender_name)

print("\n" + "=" * 40)

