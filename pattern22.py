"""
Example
Enter the number of rows: 5
E E E E E
D D D D
C C C
B B
A
"""
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, n + 2 - i):
        print(chr(65 + (n - i)), end=" ")
    print()
