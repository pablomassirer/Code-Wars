"""
Write a function named first_non_repeating_letter that takes a string input, 
and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', 
since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, 
but the function should return the correct case for the initial letter. For example, 
the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, 
it should return an empty string ("") or None -- see sample tests.
"""


def first_non_repeating_letter(s):
    s_lower = s.lower()
    occurrences = {x:s_lower.count(x) for x in s_lower}
    first_char_not_repeated = ([x for x in occurrences.keys() if occurrences[x] == 1]
                                                    if 1 in occurrences.values() 
                                                    else "")
    if first_char_not_repeated: 
        first_chr_n_rptd = first_char_not_repeated[0]
        result = s[s_lower.index(first_chr_n_rptd)]
    else:
        result = ""
    print(result)
    return result
first_non_repeating_letter("stress")
first_non_repeating_letter("abba")
first_non_repeating_letter("a")
first_non_repeating_letter("sTreSS")
first_non_repeating_letter("6X XHdCYJ kB 6MKa.CMsdG9aYJa s5aBU9USKkChG.ChSH5")