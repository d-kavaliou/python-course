def buy_and_sell_stock_once(prices):
    
    sourted_prices = prices
    res = []
    for i in range(len(sourted_prices)):
        for j in range (len(prices)):
            if sourted_prices[i] == prices[j]:
                continue
            if sourted_prices[i] - prices[j] >=  0 and j < i :
                res.append(sourted_prices[i] - prices[j])
                
    res = sorted(res)
    if res == []:
        return 0
    else:
        return res[-1]

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

print(buy_and_sell_stock_once(A))
print(buy_and_sell_stock_once([100, 180, 260, 310, 40, 535, 695]))
print(buy_and_sell_stock_once([50, 50, 30, 20, 10]))
print(buy_and_sell_stock_once([110, 215, 180, 335, 5]))
