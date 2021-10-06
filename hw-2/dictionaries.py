#define a dictionary data structure

#dictionaries have a key:value structure
example_dict = {
	"class" : "ASTR 119",
	"prof"  : "Brant",
	"awesomeness" : 10
}

print(type(example_dict)) #prints dict

#get value via key
course = example_dict["class"]
print(course)

#change a value via key
example_dict["awesomeness"] +=1 #increase awesomeness by 1
print(example_dict)

#print dictionary element by element
for x in example_dict.keys():
	print(x,example_dict[x])