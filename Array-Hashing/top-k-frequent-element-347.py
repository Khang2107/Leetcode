'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. 

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

'''

from heapq import heappush, heappop


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # create a dictionary to store the frequency of each number in the list
        freq_dict = {}
        for num in nums:
            # reverse the dictionary
            # using priority queue
            # most appeared elements will have smallest negative frequency in heap
            if num not in freq_dict:
                freq_dict[num] = -1
            else:
                # the more appeared the number, the smaller negative value is
                # opposite to += 1
                freq_dict[num] -= 1
        # print(freq_dict)

        # create the heap from dictionary to sort the numbers based on their frequency
        heap = []
        # loop over frequency dict
        for key in freq_dict:
            # for each key, we have tuple (freq_dict[key], key)
            # where freq_dict[key] is negative frequency of element represented by key
            # after we push the tuple into heap, heap will sort in order based on the negative frequency:
            # -3 first -> -1
            # eg: {1:-3, 2:-2, 3:-1} -> (-3,1) (-2,2) (-1,3)
            # eg: {1:-2, 2:-3, 3:-1} -> (-3,2) (-2,1) (-1,3)
            # then we will push the tuple into heap
            heappush(heap, (freq_dict[key], key))
            # print(heap)

        res = []
        for i in range(k):
            # use heappop to remove element with smallest negative frequency from heap
            # when heappop runs, it returns the tuple with the smallest frequency
            # in form (frequency: negative, element)
            freq, item = heappop(heap)
            res.append(item)
        return res
