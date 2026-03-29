class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        smap, tmap = {}, {}
        for c in s:
            smap[c] = smap.get(c,0) + 1
        for c in t:
            tmap[c] = tmap.get(c,0) + 1
        
        count=0
        #insert
        if len(t)>=len(s):
            for k,v in tmap.items():
                if k not in smap:
                    count+=v
                else:
                    count+=abs(v-smap[k])
        else:
            for k,v in smap.items():
                if k not in tmap:
                    count+=v
                else:
                    count+=abs(v-tmap[k])
        
        return count==1
        