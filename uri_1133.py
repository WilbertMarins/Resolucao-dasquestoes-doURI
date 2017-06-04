X = int(input())
Y = int(input())

if X < Y:
    c=X+1
    while X < c < Y:
        if c%5==2 or c%5==3:
            print(c)
        c+=1
if Y < X:
    c=Y+1
    while Y < c < X:
        if c%5==2 or c%5==3:
            print(c)
        c+=1
