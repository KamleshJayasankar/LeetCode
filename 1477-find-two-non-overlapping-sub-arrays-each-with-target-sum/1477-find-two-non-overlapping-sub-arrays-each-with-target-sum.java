class Solution {
    public int minSumOfLengths(int[] arr, int target) {
        int n = arr.length;
        int[] minLen = new int[n];
        Arrays.fill(minLen, Integer.MAX_VALUE);

        int left = 0;
        int currentSum = 0;
        int minTotalLen = Integer.MAX_VALUE;

        for (int right = 0; right < n; right++) {
            currentSum += arr[right];

            while (currentSum > target && left <= right) {
                currentSum -= arr[left++];
            }

            if (right > 0) {
                minLen[right] = minLen[right - 1];
            }

            if (currentSum == target) {
                int currLen = right - left + 1;

                if (left > 0 && minLen[left - 1] != Integer.MAX_VALUE) {
                    minTotalLen = Math.min(minTotalLen, currLen + minLen[left - 1]);
                }

                minLen[right] = Math.min(minLen[right], currLen);
            }
        }

        return minTotalLen == Integer.MAX_VALUE ? -1 : minTotalLen;
    }
}