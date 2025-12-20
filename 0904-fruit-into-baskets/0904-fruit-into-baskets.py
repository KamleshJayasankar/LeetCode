class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        freq = {}
        max_len = 0

        for right in range(len(fruits)):
            freq[fruits[right]] = freq.get(fruits[right] , 0) + 1

            while(len(freq) > 2):
                left_fruit = fruits[left]
                freq[left_fruit] -= 1

                if freq[left_fruit] == 0:
                    del freq[left_fruit]
                
                left += 1

            max_len = max(max_len , right - left +1)

        return(max_len)