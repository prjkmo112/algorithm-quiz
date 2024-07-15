N,M = map(int, input().split(" "))

sol = 2

if sol == 1:
    # sol 1
    basket = [[] for i in range(0,N)]
    for _i in range(0, M):
        i,j,k = map(int, input().split(" "))
        for basket_idx in range(i-1, j):
            basket[basket_idx].append(k)

    res = []
    for v in basket:
        if len(v) == 0:
            res.append('0')
        else:
            res.append(str(v[-1]))

    print(' '.join(res))
elif sol == 2:
    # sol 2
    basket = ['0' for i in range(0,N)]
    for _i in range(0, M):
        i,j,k = map(int, input().split(" "))
        for basket_idx in range(i-1, j):
            basket[basket_idx] = str(k)

    print(' '.join(basket))
