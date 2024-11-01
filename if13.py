a=int(input("a ni kiriting: "))
b=int(input("b ni kiriting: "))
c=int(input("c ni kiriting: "))

if a>b>c or a<b<c:
    print(b)
elif a>c>b or a<c<b:
    print(c)
elif b>a>c or b<a<c:
    print(a)