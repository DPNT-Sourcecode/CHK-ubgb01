from collections import Counter


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
    sku_table = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
    }
    for letter in skus:
        try:
            total_checkout += sku_table[letter]
        except KeyError:
            return -1
    return total_checkout 
