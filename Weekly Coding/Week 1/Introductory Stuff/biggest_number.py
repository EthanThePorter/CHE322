# -*- coding: utf-8 -*-
"""
script to check biggest number than one in double precision
"""
bits_for_exponent = 53

# the integer value of the numbers is one
biggest_number = 1
next_biggest_number = 1

# negative powers start from 1
for i in range(1, bits_for_exponent):
    biggest_number += 1 * 2 ** (-i)
    print("with the power being", i, "the number is", biggest_number)

print("the number is ", biggest_number * (2 ** 1023))

# second biggest number
# all ones in mantissa except one zero
# so we would have 0*2**0

# either calculate this
# for i in range(1,bits_for_exponent-1):
#	next_biggest_number += 1*2**(-i)

# or
next_biggest_number = biggest_number - (1 * 2 ** -52)

print("next biggest number is ", next_biggest_number * (2 ** 1023))
print("and their difference is", biggest_number * (2 ** 1023) - next_biggest_number * (2 ** 1023))
