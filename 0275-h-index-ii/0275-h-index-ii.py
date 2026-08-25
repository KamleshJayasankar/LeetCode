class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            papers_count = n - mid

            if citations[mid] == papers_count:
                return papers_count
            elif citations[mid] < papers_count:
                left = mid + 1
            else:
                right = mid - 1

        return n - left