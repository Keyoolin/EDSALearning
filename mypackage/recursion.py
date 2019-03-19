def sum_array(array):
    if len(array) == 1:
        return array[0]
    else:
        array = np.append(array[:-2],array[-1] + array[-2])
        return sum_array(array)

def fibonacci(n):
    if n<=0:
        return None
    elif n<=2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n-2)

def factorial(n):
    if n < 0:
        return 0:
    elif n == 1:
        return 1
    else:
        return factorial(n-1)*n

def reverse(word):
    if type(word) != str:
        return reverse(str(word))
    elif len(word)==1:
        return word
    else:
        return reverse(word[1:]) + word[0]
