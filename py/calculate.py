import sys

sum = 0
rate = 0.0
for line in open("sum.log","r"):
	a = line
	data=a.split(" ")
	tps = data[0]
	rate= data[1]
	sum = sum+float(tps)
print (rate,sum)

