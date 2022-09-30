while(True):
    a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = b**2 - 4*a*c
    print(d)
    if(d>0):
        x1 = (-b + d**0.5)/2/a
        x2 = (-b - d**0.5)/2/a
        print("x1: ",x1," x2: ",x2)
    elif d == 0:
        print("x: " + -b/2/a)
    else:
         print("нет корней")

