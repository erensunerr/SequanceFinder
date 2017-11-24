#!/usr/bin/python3
while True:
	a = float(input("1.Number = "))
	b = float(input("2.Number = "))
	c = int(input("How many numbers in between : "))
	d = int(input("By Adding or Subtracting 1 | By Division or Multiplication 0\n"))
	if d == 1 :
		z =((b-a)/c)
		p = 0
		while p < 10:
			print(a) 
			a +=z
			p += 1
		print("Adds = "+str(z))
	elif d == 0:
		z = (b/a)**(1/(c+1))
		p = 0
		while p < 10:
			print (a)
			a = a*z
			p += 1
		print("Multiply by = "+str(z))
#Elif
