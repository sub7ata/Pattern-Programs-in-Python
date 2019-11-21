"""
Example:
Enter the no of rows: 5
A B C D E
A B C D
A B C
A B
A

"""
n = int(input("Enter the no of rows: "))
for i in range(1, n + 1):
    for j in range(1, n + 2 - i):
        print(chr(64+j), end=" ")
    print()
