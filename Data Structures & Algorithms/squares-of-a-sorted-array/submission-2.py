# trivial solution
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ret = []
        bkpt = len(nums)-1
        for i in range(len(nums)):
            if nums[i] >= 0:
                bkpt = i
                break

        negs = [x**2 for x in nums[:bkpt]]
        pos = [x**2 for x in nums[bkpt:]]

        L,R = len(negs)-1, 0
        print(negs)
        print(pos)
        while L>=0 and R<len(pos):
            if negs[L] <= pos[R]:
                ret.append(negs[L])
                L-=1
            else:
                ret.append(pos[R])
                R+=1
        print(L)
        while L>=0:
            ret.append(negs[L])
            L-=1
        while R<len(pos):
            ret.append(pos[R])
            R+=1

        return ret