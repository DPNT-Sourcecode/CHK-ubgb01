PRICE_TABLE = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
}


def illegal_input(skus):
    """
    Check if there are any illegal characters.
    Acceptable characters: ABCD, any other character
    will be an illegal character.

    param skus: a String
    @return:    Boolean value
    """
    for letter in skus:
        if letter not in PRICE_TABLE:
            return True
    return False


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    Return the total price for the checkout basket.

    param skus: a String containing the SKUs of all the 
                products in the basket.
    @return:    an Integer representing the total checkout
                value of the items.
    """
    total_checkout = 0
    free_b_count = 0
    free_f_count = 0
    quantity = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
        'F': 0,
    }
    
    if illegal_input(skus):
        return -1

    # sort and reverse string: EBBEEEB --> EEEEBBB
    skus = ''.join(sorted(skus, reverse=True))

    for item in skus:
        quantity[item] += 1
        
        if item == 'F' and quantity[item] % 2 == 0:
            free_f_count +=1
            total_checkout += PRICE_TABLE[item]
        elif item == 'F' and free_f_count:
            free_f_count -= 1
            quantity[item] = 0
        elif item == 'E' and quantity[item] % 2 == 0:
            # keep count of how may B items shopper should get
            free_b_count += 1
            total_checkout += PRICE_TABLE[item]
        elif item == 'B' and free_b_count:
            free_b_count -=1 
            quantity[item] = 0
        elif item == 'B' and quantity[item] % 2 == 0:
            total_checkout += PRICE_TABLE[item] - 15
        elif item == 'A' and quantity[item] % 5 == 0:
            # add back money removed from special offer 3A
            total_checkout += 20
            # reset count
            quantity[item] = 0
        elif item == 'A' and quantity[item] % 3 == 0:
            total_checkout += PRICE_TABLE[item] - 20
        else:
            total_checkout += PRICE_TABLE[item]
    return total_checkout
