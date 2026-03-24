n = int(input("jumlah baris: "))
for i in range(1, n + 1):
    print(f"{i} " * i)

# n = int(input("jumlah baris: "))
# for i in range(0, n + 1):
#     for j in range(1, n - i + 1):
#         print("X ", end = "") if j % 2 == 1 else print("0 ", end = "")
#     print()