def get_list(input_string):
    """Removes spaces from input string with numbers."""
    A_list = []
    temp_str = ''
    for i in range(len(input_string)):
        if input_string[i] != ' ':
            temp_str += (input_string[i])
        else:
            A_list.append(int(temp_str))
            temp_str = ''
    A_list.append(int(temp_str))
    return A_list

def money(price, delta, weeks):
    """Price grows by delta every day. Return how match money you spend
    buying every day."""
    price -= delta
    sum_price = 0
    for i in range(7 * weeks):
        price += delta
        sum_price += price
    return sum_price

input_string = get_list(str(input()))
print(money(*input_string))