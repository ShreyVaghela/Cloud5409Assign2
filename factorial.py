import math
import time
f=open("Input.txt","r")
id=1
for line in f:
	start=time.clock()	
	val=math.factorial(int(line))    
	Time=(time.clock()-start)*1e6
	print "Request Id:%d, Time:%.3f,N:%d,result:%d\n"%(id,Time,int(line),val)
	id+=1
