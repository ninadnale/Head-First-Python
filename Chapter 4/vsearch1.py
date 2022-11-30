
def search4vowels():
    """Finds any vowel in an asked-for word"""
    vowels = set('aeiou')
    word = input('Enter a word you want to search for vowels : ')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

