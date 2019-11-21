"""
Example:
Enter number: 5
E D C B A
 D C B A
  C B A
   B A
    A
"""
num = int(input("Enter number: "))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    for j in range(1,num+2-i):
        print(chr(65+num+1-i-j),end=" ")
    print()