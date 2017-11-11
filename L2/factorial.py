# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    ret=1
    for i in range(n,0,-1):
        ret*=i
    return ret




print factorial(4)
#>>> 24
#print factorial(5)
#>>> 120
#print factorial(6)
#>>> 720

