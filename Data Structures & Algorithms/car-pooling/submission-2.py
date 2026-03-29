class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        print(trips)
        prevEnd = 0
        currPassengers=0

        for tcap,s,e in trips:
            #trips can overlap, we just can't pick up passengers over our capacity if we do overlap
            #at the start of the trip we add to currPassengers, at the end we subtract from it
            if [tcap, s, e] == trips[0]:
                if currPassengers+tcap > capacity:
                    return False
                else:
                    currPassengers+=tcap
                    prevEnd = e
            else:
                if prevEnd>s: 
                    currPassengers = currPassengers+tcap
                else: currPassengers = tcap
                
                if currPassengers>capacity or s>e:
                    return False
                prevEnd = e
        return True
        