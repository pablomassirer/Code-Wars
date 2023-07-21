def is_isogram(string):
    if len(string) > 0:
        str_split = [x for x in string.lower()]
        count_occurences = [str_split.count(x) for x in str_split]
        if max(count_occurences) == 1:
            return True
        else:
            return False
    return True


print(is_isogram("Dermatoglyphics"))
print(is_isogram("moose"))
print(is_isogram(""))
print(is_isogram("moOse"))
