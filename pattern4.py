"""
Example:

Enter the no row: 5
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E

"""
n = int(input("Enter the no row: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(chr(64+i), end=" ")
    print()

