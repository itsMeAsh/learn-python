def find_short(inputString):
    print("Shortest word length: %d" % (min(len(word) for word in inputString.split())))

#main
find_short("This is sample sentence to find the shortest word")
