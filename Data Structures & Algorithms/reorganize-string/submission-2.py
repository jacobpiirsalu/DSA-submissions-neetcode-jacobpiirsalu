class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        if max(count.values()) > (len(s)+1)//2: return ""
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        ret = ""
        i = -1 #tracking - can't put 2 adjacent chars next to each other
        while maxHeap:
            currFreq, currChar = heapq.heappop(maxHeap)
            if i>=0 and ret[i] == currChar:
                #ignore currChar bc it would be adjacent

                #there's no other characters left to use, not possible
                #if not maxHeap: return ""

                nextFreq, nextChar = heapq.heappop(maxHeap)
                ret+=nextChar
                i+=1
                if nextFreq<-1: heapq.heappush(maxHeap,[nextFreq+1, nextChar])
                heapq.heappush(maxHeap,[currFreq, currChar])
            else:
                ret+=currChar
                i+=1
                if currFreq<-1: heapq.heappush(maxHeap,[currFreq+1, currChar])

        return ret
            