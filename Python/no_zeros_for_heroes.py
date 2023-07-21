
# Implementation from scratch. Could have used rstrip instead for more legibillity and simplicity.
def no_boring_zeros(n):
    l_str_n = list(str(n)[::-1])
    if len(l_str_n) > 1:
        for i in l_str_n:
            if int(i) > 0:
                idx = l_str_n.index(i)
                break
        f_n = int("".join(l_str_n[idx:])[::-1])
    else:
        f_n = n
    return f_n


print(no_boring_zeros(960000))
print(no_boring_zeros(1450))
print(no_boring_zeros(960000))
print(no_boring_zeros(1050))
print(no_boring_zeros(-1050))
print(no_boring_zeros(0))
print(no_boring_zeros(2016))
