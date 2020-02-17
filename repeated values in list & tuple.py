def a(x):
    s=len(x)
    b=[]
    for i in range(s):
        k=i+1
        for j in range(k,s):
            if x[i]==x[j] and x[i] not in b:
                b.append(x[i])
    print(b)
a([1,3,4,5,'a',6,7,3,'b',1,4,5,'a'])
a((0,2,4,6,8,"r","g",6,2,"r"))
