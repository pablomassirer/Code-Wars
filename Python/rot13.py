"""ROT13 is a simple letter substitution cipher that replaces a letter 
with the letter 13 letters after it in the alphabet. 
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, 
they should be returned as they are. 
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""

def rot13(message):
    letter_upper = [y for y in range(len(message)) if message[y].isupper()]
    message = message.lower()
    alphabet = [chr(x) for x in range(ord("a"), ord("z") + 1)]
    result = [alphabet[(alphabet.index(message[x]) + 13)-len(alphabet)] 
                if message[x] in alphabet and alphabet.index(message[x]) + 13 > len(alphabet) - 1
                else alphabet[alphabet.index(message[x]) + 13] 
                if message[x] in alphabet else message[x] 
                for x in range(len(message))
            ]
    for i in letter_upper:
        result[i] = result[i].upper()
    return "".join(result)

try:
    result = rot13("aA bB zZ 1234 *!?%")
    result2 = rot13("ZZZZZZZZZzzzzzzzzz")
    assert result == "nN oO mM 1234 *!?%"
    print(result2)
except AssertionError:
    print(f"Result value: {result} does not match inputed one.")

    


