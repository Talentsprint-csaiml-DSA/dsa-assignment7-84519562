def longest_common_subsequence(X,Y):
    # ToDo 


    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
  
    lcs_length = dp[m][n]


    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    

    lcs = ''.join(reversed(lcs))

    return lcs_length, lcs


X = "dynamicprogramming"
Y = "machinelearning"
lcs_length, lcs = longest_common_subsequence(X, Y)
print(f"Length of LCS: {lcs_length}")
print(f"LCS: {lcs}")
