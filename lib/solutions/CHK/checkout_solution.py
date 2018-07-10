PRICE_TABLE = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50
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
    quantity = {}
    total_checkout = 0
    free_b_count = 0
    free_f_count = 0
    free_m_count = 0
    free_q_count = 0
    free_u_count = 0
    
    if illegal_input(skus):
        return -1

    # sort and reverse string: EBBEEEB --> EEEEBBB
    skus = ''.join(sorted(skus, reverse=True))

    for item in skus:
        try:
            quantity[item] += 1
        except KeyError:
            quantity[item] = 1
        
        # 3V for 130
        if item == 'V' and quantity[item] % 3 == 0:
            total_checkout += PRICE_TABLE[item] - 10
            quantity[item] = 0
        # 2V for 90
        elif item == 'V' and quantity[item] % 2 == 0:
            total_checkout += PRICE_TABLE[item] - 10
        # 3U get one U free
        elif item == 'U' and quantity[item] % 3 == 0:
            free_u_count += 1
            total_checkout += PRICE_TABLE[item]
        elif item == 'U' and free_u_count:
            free_u_count -= 1
            quantity[item] = 0

        # 3R get one Q free
        elif item == 'R' and quantity[item] % 3 == 0:
            free_q_count += 1
            total_checkout += PRICE_TABLE[item]
        elif item == 'Q' and free_q_count:
            free_q_count -= 1
            quantity[item] = 0
        # 3Q for 80
        elif item == 'Q' and quantity[item] % 3 == 0:
            total_checkout += PRICE_TABLE[item] - 10
        # 5P for 200
        elif item == 'P' and quantity[item] % 5 == 0:
            total_checkout += PRICE_TABLE[item] - 50
        # 3N get one M free
        elif item == 'N' and quantity[item] % 3 == 0:
            free_m_count += 1
            total_checkout += PRICE_TABLE[item]
        elif item == 'M' and free_m_count:
            free_m_count -= 1
            quantity[item] = 0
        # 2K for 150
        elif item == 'K' and quantity[item] % 2 == 0:
            total_checkout += PRICE_TABLE[item] - 10
        # 10H for 80
        elif item == 'H' and quantity[item] % 10 == 0:
            total_checkout += PRICE_TABLE[item] - 15
            quantity[item] = 0
        # 5H for 45
        elif item == 'H' and quantity[item] % 5 == 0:
            total_checkout += PRICE_TABLE[item] - 5
        # 2F get one F free
        elif item == 'F' and quantity[item] % 2 == 0:
            free_f_count += 1
            total_checkout += PRICE_TABLE[item]
        elif item == 'F' and free_f_count:
            free_f_count -= 1
            quantity[item] = 0
        # 2E get one B free
        elif item == 'E' and quantity[item] % 2 == 0:
            # keep count of how may B items shopper should get
            free_b_count += 1
            total_checkout += PRICE_TABLE[item]
        elif item == 'B' and free_b_count:
            free_b_count -=1 
            quantity[item] = 0
        # 2B for 45
        elif item == 'B' and quantity[item] % 2 == 0:
            total_checkout += PRICE_TABLE[item] - 15
        # 5A for 200
        elif item == 'A' and quantity[item] % 5 == 0:
            # add back money removed from special offer 3A
            total_checkout += 20
            # reset count
            quantity[item] = 0
        # 3A for 130
        elif item == 'A' and quantity[item] % 3 == 0:
            total_checkout += PRICE_TABLE[item] - 20
        else:
            total_checkout += PRICE_TABLE[item]
    return total_checkout
