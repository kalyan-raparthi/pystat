import matplotlib.pyplot as plt 

f = open("weekly_retail_price_rice_upto-2012.csv", 'r')
lines = f.readlines()

hyd_prices = []
for line in lines:
    element = line.strip().split(',')
    if element[2] == 'HYDERABAD' and element[3] != 'NA': hyd_prices.append(float(element[3]))

# print(hyd_prices)
plt.plot(hyd_prices)
plt.show()