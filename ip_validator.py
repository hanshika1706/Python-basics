#ip_validator.py
ip = input().split(".")

if len(ip) == 4 and all(0 <= int(x) <= 255 for x in ip):
    print("Valid IP")
else:
    print("Invalid IP")
