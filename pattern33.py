"""
Example:
Enter the number of rows: 5
 EEEEE
  DDDD
   CCC
    BB
     A
"""
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" "*(i - 1), str(chr(65 + (n - i))+ "") * (n + 1 - i))
