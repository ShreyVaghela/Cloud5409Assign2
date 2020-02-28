f=open("Input.txt","r")
for line in f:
	a=0
	b=1
	num=0
	if int(line)==1:
		print(a)
	else:
		print "\n"
		while num<int(line):
			print a,
			temp=a+b
			a=b
			b=temp
			num+=1
    

