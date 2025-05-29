import random

print("Sir your password is :")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*:;!?@#$_&-+()/%©®™✓£¢€¥°~`§"
password = ""

for i in range(16):
    password += random.choice(chars)
print(password)