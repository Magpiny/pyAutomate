import os

path = os.getcwd()

print(path)

# GET NO OF CPUs OF MY COMPUTER
pat = os.cpu_count()
print(pat)

# GET OS INFORMATION
my_os = os.uname()
print(my_os)