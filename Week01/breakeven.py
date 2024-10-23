#varables for cost of item , sell price ( production + profit) and fixed costs ( money commited) 
production_cost = float(20)
selling_price = float(40)
fixed_costs = float(50000)
profit = selling_price-production_cost
print("profit =",profit)
#calculation 
breakeven = fixed_costs/production_cost-selling_price
print("units needed to break even =", breakeven)