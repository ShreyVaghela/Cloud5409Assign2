import time
f=open("Input.txt","r")
id=1

for line in f:
	start=time.clock()
	a=0
	b=1
	num=0
	if int(line)==1:
		Time=(time.clock()-start)*1e6
		print "Request Id:%d, Time:%.3f,N:%d,result:%d\n"%(id,Time,int(line),a)
		id+=1
	else:
		arr=[]
		while num<int(line):
			arr.append(a)
			temp=a+b
			a=b
			b=temp
			num+=1
		Time=(time.clock()-start)*1e6
		print "Request Id:%d, Time:%.3f,N:%d,result:%s\n"%(id,Time,int(line),arr)
		id+=1
    

