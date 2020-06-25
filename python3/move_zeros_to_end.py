def move_zeros(array):
    nonZeros = []
    zeros = []

    for i in range(len(array)):
        if array[i] == 0 or array[i] == 0.0:
            if type(array[i]) == int or type(array[i]) == float:
                zeros.append(array[i])
            else: nonZeros.append(array[i])
        else:
            nonZeros.append(array[i])

    print(nonZeros + zeros)

move_zeros([1, 12, 0, 'a', 'b', False, 123])
