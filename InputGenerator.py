from random import randint
f=open("Input.txt","w+")#The Input.txt will be made in a folder from which the program is executed
for _ in range(100):
    val=randint(0,100)
    f.write("%d\n"%(val))
    print(val)
f.close()