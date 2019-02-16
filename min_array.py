n1=int(input())
k=list(map(int,input().split()))
m=k[0]
for i in range (0,n1):
	if k[i]<m:
		m=k[i]
print (m)
