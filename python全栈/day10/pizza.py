def make_pizza(size, *toppings):
    """ 概述要制作的披萨 """
    print(f'\nmaking a {size}-inch pizza with rhe following toppings:')
    for topping in toppings:
        print(f'-{topping}')