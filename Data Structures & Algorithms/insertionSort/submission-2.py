# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) <= 0:
            return [] 
        elif len(pairs) == 1:
            print(len(pairs))
            return [pairs]
        else: #actual logic
            steps = []
            l_ptr = 0
            r_ptr = 1 # list has at least 2 elements
            steps.append(pairs.copy())
            while r_ptr < len(pairs): 
               
               if pairs[r_ptr].key < pairs[l_ptr].key:
                   
                   
                   
                   # keep swapping with the previous value until it's less than the one before it
                   curr_ptr = r_ptr
                   
                   while curr_ptr-1 >= 0 and pairs[curr_ptr].key < pairs[curr_ptr-1].key:
                       # swap the two
                       curr_pair = pairs[curr_ptr]
                       prev_pair = pairs[curr_ptr-1]
                       pairs[curr_ptr] = prev_pair
                       pairs[curr_ptr-1] = curr_pair
                       
                       curr_ptr-=1
                       # add this completed step to the list of steps
                       

               
               l_ptr+=1
               r_ptr+=1
               steps.append(pairs.copy())
            return steps