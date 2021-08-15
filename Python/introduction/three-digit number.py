n = abs(float(input()))
b = abs(n-int(n))
b = ((b % 0.1) + (b % 100 // 10) + (b // 100))
print(int((n % 10) + (n % 100 // 10) + (n // 100)+b))
