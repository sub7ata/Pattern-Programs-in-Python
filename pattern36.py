"""
Example
Enter the number of rows: 5
     1
    2 2
   3 3 3
  4 4 4 4
 5 5 5 5 5
"""
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" "*(n - i), (str(i) + " ") * (2 * i - i))