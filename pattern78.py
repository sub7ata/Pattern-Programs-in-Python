"""
Example
Enter number: 5
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1
"""

num = int(input("Enter number: "))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1,i+1):
        print(i,end=" ")
    print()
for m in range(1,num):
    print(" "*m,end="")
    for n in range(1,num+1-m):
        print(num-m,end=" ")
    print()