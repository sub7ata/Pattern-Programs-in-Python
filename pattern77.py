"""
Example
Enter number: 5
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    * 
"""

num = int(input("Enter number: "))
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for m in range(1,num):
    print(" "*m,end="")
    for n in range(1,num+1-m):
        print("*",end=" ")
    print()