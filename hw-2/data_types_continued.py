s = "I am a string."
print(type(s))

yes = True
print(type(yes))

no = False
print(type(no))

#list -- ordered and changeable

alpha_list = ["a", "b", "c"] #list initialization
print(type(alpha_list)) #will say tuple
print(type(alpha_list[0])) #will say string
alpha_list.append("d") #will add "d" to list end
print(alpha_list) #will print list

#Tuple -- ordered and unchangeable

alpha_tuple = ["a", "b", "c"]
print(type(alpha_tuple)) #will say tuple

try:
	alpha_tuple[2] = "d"
except TypeError:
	print("We can't add elements to tuples!") #prints this message
print(alpha_tuple) #prints tuple