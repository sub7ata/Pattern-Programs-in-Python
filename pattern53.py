"""
Example:
Enter a number: 5
 I I I I I I I I I
   G G G G G G G
     E E E E E
       C C C
         A
"""
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    print("  " * (i - 1), end=" ")
    for j in range(1, num + 2 -i):
        print(chr(65 + 2 * num - i * 2), end= " ")
    for k in range(2, num + 2 - i):
        print(chr(65 + 2 * num - i * 2), end= " ")
    print()
