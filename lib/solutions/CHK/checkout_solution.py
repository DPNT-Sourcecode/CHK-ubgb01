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
    if illegal_input(skus):
        return -1

    # sort `PRICE_TABLE` keys by value (descending order)
    items_ordered_by_price = sorted(PRICE_TABLE, key=PRICE_TABLE.__getitem__, reverse=True)

    # orders skus based on the list `items_ordered_by_price`,
    # example:
    #   INPUT skus = 'AAOLKK'
    #   items_ordered_by_price = ['L', 'K', 'J', 'A', 'P', 'O']
    #   OUTPUT skus = 'LKKAAO'
    skus = sorted(skus, key=lambda s: items_ordered_by_price.index(s))
    # convert to string
    skus = ''.join(skus)

    total_cost = 0
    pre_cost = 0
    discount = 0
    free_b_count = 0
    free_m_count = 0
    free_q_count = 0
    free_u_count = 0
    promo_items = []
    basket = {}

    for item in skus:
        try:
            basket[item]
        except KeyError:
            basket[item] = {'total_qnt': 0, 'qnt': 0, 'cost': 0}

        basket[item]['total_qnt'] += 1
        basket[item]['qnt'] += 1
        basket[item]['cost'] += PRICE_TABLE[item]

        # freebies
        if item == 'B' and free_b_count:
            free_b_count -= 1
            basket[item]['qnt'] -= 1
            basket[item]['cost'] -= PRICE_TABLE[item]

        elif item == 'M' and free_m_count:
            free_m_count -= 1
            basket[item]['qnt'] -= 1
            basket[item]['cost'] -= PRICE_TABLE[item]

        elif item == 'Q' and free_q_count:
            free_q_count -= 1
            basket[item]['qnt'] -= 1
            basket[item]['cost'] -= PRICE_TABLE[item]

        elif item == 'U' and free_u_count:
            free_u_count -= 1
            basket[item]['qnt'] -= 1
            basket[item]['cost'] -= PRICE_TABLE[item]

        # 10H for 80
        elif (
                item in ['H'] and
                basket[item]['qnt'] != 0 and
                basket[item]['qnt'] % 10 == 0
        ):
            if item == 'H':
                basket[item]['qnt'] = 0
                basket[item]['cost'] -= 15

        # 5A for 200
        # 5H for 45
        # 5P for 200
        elif (
                item in ['A', 'H', 'P'] and
                basket[item]['qnt'] != 0 and
                basket[item]['qnt'] % 5 == 0
        ):
            if item == 'A':
                # reset the number of items
                basket[item]['qnt'] = 0
                basket[item]['cost'] -= 30
            elif item == 'H':
                basket[item]['cost'] -= 5
            elif item == 'P':
                basket[item]['cost'] -= 50

        # 3A for 130
        # 2F get one F free (3F for 2F)
        # 3N get one M free
        # 3Q for 80
        # 3R get one Q free
        # 3U get one U free
        # 3V for 130
        elif (
                item in ['A', 'F', 'U', 'N', 'Q', 'V', 'R'] and
                basket[item]['qnt'] != 0 and
                basket[item]['qnt'] % 3 == 0
        ):
            if item == 'A':
                basket[item]['cost'] -= 20
            elif item == 'Q':
                basket[item]['cost'] -= 10
            elif item == 'V':
                # reset the number of items
                basket[item]['qnt'] = 0
                basket[item]['cost'] -= 10
            elif item == 'F':
                basket[item]['cost'] -= PRICE_TABLE[item]
            elif item == 'U':
                free_u_count += 1
            elif item == 'N':
                free_m_count += 1
            elif item == 'R':
                free_q_count += 1

        # 2B for 45
        # 2E get one B free
        # 2K for 120
        # 2V for 90
        elif (
                item in ['B', 'E', 'K', 'V'] and
                basket[item]['qnt'] != 0 and
                basket[item]['qnt'] % 2 == 0
        ):
            if item == 'B':
                basket[item]['cost'] -= 15
            elif item == 'K':
                basket[item]['cost'] -= 20
            elif item == 'V':
                basket[item]['cost'] -= 10
            elif item == 'E':
                free_b_count += 1

        # buy any 3 of (S,T,X,Y,Z) for 45
        elif item in ['S', 'T', 'X', 'Y', 'Z']:
            promo_items.append(PRICE_TABLE[item])

    for values in basket.values():
        total_cost += values['cost']

    if promo_items:
        for n_index, item_value in enumerate(promo_items, start=1):
            pre_cost += item_value
            if n_index % 3 == 0:
                discount += pre_cost - 45
                pre_cost = 0

        total_cost -= discount
    return total_cost
