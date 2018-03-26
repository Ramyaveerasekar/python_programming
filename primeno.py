#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      vino
#
# Created:     23/03/2018
# Copyright:   (c) VINO 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
num=int(input())
if num>1:
    for i in range(2,1000):
        if (num%i==0):
            print num,("not a prime")
            break
    else:
        print("prime")

