class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()

        for Bptr in range(len(nums)):
            if Bptr>0 and nums[Bptr] == nums[Bptr-1]:
                continue
            l,r = Bptr+1,len(nums)-1
            while l<r:
                print(l)
                print(r)
                if l == Bptr:
                    l+=1
                    continue
                if r==Bptr:
                    r-=1
                    continue
                
                summ = nums[Bptr] + nums[l] + nums[r]
                if summ == 0:
                    ret.append([nums[Bptr], nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                elif summ < 0: #increase size:
                    l+=1
                elif summ > 0: #decr size
                    r-=1
                
        return ret

