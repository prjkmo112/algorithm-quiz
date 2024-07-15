max = 0
max_idx = 0
for i in range(1,10):
    inp = int(input())
    if (inp > max):
        max = inp
        max_idx = i

print(max)
print(max_idx)