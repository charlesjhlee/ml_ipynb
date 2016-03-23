listOfNumbers = [1, 2, 3, 4, 5, 6]

for number in listOfNumbers:
    print number,
    if (number % 2 == 0):
        print "is even"
    else:
        print "is odd"
        
print "All done."