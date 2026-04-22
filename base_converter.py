#base_converter.py
num = int(input("Number: "))
base = int(input("Base (2/8/16): "))

if base == 2:
    print(bin(num))
elif base == 8:
    print(oct(num))
elif base == 16:
    print(hex(num))
