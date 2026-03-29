# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        insertions = []
        if len(pairs) == 0:
            return insertions

        list_ptr = 1
        swap_ptr = 0

        insertions.append(pairs.copy())

        while list_ptr <= len(pairs)-1:
            if pairs[list_ptr].key < pairs[swap_ptr].key:
                init_list_ptr = list_ptr
                init_swap_ptr = swap_ptr
                while pairs[list_ptr].key < pairs[swap_ptr].key and swap_ptr>=0:
                    tmp = pairs[swap_ptr]
                    pairs[swap_ptr] = pairs[list_ptr]
                    pairs[list_ptr] = tmp
                    
                    list_ptr-=1
                    swap_ptr-=1
                    

                
                list_ptr = init_list_ptr
                swap_ptr = init_swap_ptr
            
            list_ptr +=1
            swap_ptr +=1
            insertions.append(pairs.copy())

        return insertions
                
