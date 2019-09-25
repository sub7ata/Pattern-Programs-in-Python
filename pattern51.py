"""
Example:
Enter the number: 5
123456789
 1234567
  12345
   123
    1
"""
n = int(input("Enter the number: "))
for i in range(1, n + 1):
    print(" " * (i -1),end="")
    for j in range(1, n + 2 - i):
        print(j,end="")
    for k in range(2, n + 2 - i):
        print(n + k -i,end="")
    print()

