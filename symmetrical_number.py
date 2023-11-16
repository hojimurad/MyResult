import random

a = int(input())


# print((a+1)//(int(str(int((a*a)**0.5))[::-1])+1))
#


b = int(str(abs(a))[::-1])
print(a-b+1)