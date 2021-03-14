# IF STATEMENTS
"""
name = "Bob"
if name == "Sam":
    print(f"Hello {name}")
print(name)
"""
# IF ELSE STATEMENTS
"""
password = 12345678

if password == 12345678:
    print("ACCESS GRANTED ")
else:
    print("ACCESS DENIED!")
"""
# IF ELIF ELSE STATEMENTS
"""
print("Please enter you passcode")
password = int(input())

if password == 12345678:
    print("Access granted SAM")
else:
    print("Go home")
"""
# BUILDING ON THE PREVIOUS KNOWLEDGE
print("Kindly ENTER your age...  ")
age = int(input())
if 0 < age < 18:
    print("Go and play kiddo!")

# elif age >=18 and age <= 31
elif 18 <= age <= 31:
    print("You're eligible to take beer!")
elif 32 <= age <= 59:
    print("Focus on your goals, I repeat LASER FOCUSED!!")
elif 60 <= age <= 130:
    print("Retire gracefully")
elif age == 0:
    print("Give us something reasonable please! ")
else:
    print("Outside the current life expectancy range!!")



