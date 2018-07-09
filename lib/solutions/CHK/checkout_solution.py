PRICE_TABLE = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
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
    quantity = {}

    if illegal_input(skus):
        return -1

    for item in skus:
        try:
            quantity[item] += 1
        except KeyError:
            quantity[item] = 1
            
        if item == 'A' and quantity[item] % 3 == 0:
            total_checkout += PRICE_TABLE[item] - 20
        elif item == 'B' and quantity[item] % 2 == 0:
            total_checkout += PRICE_TABLE[item] - 15
        else:
            total_checkout += PRICE_TABLE[item]
    return total_checkout
