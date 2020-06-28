# # keys --> values
# # keys are unique
#
# words = {
#     'i': 10,
#     'am': 10,
#     'bat': 45
# }
#
# a = [1, 2, 3]
# # print(words['bat'])
#
# for val in words.items():
#     print(val)
#
# words['ball'] = 89
# words['bat'] = 0
# print(words['bat'])
# print(words.get('ball')) # --> print(words[0])
# print(words)

person = {
    'firstName': 'anish',
    'lastName': 'sachdeva',
    'age': 21,
    'hasBeard': True,
    'complexProperty': {
        'prop1': 'hello',
        'prop2': [2, 5, 7, 11],
        'prop3': False,
        'prop4': (1, 2, 3),
        'prop5': {
            'abc': ['a', 'b']
        }
    }
}

# for item in person.items():
#     print(item)

# for item in person['complexProperty'].items():
#     print(item)
#
# person['complexProperty']['prop2'].append([13, 17])
# print(person['complexProperty']['prop2'])
print(person.keys())
print(person.values())
print(person.items())
