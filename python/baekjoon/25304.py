X = int(input())
N = int(input())
total_price = 0
for i in range(0, N):
    [a,b] = map(int, input().split(" "))

    total_price += a*b

print("Yes" if X == total_price else "No")