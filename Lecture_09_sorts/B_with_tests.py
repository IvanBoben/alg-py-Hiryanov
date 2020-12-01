def how_many_ones(n):
    """Returns the amount of 'ones' inside binary code of number."""
    bin_n = str(bin(n))
    amount = 0
    for i in range(len(bin_n)):
        if bin_n[i] == '1':
            amount += 1
    return amount

def test(func):
    print('Test: ', end='')
    print('OK' if func(5) == 2 else 'Fail')

test(how_many_ones)