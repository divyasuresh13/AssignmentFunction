values=10
result= list(map(lambda x:2**x,range(values)))
print("the total values are:",values)
for i in range(values):
	print("2 raised to power",i,"is",result[i])
	