"""
Example:
Enter the number of rows: 5
*********
 *******
  *****
   ***
    *
"""
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" " * (i - 1), end="")
    for j in range(1, n + 2 - i):
        print("*", end="")
    for k in range(1, n + 1 - i):
        print("*",end="")
    print()
