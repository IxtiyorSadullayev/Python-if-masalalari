a=int(input("a ni kiriting: "))
b=int(input("b ni kiriting: "))
c=int(input("c ni kiriting: "))
d=int(input("d ni kiriting: "))

if a==b==c:
    print(d)
elif b==c==d:
    print(a)
elif c==d==a:
    print(b)
elif a==b==d:
    print(c)
else: 
    print("Sizda 3 ta son bir hil emas")