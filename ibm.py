

def security(security, k):
    dp = [float('-inf') for _ in range(len(security)+1)]
    dp[len(security)] = 0
    for i in reversed(range(len(security))):
        dp[i] = dp[min(i+k, len(security))] + security[i]
    print(dp)
    return dp[0]


a=security([1, 2, 3, 4, 5], 2)
print(a)