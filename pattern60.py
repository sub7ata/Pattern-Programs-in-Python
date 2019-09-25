"""
Example:
Enter a number: 5
*
**
***
****
*****
****
***
**
*
"""
num = int(input("Enter a number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
for k in range(1,num+1):
    for l in range(1,num+1-k):
        print("*",end="")
    print()

