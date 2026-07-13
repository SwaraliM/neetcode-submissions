class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        cnt = {}
        maxFrequency = 0
        l = 0

        for i in range(len(s)):
            cnt[s[i]] = 1 + cnt.get(s[i], 0)
            maxFrequency = max(maxFrequency, cnt[s[i]])

            while(i-l+1) - maxFrequency > k:
                cnt[s[l]]-=1
                l += 1

            res = max(res, i-l+1)

        return res