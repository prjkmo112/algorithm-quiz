N = int(input())
arr = list(map(int, input().split(" ")))

# sol 1
print(str(max(arr)) + " " + str(min(arr)))

# sol 2
max = arr[0]
min = arr[0]
for v in arr:
    if v < min:
        min = v
    if v > max:
        max = v

print(f'{max} {min}')