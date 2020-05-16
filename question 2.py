print("Enter Size: ")
N = int(input())

for i in range(N):
    for k in range(N):
        if (i == k) or ((N - k -1) == i):
            print('*', end = '')
        else:
            print(' ', end = '')
    print('')

# Code by Shreyansh Sharma