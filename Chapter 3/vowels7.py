vowels = {'a','e','i','o','u'}
word = input("Enter a word : ")

found = vowels.intersection(set(word))

for x in found:
    print(x)
