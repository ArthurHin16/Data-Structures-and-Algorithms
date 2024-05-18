"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0
"""


def maxProfit(prices):
    max_profit = 0
    buy = prices[0]
    for i in range(1, len(prices)):
        sell = prices[i]
        profit = sell - buy
        max_profit = max(profit, max_profit)
        if sell < buy:
            buy = sell
    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))