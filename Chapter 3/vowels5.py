vowels = ['a' ,'e' ,'i' ,'o' ,'u' ]
word = input("Enter a word to get count of vowels : ")

found = {}

for letter in word:
    if letter in vowels:
        if letter not in found:
            found[letter] = 0
        found[letter] += 1


for k,v in sorted(found.items()):
    print(k,"was found",v,"times.")
