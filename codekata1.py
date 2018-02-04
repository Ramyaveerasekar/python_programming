#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Administrator
#
# Created:     04/02/2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
a=input("enter a number")
if(a>0 and a<100000):
    print("positive")
elif(a<0 ):
    print("negative")
elif(a==0):
    print("zero")
else:
    print("invalid input")
