#Write function calc(m, n) that multiplies two variables m and n of type int, 
# then divides the product by two, and outputs the remainder with respect to division
#  by 7.

def calc(m:int, n:int)->int:
    	return ((n * m // 2) % 7)
print(calc(18, 2))
