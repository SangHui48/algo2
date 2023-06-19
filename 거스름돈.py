n = 1260
answer = 0

data = [500, 100, 50, 10]

for item in data:
    answer += (n // item)
    n %= item

print(answer)