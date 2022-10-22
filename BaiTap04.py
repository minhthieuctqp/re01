# Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5,
# nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200)
for i in range(2002, 3201, 7):
    if (i % 5) != 0:
        print(i)
