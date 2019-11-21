"""
Example:
Enter the number of rows: 5
 5 5 5 5 5 5 5 5 5
  4 4 4 4 4 4 4
   3 3 3 3 3
    2 2 2
     1
"""
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" " * (i - 1), end=" ")
    for j in range(0, n + 1 - i ):
        print(n + 1 - i, end=" ")
    for k in range(1, n + 1 - i):
        print(n + 1 - i, end=" ")
    print()


