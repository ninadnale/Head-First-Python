
def search4vowels(word):
    """Return a boolean value based on any vowels found"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)

