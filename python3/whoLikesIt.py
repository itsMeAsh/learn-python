def likes(names):
    n = len(names)
    print( {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2))

#main
likes(["Robert", "Zeke", "Landon", "Someone"])
