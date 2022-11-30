
def search4vowels(word:str) -> set:
    """Return a set of vowels found in given word"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Search the provided set of letters in a phrase"""
    return set(letters).intersection(set(phrase))
