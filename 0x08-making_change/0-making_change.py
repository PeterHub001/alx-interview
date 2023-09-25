#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0

    # Create a list to store the minimum number of coins needed for each amount from 0 to total
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make change for 0
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        for amount in range(coin, total + 1):
            # Calculate the minimum number of coins needed to make change for the current amount
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        # If dp[total] is still infinity, it means the total cannot be met by any combination of coins
        return -1
    else:
        return dp[total]

# Example usage:
coins = [1, 2, 5]
total = 11
result = make_change(coins, total)
print(result)  # Output should be 3 (1 * 5 + 2 * 3)
