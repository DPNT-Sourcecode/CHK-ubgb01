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
    'K': 70,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21
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
    discount = 0
    pre_discount = 0
    free_b_count = 0
    free_f_count = 0
    free_m_count = 0
    free_q_count = 0
    free_u_count = 0
    any_three = []
    buy_two_with_discount = ['K', 'B', 'V']
    buy_three_with_discount = ['A', 'Q', 'V']
    buy_five_with_discount = ['P', 'H']
    two_get_one_free_sale = ['F', 'E']
    three_get_one_sale = ['U', 'R', 'N']
    
    if illegal_input(skus):
        return -1

    # sort and reverse string: EBBEEEB --> EEEEBBB
    skus = ''.join(sorted(skus, reverse=True))

    for item in skus:
        try:
            quantity[item] += 1
        except KeyError:
            quantity[item] = 1
        
        # 5A for 200
        if item == 'A' and quantity[item] % 5 == 0:
            # add back money removed from special offer 3A
            total_checkout += 20
            # reset count
            quantity[item] = 0

        # 3A for 130
        # 3Q for 80
        # 3V for 130
        elif item in buy_three_with_discount and quantity[item] % 3 == 0:
            if item == 'A':
                total_checkout += PRICE_TABLE[item] - 20
            elif item == 'Q':
                total_checkout += PRICE_TABLE[item] - 10
            elif item == 'V':
                total_checkout += PRICE_TABLE[item] - 10
                quantity[item] = 0

        # 2K for 120
        # 2B for 45
        # 2V for 90
        elif item in buy_two_with_discount and quantity[item] % 2 == 0:
            if item == 'K':
                total_checkout += PRICE_TABLE[item] -20
            elif item == 'B':
                total_checkout += PRICE_TABLE[item] - 15
            else:
                total_checkout += PRICE_TABLE[item] - 10

        # 3U get one U free 
        # 3R get one Q free 
        # 3N get one M free
        elif item in three_get_one_sale and quantity[item] % 3 == 0:
            if item == 'U':
                free_u_count += 1
            elif item == 'R':
                free_q_count += 1
            else:
                free_m_count += 1
            total_checkout += PRICE_TABLE[item]
        elif item == 'U' and free_u_count or \
             item == 'Q' and free_q_count or \
             item == 'M' and free_m_count:
            if item == 'U':
                free_u_count -= 1
            elif item == 'Q':
                free_q_count -= 1
            else:
                free_m_count -= 1
            quantity[item] = 0

        # 10H for 80
        elif item == 'H' and quantity[item] % 10 == 0:
            total_checkout += PRICE_TABLE[item] - 15
            quantity[item] = 0

        # 5P for 200 
        # 5H for 45
        elif item in buy_five_with_discount and quantity[item] % 5 == 0:
            if item == 'P':
                total_checkout += PRICE_TABLE[item] - 50
            else:
                total_checkout += PRICE_TABLE[item] - 5

        # 2F get one F free 
        # 2E get one B free
        elif item in two_get_one_free_sale and quantity[item] % 2 == 0:
            if item == 'F':
                free_f_count += 1
            else:
                free_b_count += 1
            total_checkout += PRICE_TABLE[item]
        elif item == 'F' and free_f_count or \
             item == 'B' and free_b_count:
            if item == 'F':
                free_f_count -= 1
            else:
                free_b_count -= 1
            quantity[item] = 0

        # buy any 3 of (S,T,X,Y,Z) for 45
        elif item in ['S', 'T', 'X', 'Y', 'Z']:
            total_checkout += PRICE_TABLE[item]
            pre_discount += PRICE_TABLE[item]
            any_three.append(item)
            if len(any_three) % 3 == 0:
                discount += pre_discount - 45
                pre_discount = 0
        else:
            total_checkout += PRICE_TABLE[item]
    
    total_checkout -= discount
    return total_checkout
