"""
Example
Enter a number: 5
        *
       * *
      * * *
     * * * *
    * * * * *
      * * *
     * * * *
    * * * * *
   * * * * * *
  * * * * * * *
    * * * * *
   * * * * * *
  * * * * * * *
 * * * * * * * *
* * * * * * * * *
   * * *
   * * *
   * * *
   * * *
   * * *

"""
num = int(input("Enter a number: "))
for a in range(1,num+1,2):
    for i in range(1,num+1):
        print(" "*(2*num-i-a),end="")
        for j in range(1,i+a):
            print("*",end=" ")
        print()
for b in range(1,num+1):
    print(" "*(num-2),end="")
    print("* "*3)