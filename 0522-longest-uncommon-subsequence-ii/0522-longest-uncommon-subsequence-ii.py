class Solution(object):
    def findLUSlength(self, strs):
        def isSubSequence(a, b):
            i = 0
            for ch in b:
                if i < len(a) and a[i] == ch:
                    i += 1
            return i == len(a)
        strs.sort(key = len, reverse = True)
        for i in range(len(strs)):
            uncommon = True
            for j in range(len(strs)):
                if i != j and isSubSequence(strs[i], strs[j]):
                    uncommon = False
                    break
            if uncommon:
                return len(strs[i])
        return -1
        