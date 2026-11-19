class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        hmap = {}
        for i,r in enumerate(recipes):
            hmap[r] = set(ingredients[i])
        ret = []
        memo = {}
        
        def canBeMade(item,depth):
            #print(item)
            if item in memo:
                return memo[item]

            if depth > len(recipes): 
                memo[item] = False
                return False
            if item in supplies:
                memo[item] = True
                return True
            if item not in hmap and item not in supplies:
                memo[item] = False
                return False


            for subitem in hmap[item]:
                if not canBeMade(subitem,depth+1): 
                    memo[item] = False
                    return False
            
            memo[item]=True
            return True
        
        for r in recipes:
            
            if canBeMade(r,0):
                ret.append(r)
        
        return ret
        

