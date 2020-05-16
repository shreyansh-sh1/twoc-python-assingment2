print("Input size: ")
n = int(input())
for i in range(n, 0, -1):
    for k in range(0, i):
        if k == i - 1:
            print(i)
        else:
            print(i, "*", end=" ")
for i in range(1, n + 1):
    for k in range(0, i):
        if k == i - 1:
            print(i)
        else:
            print(i, "*", end=" ")


# Code by Shreyansh Sharma