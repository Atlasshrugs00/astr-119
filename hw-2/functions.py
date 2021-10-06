import numpy as np
import sys
#imports library
#sys is operating system

def expo(x):
	return np.exp(x)
	#returns the np e^x function

def show_expo(n):
	for i in range(n):
		print(expo(float(i)))
		#calls expo function

def main():
	n = 10

	if(len(sys.argv)>1):
		n = int(sys.argv[1])
		#check if there is a command line argument provided
		#if an argument was provdied, use it for n
	show_expo(n)

if __name__=="__main__":
	main()