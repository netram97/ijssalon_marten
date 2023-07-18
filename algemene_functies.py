def mijn_functie_1(num):
    return(num ** 2)

def mijn_functie_2(num_input):
    # Make the list of the numbers
    numbers = num_input.split(',')
    numbers = [int(num) for num in numbers]
    num_list = numbers

    # Calculate stuff
    total_sum = num_list[0] + num_list[1]
    min_value = num_list[0] - num_list[1]
    product = num_list[0] * num_list[1]
    quotient = int(num_list[0] / num_list[1])
    Teruggeefwaarde = [total_sum, min_value, product, quotient]
    return Teruggeefwaarde