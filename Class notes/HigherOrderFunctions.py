def __verify_int(n):
    try:
        int(n)
    except ValueError:
        raise ValueError("the mathseries moodule only works with inetgers.")
    else:
        return n
        
def series_sum_factories(series_term):
    def series(maxN):
        totalsum = 0
        i = 1
        tested_maxN = __verify_int(maxN)
        while i <= tested_maxN:
            totalsum = totalsum +series_term(i)
            i = i + 1
        return totalsum
    return series

if __name__ == "__main__":
    sum_numbers = series_sum_factories(lambda x: x)   #this allows us to extend the function instead of having to modify it, al
    sum_squares = series_sum_factories(lambda x: x * x) #all we have to do is write another seires and change lambda

    result = sum_numbers('w')

    print(result)