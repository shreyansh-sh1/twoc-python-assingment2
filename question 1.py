print("Enter number ")
a = int(input())
b = a           #for comparision



# For Prime
c = 0
for i in range(1, a + 1):
    if a % i == 0:
        c = c+1
if c == 2:
    print(a, "is Prime")
else:
    print(a, "is not Prime")

# For Even-Odd
if a % 2 == 0:
    print(a, "is Even")
else:
    print(a, "is Odd")


# For Palindrome
rev = 0
while b != 0:
    rem = b % 10
    rev = rev * 10 + rem
    b = b // 10
if rev == a:
    print(a, "is Palindrome")
else:
    print(a, "is not Palindrome")

# For Armstrong
d = a
sum = 0
while d != 0:
    rem2 = d % 10
    sum = sum + (rem2 * rem2 * rem2)
    d = d // 10
if sum == a:
    print(a, "is Armstrong number")
else:
    print(a, "is not Armstrong number")


# Code by Shreyansh Sharma