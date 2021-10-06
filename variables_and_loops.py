import numpy as np
#this allows us to use the numpy package much like <iostream>

def main():
	i = 0
	n = 10
	x = 119.0
	#declaring integers with just a number, and 
	#declaring floats with "."

	y = np.zeros(n,dtype=float)
	#this creates an array "y"
	#"zeros" is a function in numpy that prints array of "0"s
	#"n" is the length of "0"s
	#"dtype" designates the data type (int, long, float, etc.)

	for i in range(n):
		#creates a for loop in range of [i, n-1]

		y[i] = 2.0 * float(i) + 1
		#sets y = 2i + 1 as floats

	for y_element in y:
		print(y_element)
		#prints out every element in y in sequence
if __name__=="__main__":
	main()
	#executes the main function while checking it exists