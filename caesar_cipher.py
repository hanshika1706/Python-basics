#caesar_cipher.py
text = input()
shift = 3

result = ""

for c in text:
    if c.isalpha():
        result += chr((ord(c) + shift - 97) % 26 + 97)
    else:
        result += c

print(result)
