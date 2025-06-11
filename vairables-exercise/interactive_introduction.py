name = input("Enter your name: ")

try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Oops! Please enter a valid number for age.")
    age=0
language = input("Enter your favorite programming language: ")

print(f"Hi, my name is {name.capitalize()}. I am {age} years old and I love {language.capitalize()}!")


# second  example

name = input("Enter your name: ")

# Ask for age until a valid number is entered
while True:
    try:
        age = int(input("Enter your age: "))
        break  # ✅ correct input → exit the loop
    except ValueError:
        print("❌ Invalid input! Please enter a number for age.\n")

language = input("Enter your favorite programming language: ")

print(f"\nHi, my name is {name.capitalize()}. I am {age} years old and I love {language.capitalize()}!")
