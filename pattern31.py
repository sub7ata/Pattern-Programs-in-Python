"""
Example:
Enter the number of rows: 5
 55555
  4444
   333
    22
     1
"""
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" "*(i - 1), (str(n + 1 - i) + "")*(n + 1 - i))
