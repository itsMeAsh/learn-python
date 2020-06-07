def high_and_low(numbers):
    #Split and convert string into integer
    result = [int(value) for value in numbers.split(" ")]
    print ("%i %i" % (max(result),min(result)))

#main
high_and_low("12 23 34 45 -12345")
