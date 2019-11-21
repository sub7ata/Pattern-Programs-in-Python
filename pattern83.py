"""
Example
Enter number: 5
    5
   454
  34543
 2345432
123454321
 2345432
  34543
   454
    5
"""
num = int(input("Enter number: "))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1,i+1):
        print(num-i+j,end="")
    for k in range(2,i+1):
        print(num+1-k,end="")
    print()
for i in range(1,num+1):
    print(" "*i,end="")
    for j in range(1+i,num+1):
        print(j,end="")
    for k in range(2,num+1-i):
        print(num+1-k,end="")
    print()