import random
import string


def passcode_generator():
    pass_chars = string.ascii_letters + string.digits + string.punctuation
    length = random.randint(8, 25)
    passcode = "".join(random.choices(pass_chars, k=length))
    print(len(passcode))  # monitor the length of my password


passcode_generator()
