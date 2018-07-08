from collections import Counter


PRICE_TABLE = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}


def illegal_input(skus):
    """
    Check if there are any illegal characters.
    Acceptable characters: ABCD, anything else will be an illegal character.

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
    param skus: a String containing the SKUs of all the 
                products in the basket.
    @return:    an Integer representing the total checkout
                value of the items.
    """
    total_checkout = 0
    

    if illegal_input(skus):
        return -1

    checkout_basket = Counter(x[0] for x in skus if x)
    for item, quantity in checkout_basket.items():
        if item == 'A' and quantity == 3:
            price = 130
            total_checkout += price
        elif item == 'B' and quantity == 2:
            price = 45
            total_checkout += price
        else:
            total_checkout += quantity * PRICE_TABLE[item]
    return total_checkout 
