"""
Given a random non-negative number, 
you have to return the digits of this number within an array in reverse order.
"""

def digitize(n):
    return list(map(lambda x: int(x), list(str(n)[::-1])))


print(digitize(35231), digitize(0), digitize(23582357), sep="\n")