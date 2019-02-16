n1=int(input())
k=list(map(int,input().split()))
m=sorted(k)
for i in range(0,len(m)):
    print(m[i],end=" ")
