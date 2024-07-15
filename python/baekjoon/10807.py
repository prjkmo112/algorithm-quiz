N = int(input())
V_ARR = map(int, input().split(" "))
V = int(input())
print(len([ v for v in V_ARR if v == V ]))
