"""
Example:
    Enter the number of row: 5
    *
    * *
    * * *
    * * * *
    * * * * *
"""

#Case - 1

#n = int(input("Enter the number of row: "))
#for i in range(1,n + 1):
#    for j in range(1, i):
#        print("* ", end=" ")
#    print()

#Case - 2

n = int(input("Enter the number of row: "))
for i in range(1, n+1):
    print("* "*i)