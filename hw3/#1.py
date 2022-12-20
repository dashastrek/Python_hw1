a = [0, 1, 2, 3, 4]
sum = 0
for i in range(len(a)):
    if a[i] % 2 == 1:
        sum += a[i]
print(sum)
