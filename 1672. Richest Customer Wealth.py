# Approach 1

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=[]
        for acc in accounts:
            wealth.append(sum(acc))

        return max(wealth)



# Approach 2

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        return max(sum(acc) for acc in accounts)
