"""
Example:
Enter a number: 5
     A
    B B
   C C C
  D D D D
 E E E E E
"""
num = int(input("Enter a number: "))
for i in range(1, num+1):
    print(" "*(num-i),end=" ")
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
