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
num=int(raw_input("Enter a number"))
sum1=0
n=num

while num!=0:
	rem=num%10
	sum1=sum1*10+rem
	num=num/10
if sum1==n:
	print n, "is palindrome"
else:
	print n, "is not palindrome"
