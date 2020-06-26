def mySum(*numbers):
    ans = 0
    for number in numbers:
        ans += number
    return ans


print(mySum(1, 2, 3))

vowels = ('a', 'e', 'i', 'o', 'u')


def isVowel(character):
    return character in vowels


def createVisibleAlphabets(word):
    return ''.join([word[i] if isVowel(word[i]) else '_' for i in range(len(word))])


test = ''.join(['_' for i in range(5)])
print(createVisibleAlphabets('baaaaaad'))
