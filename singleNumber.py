class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        freq = {}
        for numbers in nums:
            if numbers in freq:
                freq[numbers] +=1
            else:
                freq[numbers] =1

        for k,v in freq.items():
            if v ==1:
                return k

        # Below is a better solution

        # res=0
        # for num in nums:
        #     res = num^res
        #     print(res)
        # return res


        
