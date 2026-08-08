class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, current_combination, total):
            if total == target:
                res.append(current_combination.copy())
                return
            if i >= len(candidates) or total > target:
                return

            current_combination.append(candidates[i])
            backtrack(i, current_combination, total + candidates[i])

            current_combination.pop()
            backtrack(i + 1, current_combination, total)

        backtrack(0, [], 0)
        return res