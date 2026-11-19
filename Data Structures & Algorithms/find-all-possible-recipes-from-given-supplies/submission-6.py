class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        hmap = {}
        for i,r in enumerate(recipes):
            hmap[r] = set(ingredients[i])
        ret = []
        memo = {}
        path = set()
        
        def canBeMade(item):
            #print(item)
            if item in memo:
                return memo[item]

            if item in path: 
                return False
            if item in supplies:
                memo[item] = True
                return True
            if item not in hmap and item not in supplies:
                memo[item] = False
                return False

            path.add(item)
            for subitem in hmap[item]:
                if not canBeMade(subitem):
                    path.discard(item) 
                    memo[item] = False
                    return False
            
            path.discard(item)
            memo[item]=True
            return True
        
        for r in recipes:
            
            if canBeMade(r):
                ret.append(r)
        
        return ret
        

