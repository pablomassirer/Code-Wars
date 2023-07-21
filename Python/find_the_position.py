def position(alphabet):

    al_dict = {chr(97 + x): x + 1 for x in range(26)}
    return f"Position of alphabet {al_dict[alphabet]}"


print(position("e"))
