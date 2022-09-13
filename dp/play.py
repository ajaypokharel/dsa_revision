

def probWarriorsWin(w, r, dp):
    if w >= 4:
        return 1
    elif r >= 4:
        return 1

    elif (w + r) + 1 in [1, 2, 5, 7]:
        dp[w][r].append((0.5 * probWarriorsWin(w+1, r, dp)) + (0.5 * probWarriorsWin(w, r+1, dp)))

    elif (w + r) + 1 in [3, 4, 6]:
        dp[w][r].append(0.7 * probWarriorsWin(w + 1, r, dp)) + (0.3 * probWarriorsWin(w, r+1, dp))


dp = [[] for i in range(5) for j in range(4)]

probWarriorsWin(0, 0, dp)
