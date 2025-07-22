class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr=[]
        p=0
        for i in nums:
            p= p+i
            arr.append(p)
        return arr
        
