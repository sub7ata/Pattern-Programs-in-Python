"""
Example:
Enter the number of input: 5
     *
    ***
   *****
  *******
 *********
"""
n = int(input("Enter the number of input: "))
for i in range(1, n + 1):
    print(" "*(n - i),"*"*(2 * i - 1))
