class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict = {}
        answer = 0
        for i in nums:
            dict[i] = True
        for i in dict:
            if i - 1 not in dict:
                count = 1
                j = i + 1
                while j in dict:
                    count += 1
                    j += 1
                if answer < count: answer = count
        return answer
            