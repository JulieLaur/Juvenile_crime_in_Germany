
def normal_round(num, ndigits=0):
    '''
    Python 3 rounds values to the next even number.
    This is what is usual in banking business?!
    This function rounds as expected.
    To be further explored...
    '''
    digit_value = 10 ** ndigits
    return int(num * digit_value + 0.5) / digit_value