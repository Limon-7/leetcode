class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        max_seq = 0

        for num in nums:
            if num - 1 not in n_set:
                curr_num = num
                curr_seq = 1
                while curr_num + 1 in n_set:
                    curr_seq += 1
                    curr_num += 1

                max_seq = max(max_seq, curr_seq)

        return max_seq
