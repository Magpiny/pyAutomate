import re
b = 12
n = 0

while n != b:
    n += 1
    print("This is my loop number  " + str(n))
    if n == b:
        print("Your loop has ended!")
        break
else:
    print("Your loop has ended!")

print("Kindly enter your password ... ")
passcode = input()
pattern = r'([a-zA-Z]+\d+)'
mo = re.compile(pattern)
match_case = mo.search(passcode)
print(match_case)
