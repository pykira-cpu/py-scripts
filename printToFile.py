

with open('filename.txt', 'a') as f:
	#Open the file you want to write the tect in append('a') mode

	name = input("Your name: ")
	address = input("Your address: ")

	#print the name, address and phone number
	print("Name:{0}, Address: {1} ".format(name,address), file=f)


