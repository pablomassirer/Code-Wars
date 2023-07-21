"""
Write a method that returns true if a given parameter is a power of 4, and false if it's not. 
If parameter is not an Integer (eg String, Array) method should return false as well.

(In C# Integer means all integer Types like Int16,Int32,.....)

isPowerOf4 1024 #should return True
isPowerOf4  102 #should return False
isPowerOf4   64 #should return True
"""


def powerof4(n):
    result = 1
    power = 4
    if str(n).isnumeric():
        while result < n:
            result *= power
        if result == n or n == 1:
            return True
    return False


print(powerof4(64))
print(powerof4(102))
print(powerof4(1024))
