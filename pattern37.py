"""
Example:
Enter the number of rows: 5
     A
    BBB
   CCCCC
  DDDDDDD
 EEEEEEEEE
"""
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" "*(n - i),(str(chr(64 + i) + "") * (2 * i - 1)))