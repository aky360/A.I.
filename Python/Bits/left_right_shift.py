"""
Bitwise left shift:   Shifts the bits of the number to the left and fills 0 on voids right as a result. 
		      Similar effect as of multiplying the number with some power of two.
let's a number x
		      x<<n   it left shifts the 'x' into 'n' times and its output is  ==>>  x*2^n.
											
Bitwise right shift:  Shifts the bits of the number to the right and fills 0 on voids left( fills 1 in the case of a negative number) as a result. 
		      Similar effect as of dividing the number with some power of two.
let's a number x
		      x>>n   it right shifts the 'x' into 'n' times and its output is  ==>>  x/2^n.
"""


a = 10
b = 4
# Print bitwise AND operation
print("a & b =", a & b)            #a & b = 0
# Print bitwise OR operation
print("a | b =", a | b)		   #a | b = 14
# Print bitwise NOT operation
print("~a =", ~a)		   #~a = -11
# print bitwise XOR operation
print("a ^ b =", a ^ b)		   #a ^ b = 14


a = 10
b = -10
# print bitwise right shift operator
print("a >> 1 =", a >> 1)                 #a >> 1 = 5
print("b >> 1 =", b >> 1)	          #b >> 1 = -5

 
a = 5
b = -10
# print bitwise left shift operator
print("a << 1 =", a << 1)                 #a << 1 = 10
print("b << 1 =", b << 1)		  #b << 1 = -20
