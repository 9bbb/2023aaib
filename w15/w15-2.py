class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s) #長度
        zero = 0#等一下也要
        one = 0#找出全部的1
        for i in range(n):
            if s[i]=='1': one += 1#如果是1先全部加起來
#現在就知道總共有幾個 one
        ans = 0
        for i in range(n-1):
            if s[i]=='0':
                zero += 1
            if s[i]=='1':
                one -= 1
            ans = max( ans, zero+one)
        return ans