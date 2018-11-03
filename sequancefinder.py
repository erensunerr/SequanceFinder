#!/usr/bin/python3
def main():
    while True:
    	a = float(input("1.Number = "))
    	b = float(input("2.Number = "))
    	c = int(input("How many numbers in between : "))
    	d = int(input("By Adding or Subtracting 1 | By Division or Multiplication 0\n"))
        #TODO: add harmonic series
        print('=',findSeq(a,b,c,d))

def findSeq(num1,num2, numInBet, method):
    """
    Function to find sequences.
    >>>findSeq(5,25,3,1):
    5
    >>>findSeq(3,81,2,0)
    9
    """
    if method == 1 : # Arithmetic
		z =((num2-num1)/numInBet)
		p = 0
		while p < 10:
			print(num1)
			num1 += z
			p += 1
	elif method == 0:#Geometric
		z = (num2/num1)**(1/(numInBet+1))
		p = 0
		while p < 10:
			print (num1)
			num1 = num1*z
			p += 1

    return z
