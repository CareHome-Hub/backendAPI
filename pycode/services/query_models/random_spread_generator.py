import numpy as np, numpy.random

# print ("Spread = {}".format(np.random.dirichlet(np.ones(10), size=3)))

def generate_spread_to_total(values_total = 100, num_Values=5):
    _sum = values_total

    n = num_Values

    spread_array = np.random.multinomial(_sum, np.ones(n)/n, size=1)[0]
    print("Spread = {}".format(spread_array))
    return spread_array

generate_spread_to_total()
generate_spread_to_total(50, 3)