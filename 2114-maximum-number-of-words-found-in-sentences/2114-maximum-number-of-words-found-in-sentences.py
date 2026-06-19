class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count = 0
        for sentence in sentences:
            current_count = sentence.count(" ")+1
            if current_count > max_count:
                max_count = current_count
        return max_count