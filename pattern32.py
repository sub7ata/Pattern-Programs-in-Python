"""
Example:
Enter the number of rows: 5
12345
 1234
  123
   12
    1
"""
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" "*(i - 1), end="")
    for j in range(1, n + 2 - i):
        print(j, end="")
    print()
