isBuy = input("Did you buy a grocery (yes/no) : ")

if isBuy.lower() == "yes":
	
	nameItem = input("NAME OF THE ITEM : ")
	priceItem = eval(input("PRICE OF THE ITEM : ")
	age = eval(input("AGE : "))
	amount = eval(input("AMOUNT GIVEN : ")
	
	if age >= 60:
		discount = priceItem * 0.052
		total = amount - discount
		print("total")
else:
 	print("Thank you for using the program")