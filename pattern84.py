"""
Example
Enter a number:5
    5
   545
  54345
 5432345
543212345
 5432345
  54345
   545
    5

"""
n = int(input("Enter a number:"))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(n + 1 - j, end="")
    for k in range(2, i + 1):
        print(n - i + k, end="")
    print()
for i in range(1, n + 1):
    print(" " * i, end="")
    for j in range(1, n + 1 - i):
        print(n + 1 - j, end="")
    for k in range(2, n + 1 - i):
        print(i + k, end="")
    print()