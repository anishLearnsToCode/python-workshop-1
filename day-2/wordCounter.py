# sentence = input().split(' ')
# print(sentence)
#
# frequency = {}
# for word in sentence:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1
#
# print(frequency)

dictionary = {
    'a': 10,
    'b': 2,
    'c': 3
}

print(dictionary)
del dictionary['b']
del dictionary['a']
print(dictionary)

a = 10
pi = 3.14
del a
del pi
