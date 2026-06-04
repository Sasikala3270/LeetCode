class Solution(object):
    def totalWaviness(self, num1, num2):
        def waviness(num):
            s = str(num)
            n = len(s)
            if n < 3:
                return 0
            count = 0
            for i in range(1, n-1):
                left = int(s[i-1])
                cur = int(s[i])
                right = int(s[i + 1])

                if(cur > left and cur > right) or (cur < left and cur < right):
                    count += 1
            return count
        ans = 0
        for num in range(num1, num2+1):
            ans += waviness(num)
        return ans