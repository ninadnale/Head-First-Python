
def search4vowels(word:str) -> set:
    """Return a set of vowels found in given word"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))

