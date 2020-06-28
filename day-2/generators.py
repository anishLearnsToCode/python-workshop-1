vowels = ('a', 'e', 'i', 'o', 'u')


def isVowel(character):
    return character in vowels


# { x^2 | for all x in natural numbers}
val = [1 for i in range(5)]
print(val)

val = [i ** 2 for i in range(1, 11)]
print(val)

word = 'balleiuhggbbbuugge'
val = ' '.join([character if isVowel(character) else '_' for character in word])
print(val)

number = int(input())
val = [i ** 2 for i in range(1, number + 1)]
print(val)
