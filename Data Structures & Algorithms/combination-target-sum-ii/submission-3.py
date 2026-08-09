class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        def backtrack(i, curr_sum, path):
            if curr_sum == target:
                res.append(path.copy())
                return

            for j in range(i, n):
                # Skip duplicates at the SAME recursion level
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                # Since candidates is sorted, everything after this
                # will also be too large
                if curr_sum + candidates[j] > target:
                    break

                path.append(candidates[j])

                # j + 1 because each candidate can only be used once
                backtrack(j + 1, curr_sum + candidates[j], path)

                path.pop()

        backtrack(0, 0, [])
        return res