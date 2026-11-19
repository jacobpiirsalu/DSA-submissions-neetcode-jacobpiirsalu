class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        hmap = {}
        for i,r in enumerate(recipes):
            hmap[r] = set(ingredients[i])
        ret = []
        
        def canBeMade(item,depth):
            #print(item)
            if depth > len(recipes): return False
            if item in supplies:
                return True
            if item not in hmap and item not in supplies:
                return False


            for subitem in hmap[item]:
                if not canBeMade(subitem,depth+1): return False
            return True
        
        for r in recipes:
            
            if canBeMade(r,0):
                ret.append(r)
        
        return ret
        

