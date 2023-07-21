from os import strerror
# return masked string
def maskify(cc):
    try:
        return "".join([ "#" for x in range(len(cc) - 4 )]) + cc[-4:]
    except e:
        print("Something went wrong: ", strerror(e))


print(maskify("4556364607935616"))
print(maskify("64607935616"))
print(maskify("1"))
print(maskify(""))
print(maskify("Skippy"))
print(maskify("Nananananananananananananananana Batman!"))