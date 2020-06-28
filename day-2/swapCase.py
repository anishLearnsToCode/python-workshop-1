sentence = input()

ans = ''
for character in sentence:
    # value 1 if condition else value2
    ans += character.lower() if character.isupper() else character.upper()

print(ans)

# print('hello' if True else [1, 2, 3])
