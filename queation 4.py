print("Input size: ")
n = int(input())
for i in range(1, n):
    print("*" * (n - i) + "  " * i + "*" * (n - i))
for k in range(1, n):
    print("*" * k + "  " * (n - k) + "*" * k)

# Code by Shreyansh Sharma