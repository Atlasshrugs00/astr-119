#python exceptions demonstrated

try:
	print(a) #a is not defined yet
except:
	print("a is not defined!")

#specific errors help
try:
	print(a)
except NameError:
	print("a is still not defined")
except:
	print("something else went wrong")

print(a)