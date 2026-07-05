class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        maximum = answer = 0

        for num in nums:
            freq[num] += 1
            if maximum < freq[num]:
                answer = num
                maximum = freq[num]

        return answer
        