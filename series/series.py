
def slices(numbers, length):
    slice = []
    if length <= len(numbers) and length != 0:
        l = [numbers[i:i+length] for i in range(0, len(numbers))]
        for i in l:
            if len(i) == length:
                slice.append(list(i))
        slice = [[int(j) for j in i] for i in slice]
        return slice
    else:
        raise ValueError

slices("01234", 4)
