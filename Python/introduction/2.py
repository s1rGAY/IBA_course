print()

x=True
y=False
z=False
if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or not y or not y and x:
    print(3)



print()