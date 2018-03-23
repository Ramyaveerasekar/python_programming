#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      VINO
#
# Created:     23/03/2018
# Copyright:   (c) VINO 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
num=int(input("enter the number"))
if num>1:
    for i in range(2,1000):
        if (num%i==0):
            print("not a prime")
        else:
            print("prime")
        break
