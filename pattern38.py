"""
Example:
Enter the number of rows: 5
     A
    CCC
   EEEEE
  GGGGGGG
 IIIIIIIII
"""
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" "*(n - i), (str(chr(64 + 2 * i - 1)+"")) * (2 * i - 1))
