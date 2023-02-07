from pprint import pprint

# number of ways to get to amount with the given coins. 
def coin_change(coins=[1, 2, 5], amount=5):
    rows = len(coins)+1
    cols = amount+1

    dp = [[0]*cols]*rows

    for row in range(rows):
        dp[row][-1] = 1

    for row in range(len(coins)-1, -1, -1):
        for col in range(amount-1, -1, -1):
            dp[row][col] = dp[row+1][col]
            if coins[row] <= amount-col:
                dp[row][col] += dp[row][col+coins[row]]

    return dp[0][0]

print(coin_change(coins=[1, 2, 5], amount=5))
