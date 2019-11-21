"""
Example:
Enter the no of rows: 5
     A

    B B

   C C C

  D D D D

 E E E E E
"""
n = int(input("Enter the no of rows: "))
for i in range(1, n + 1):
    print(" "*(n - i), (chr(64 + i) + " ")* i)
    print()
