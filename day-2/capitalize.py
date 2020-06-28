line = input()
words = line.split(' ')
print(words)

for word in words:
    print(word.capitalize())
    line = line.replace(word, word.capitalize())

print(line)
