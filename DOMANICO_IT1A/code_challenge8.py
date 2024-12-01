sum = 0
sumOdd = 0
for i in range(0,10):
    number = eval(input("Enter your number : "))
    sum += number
    
    oddNumber = number % 2
    sumOdd += oddNumber
    
    if sumOdd is not 0:
		sumOdd += oddNumber
        
print(sumOdd)