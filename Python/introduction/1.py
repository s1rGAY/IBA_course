# This is a sample Python script.
data = input().lower()
data = list(data)
print(data)
l = len(data)
l = l//2
for i in range(l):
    if data[i] != data[-1-i]:
        print("It's not palindrome")
        break
else:
    print("It's palindrome")
print()
