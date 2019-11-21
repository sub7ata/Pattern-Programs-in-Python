"""
Example
Enter the number of rows: 5
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, n + 2 - i):
        print(n + 1 - j, end=" ")
    print()
