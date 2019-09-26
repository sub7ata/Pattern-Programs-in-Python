"""
Example:
Enter a number: 5
E
D E
C D E
B C D E
A B C D E
B C D E
C D E
D E
E 
"""
num = int(input("Enter a number: "))
for i in range(1, num+1):
    for j in range(1,i+1):
        print(chr(64+num-i+j),end=" ")
    print()
for a in range(1,num+1):
    for b in range(1, num-a+1):
        print(chr(64+b+a),end=" ")
    print()
