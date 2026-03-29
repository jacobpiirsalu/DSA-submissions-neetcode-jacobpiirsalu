class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(n+1):
            num = i
            if num==0: 
                lst.append(0)
                continue
            
            count=0
            while num!=0:
                if num & 1 == 1:
                    count+=1
                num = num >> 1
            lst.append(count)
        
        return lst