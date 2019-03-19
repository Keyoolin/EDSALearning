def sum_array(array):
    if len(array) == 1:
        return array[0]
    else:
        array = np.append(array[:-2],array[-1] + array[-2])
        return sum_array1(array)
