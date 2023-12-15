class Solution:
    def average(self, salary: List[int]) -> float:
        n=len(salary)
        ans=(sum(salary)-max(salary)-min(salary))/(n-2)
        return ans