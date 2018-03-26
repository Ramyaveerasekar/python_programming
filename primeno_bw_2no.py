#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      VINO
#
# Created:     26/03/2018
# Copyright:   (c) VINO 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
first=int(input())
last=int(input())
for num in range(first,last+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print (num)

