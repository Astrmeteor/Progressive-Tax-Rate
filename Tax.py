import numpy as np
import matplotlib.pyplot as plt
"""
level amount ratio
1 1-5000    0%
2 5001-8000 3%
3 8001-17000    10%  
4 17001-30000   20%
5 30001-40000   25%
6 40001-60000   30%
7 60001-85000   35%
8 85001~        45%
"""
# level: [ratio, max amount, min,  maximum]
tax_level = {
    1: [0, 0, 1, 5000],
    2: [0.03, 89.97, 5001, 8000],
    3: [0.1, 899.9, 8001, 17000],
    4: [0.2, 2599.8, 17001, 30000],
    5: [0.25, 2499.75, 30001, 40000],
    6: [0.3, 5999.7, 40001, 60000],
    7: [0.35, 6999.65, 60001, 850000],
    8: [0.45, None, 85001, None]
}

level = None


def tax(x):
    global tax_level
    global level
    if 1 <= x <= 5000:
        level = 1
    elif 5001 <= x <= 8000:
        level = 2
    elif 8001 <= x <= 17000:
        level = 3
    elif 17001 <= x <= 30000:
        level = 4
    elif 30001 <= x <= 40000:
        level = 5
    elif 40001 <= x <= 60000:
        level = 6
    elif 60001 <= x <= 85000:
        level = 7
    elif x >= 85001:
        level = 8
    else:
        print(ValueError)
        exit()
    # print(level)

    # level: [ratio, max amount, min,  maximum]
    tax_amount = (x-tax_level[level][2])*tax_level[level][0]
    for i in range(1, level):
        tax_amount += tax_level[i][1]

    return tax_amount
    # print(tax_amount)


if __name__ == '__main__':
    arr = np.arange(1, 100001, 1)
    vec_tax = np.vectorize(tax)
    tax_amount = vec_tax(arr)
    ratio = tax_amount / arr
    fig = plt.figure()
    plt.plot(ratio)
    plt.show()
    # tax()
