class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        frequencyOfNums = [[] for i in range(len(nums)+ 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, c in count.items():
            frequencyOfNums[c].append(num)

        result = []
        for i in range(len(frequencyOfNums) - 1, 0, -1):
            for num in frequencyOfNums[i]:
                result.append(num)
                if len(result) == k:
                    return result

        