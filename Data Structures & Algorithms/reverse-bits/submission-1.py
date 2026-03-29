class Solution:
    def reverseBits(self, n: int) -> int:
        a = 0
        ctr=31
        while n!=0:
            bit_n = n & 1
            a = a + 2**ctr * bit_n
            
            ctr-=1
            n = n >> 1
        
        return a

        