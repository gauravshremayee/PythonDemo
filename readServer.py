#!/usr/bin/python

file=open("/var/lib/jenkins/workspace/GitBuild/etc/server.cfg")


#first open file
#read all lines or read line by line
serverDict={}
lines=file.readlines()
print (type(lines))
for line in lines:
	print (line)
	keyValue=line.split(" ")
	keyValue[0].rstrip()
	keyValue[1].rstrip()
	print(keyValue[0])
	print(keyValue[1])
	print("KeyValue[0] is",keyValue[0])
	serverDict[keyValue[0]]=keyValue[1]

print("___________")
print(serverDict.items())
print("-------")
for key,val in serverDict.items():
	print(key)
	print(val)


print (serverDict['server4'])



