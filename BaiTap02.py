import os
os.system('cls')

print("Giai phuong trinh ax + b = 0")
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    print("Nghiệm phương trình là: ", -b/a)
