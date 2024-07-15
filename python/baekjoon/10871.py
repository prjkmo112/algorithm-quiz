N, X = map(int, input().split(" "))
A = map(int, input().split(" "))
print(' '.join([ str(v) for v in A if v < X ]))