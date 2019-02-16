n1,a1,d1=map(int,input().split())
i=1
ap=0
while i<=n1:
	ap=ap+a1
	a1=a1+d1
	i=i+1
print(ap)
