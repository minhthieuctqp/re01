import math
import os
os.system('cls')
print("Giai phuong trinh ax^2 + bx + c = 0")

a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))
if a == 0:
    print("Đây là phương trình bậc 1!")
else:
    Delta = b*b - 4*a*c
    if Delta < 0:
        print("Phương trình vô nghiệm.")
    elif Delta == 0:
        print("Phương trình có nghiệm kép là: ", -b/(2*a))
    else:
        x1 = (-b+math.sqrt(Delta))/(2*a)
        x2 = (-b-math.sqrt(Delta))/(2*a)
        print("Nghiệm phương trình là: ")
        print("x1 = ", x1)
        print("x2 = ", x2)