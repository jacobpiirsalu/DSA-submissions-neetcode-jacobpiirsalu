class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def realMergeSort(self, pairs, startIdx, endIdx):
        if endIdx-startIdx <=0:
            return pairs

        midIdx = (startIdx + endIdx)//2

        self.realMergeSort(pairs, startIdx, midIdx)
        self.realMergeSort(pairs, midIdx+1, endIdx)
        self.merge(pairs, startIdx, endIdx)

        return pairs

    def merge(self, pairs, startIdx, endIdx):
        mid_idx = (startIdx + endIdx)//2

        l_ptr = startIdx
        r_ptr = mid_idx+1

        newArr = []

        while l_ptr <= mid_idx or r_ptr <= endIdx:
            # both ptrs in bounds
            if l_ptr <= mid_idx and r_ptr <= endIdx:
                if pairs[l_ptr].key <= pairs[r_ptr].key:
                    newArr.append(pairs[l_ptr])
                    l_ptr+=1
                else:
                    newArr.append(pairs[r_ptr])
                    r_ptr+=1
            #only left pointer in bounds
            elif l_ptr <=mid_idx and r_ptr > endIdx:
                newArr.append(pairs[l_ptr])
                l_ptr+=1
            else: #only right ptr in bounds
                newArr.append(pairs[r_ptr])
                r_ptr+=1

        # overwrite pairs with the newArr in that section
        for i in range(startIdx, endIdx+1):
            pairs[i] = newArr[i-startIdx]

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.realMergeSort(pairs, 0, len(pairs)-1)