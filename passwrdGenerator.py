import random
import string

pass_chars = string.ascii_letters + string.digits + string.punctuation
length = random.randint(8, 16)
passcode = "".join(random.choices(pass_chars, k=length))
print(passcode)
print(len(passcode))

