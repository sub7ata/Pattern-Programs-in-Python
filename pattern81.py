"""
Example
Enter number: 5
    A
   B B
  C C C
 D D D D
E E E E E
 D D D D
  C C C
   B B
    A

"""
num = int(input("Enter number: "))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
for m in range(1,num):
    print(" "*m,end="")
    for n in range(1,num+1-m):
        print(chr(64+num-m),end=" ")
    print()