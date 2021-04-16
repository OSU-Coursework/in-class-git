import random

def password(_num):
    password = ""
    for _ in range(_num):
        password += (chr(random.randint(48, 122)))
    return password


