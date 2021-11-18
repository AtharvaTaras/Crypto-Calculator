# Trading Profit Calculator

# Crypto to Fiat Price
buy = float(input('Enter buying price '))
sell = float(input('Enter selling price '))

# Investment
inv = float(input('Enter amount invested '))

# Volume Calculation
vol = (inv/buy)

# Trading Fee Buying
buy_fee = 0.001 * inv

# Return
retn = (sell * vol)

# Trading Fee Selling
sell_fee = 0.001 * retn

# Profit?
net_profit = round((retn - inv - buy_fee - sell_fee), 2)

if net_profit > 1:
    print()
    print('Net Profit', net_profit)
    print('Net Estimate 30 Days', round(30 * net_profit, 2))
    print()
    print('Current Transaction Profit %', (net_profit/inv) * 100)
    print('Estimated 30 Days Profit %', (30*net_profit/inv) * 100)

else:
    print('Trade Not Profitable')
    print('Loss', net_profit)
