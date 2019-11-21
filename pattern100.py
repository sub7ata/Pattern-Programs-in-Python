"""
Example
Enter a number: 5
**
**
****
****
******
******
********
********
**********
**********
"""
num = int(input("Enter a number: "))
for i in range(1,2*num+1):
    if i%2==0:
        print("*"*i,end=" ")
    else:
        print("*"*(i+1),end=" ")
    print()