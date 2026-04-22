#password_generator.py
import random
import string

chars = string.ascii_letters + string.digits + "!@#$%"

length = int(input("Length: "))
password = ''.join(random.choice(chars) for _ in range(length))

print(password)
