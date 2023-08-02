# pcost.py

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'r') as f:
        for line in f:
            elems = line.split()
            try:
                shares = int(elems[1])
                price = float(elems[2])
            except ValueError as e:
                print(f"Couldn't parse: {line.strip()}")
                print(f"Reason: {e}")
                continue

            total_cost += shares * price

    return total_cost

print("P1: "+ str(portfolio_cost("../../Data/portfolio.dat")))
print("P3: "+ str(portfolio_cost("../../Data/portfolio3.dat")))
