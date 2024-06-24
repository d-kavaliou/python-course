# Exercise: Buy and Sell Stock

# solution 1

def buy_and_sell_stock_once(prices):
    profit = 0
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            current_profit = prices[j] - prices[i]
            if current_profit > profit:
                profit = current_profit
    return profit


prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_and_sell_stock_once(prices))
prices = [100, 180, 260, 310, 40, 535, 695]
print(buy_and_sell_stock_once(prices))

# solution 2

def buy_and_sell_once(prices):
    profit = 0
    min_price = 100000
    for price in prices:
        if price < min_price:
            min_price = price
        currtent_profit = price - min_price
        if currtent_profit > profit:
            profit = currtent_profit
    return profit

prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_and_sell_once(prices))
prices = [100, 180, 260, 310, 40, 535, 695]
print(buy_and_sell_stock_once(prices))


# educative solution

# def buy_and_sell_once(prices):
#     profit = 0
#     min_price = float('inf')
#   for price in prices:
#     min_price = min(min_price, price)
#     current_profit = price - min_price
#     profit = max(profit, current_profit)
#   return profit

