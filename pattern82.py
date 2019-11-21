"""
Example
Enter number: 5
    A
   A B
  A B C
 A B C D
A B C D E
 B C D E
  C D E
   D E
    E 
"""
num = int(input("Enter number: "))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
for m in range(1,num):
    print(" "*m,end="")
    for n in range(1,num+1-m):
        print(chr(64+m+n),end=" ")
    print()