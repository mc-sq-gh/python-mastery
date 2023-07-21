# pcost.py

total_cost = 0.0

with open("../../Data/portfolio.dat", 'r') as f:
    for line in f:
        elems = line.split(' ')
        shares = int(elems[1])
        price = float(elems[2])
        total_cost += shares * price

print(total_cost)
