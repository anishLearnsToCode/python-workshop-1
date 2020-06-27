number = int(input())

sum = 0
for i in range(1, number + 1):
    sum += i
print(sum)

fact = 1
for i in range(1, number + 1):
    fact *= i
print(fact)
