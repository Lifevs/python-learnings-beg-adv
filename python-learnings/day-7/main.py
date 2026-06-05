# Day 7: Interactive Terminal Script
# Demonstrating input(), type conversion, and terminal output

print("--- Welcome to the Day 7 Terminal Script ---")

# 1. Capture user input
name = input("Enter your name: ")
age_str = input("Enter your age: ")

# 2. Type conversion (input always returns a string)
age = int(age_str)

# 3. Dynamic logic based on input
print(f"\nHello, {name}!")
print(f"Next year, you will be {age + 1} years old.")

if age >= 18:
    print("You are eligible for adult-only terminal features.")
else:
    print("You are currently in 'Junior Scripter' mode.")

print("\n--- Script Execution Complete ---")
