# Labortation 1: Approximera en matematisk konstant

import random

n = 0

for k in range(1000000):
    x = random.random()
    y = random.random()
    # print(x)

    if x**2 + y**2 <= 1:
        # print('Innanför!')
        n = n + 1

    # print('Nu kör vi!')

ratio = n / 1000000
print(4 * ratio)