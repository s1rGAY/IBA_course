a,b = map(float, input().split())
if (a+b).is_integer():
    print(int(a+b))
else:
    print(a+b)