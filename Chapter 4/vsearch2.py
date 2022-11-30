
def search4vowels(word):
    """Finds any vowel in a provided word"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

